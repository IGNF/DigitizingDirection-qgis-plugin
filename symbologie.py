from qgis.PyQt.QtGui import QColor
from qgis.core import (Qgis,QgsRendererCategory, QgsCategorizedSymbolRenderer,QgsSymbol,QgsWkbTypes
            ,QgsSingleSymbolRenderer, QgsRuleBasedRenderer, QgsProject,QgsUnitTypes, QgsMapUnitScale)

from .mapping_version import *

class SensNumerisation:
    def __init__(self, iface):
        self.saved_renderers = {}
        self.layer = None
        self.iface = iface
        self.is_affiche_sens_num = False

    def initGui(self):
        pass

    def unload(self):
        pass

    def init_symbole(self):
        # Créer le triangle comme SimpleMarkerLayer
        triangle_layer = QgsSimpleMarkerSymbolLayer()
        # triangle_layer.setShape(Triangle)
        triangle_layer.setShape(Arrow)
        triangle_layer.setColor(QColor(255, 0, 0))
        triangle_layer.setSize(12)
        triangle_layer.setAngle(90)

        # Créer un QgsSymbol pour le MarkerLine
        triangle_symbol = QgsSymbol.defaultSymbol(QgsWkbTypes.PointGeometry)
        triangle_symbol.deleteSymbolLayer(0)  # supprime le SimpleMarker par défaut
        triangle_symbol.appendSymbolLayer(triangle_layer)

        triangle_symbol.setSizeUnit(QgsUnitTypes.RenderMapUnits)
        triangle_symbol.setSizeMapUnitScale(QgsMapUnitScale(0, 0))

        # marque ligne
        ml = QgsMarkerLineSymbolLayer()
        ml.setSubSymbol(triangle_symbol)  #  ici on passe un QgsSymbol
        ml.setPlacement(QgsMarkerLineSymbolLayer.Interval)
        ml.setInterval(30)
        ml.setIntervalUnit(QgsUnitTypes.RenderMapUnits)
        # ml.setOffset(1)
        # ml.setOffsetUnit(QgsUnitTypes.RenderMapUnits)
        return ml

    def add_symb_sens_num_all_layer(self,layer):
        renderer = layer.renderer()

        if renderer.type() == "singleSymbol":
            ml = self.init_symbole()
            # Ajouter la MarkerLine au symbole existant
            sym = renderer.symbol().clone()
            sym.appendSymbolLayer(ml)

            layer.setRenderer(QgsSingleSymbolRenderer(sym))
            layer.setCustomProperty("extra_triangle_single",sym.symbolLayerCount() - 1)

        elif renderer.type() == "RuleRenderer":
            root = renderer.rootRule().clone()
            rules_to_process = [root]
            while rules_to_process:
                rule = rules_to_process.pop()
                sym = rule.symbol()
                if sym:
                    sym = sym.clone()
                    ml = self.init_symbole()
                    sym.appendSymbolLayer(ml)
                    rule.setSymbol(sym)
                rules_to_process.extend(rule.children())
            layer.setRenderer(QgsRuleBasedRenderer(root))

        elif renderer.type() == "categorizedSymbol":
            new_categories = []
            for cat in renderer.categories():
                sym = cat.symbol().clone()  # cloner le symbole existant
                ml = self.init_symbole()
                # Ajouter la MarkerLine au symbole existant
                sym.appendSymbolLayer(ml)
                # Stocker un identifiant pour suppression future
                layer.setCustomProperty(f"categorie_{cat.value()}", sym.symbolLayerCount() - 1)
                # Nouvelle catégorie
                new_cat = QgsRendererCategory(cat.value(), sym, cat.label())
                new_categories.append(new_cat)

            # Appliquer le nouveau renderer
            new_renderer = QgsCategorizedSymbolRenderer(renderer.classAttribute(), new_categories)
            layer.setRenderer(new_renderer)
        layer.triggerRepaint()

    def add_symb_sens_num(self, layer):
        renderer = layer.renderer()
        # =========================
        # SINGLE SYMBOL
        # =========================
        if renderer.type() == "singleSymbol":
            base_symbol = renderer.symbol().clone()
            # Symbole spécial sélection
            selected_symbol = base_symbol.clone()
            ml = self.init_symbole()
            selected_symbol.appendSymbolLayer(ml)
            # Règle sélection
            selected_rule = QgsRuleBasedRenderer.Rule(selected_symbol)
            selected_rule.setFilterExpression("is_selected()")
            # Règle normale
            normal_rule = QgsRuleBasedRenderer.Rule(base_symbol)
            normal_rule.setIsElse(True)
            root = QgsRuleBasedRenderer.Rule(None)
            root.appendChild(selected_rule)
            root.appendChild(normal_rule)
            layer.setRenderer(QgsRuleBasedRenderer(root))

        # =========================
        # RULE RENDERER
        # =========================
        elif renderer.type() == "RuleRenderer":
            root = QgsRuleBasedRenderer.Rule(None)
            rules_to_process = renderer.rootRule().children()
            for rule in rules_to_process:
                # symbole normal
                normal_rule = rule.clone()
                # symbole sélection
                selected_symbol = rule.symbol().clone()
                ml = self.init_symbole()
                selected_symbol.appendSymbolLayer(ml)
                selected_rule = QgsRuleBasedRenderer.Rule(selected_symbol)
                selected_rule.setFilterExpression(
                    f"is_selected() AND ({rule.filterExpression()})"
                    if rule.filterExpression()
                    else "is_selected()"
                )
                root.appendChild(selected_rule)
                root.appendChild(normal_rule)
            layer.setRenderer(QgsRuleBasedRenderer(root))

        # =========================
        # CATEGORIZED SYMBOL
        # =========================
        elif renderer.type() == "categorizedSymbol":
            root = QgsRuleBasedRenderer.Rule(None)
            field_name = renderer.classAttribute()
            for cat in renderer.categories():
                # expression catégorie
                expr = f"\"{field_name}\" = '{cat.value()}'"
                # symbole normal
                normal_symbol = cat.symbol().clone()
                normal_rule = QgsRuleBasedRenderer.Rule(normal_symbol)
                normal_rule.setFilterExpression(expr)
                # symbole sélection
                selected_symbol = cat.symbol().clone()
                ml = self.init_symbole()
                selected_symbol.appendSymbolLayer(ml)
                selected_rule = QgsRuleBasedRenderer.Rule(selected_symbol)
                selected_rule.setFilterExpression(
                    f"is_selected() AND {expr}"
                )
                root.appendChild(selected_rule)
                root.appendChild(normal_rule)
            layer.setRenderer(QgsRuleBasedRenderer(root))
        layer.triggerRepaint()

    def suppr_symb_sens_num(self,layer):
        renderer = layer.renderer()
        if renderer.type() == "singleSymbol":
            sym = renderer.symbol().clone()
            idx = layer.customProperty("extra_triangle_single", None)
            if idx is not None:
                idx = int(idx)
                if 0 <= idx < sym.symbolLayerCount():
                    sym.deleteSymbolLayer(idx)
                layer.removeCustomProperty("extra_triangle_single")
            layer.setRenderer(QgsSingleSymbolRenderer(sym))

        elif renderer.type() == "RuleRenderer":
            root = renderer.rootRule().clone()
            rules_to_process = [root]
            while rules_to_process:
                rule = rules_to_process.pop()
                rule_sym = rule.symbol()
                if rule_sym:
                    sym = rule_sym.clone()
                    # Supprimer uniquement le dernier MarkerLine (le triangle ajouté)
                    for i in reversed(range(sym.symbolLayerCount())):
                        sl = sym.symbolLayer(i)
                        if isinstance(sl, QgsMarkerLineSymbolLayer):
                            sym.deleteSymbolLayer(i)
                            break  # on supprime seulement le dernier
                    rule.setSymbol(sym)
                rules_to_process.extend(rule.children())
            layer.setRenderer(QgsRuleBasedRenderer(root))

        elif renderer.type() == "categorizedSymbol":
            new_categories = []
            for cat in renderer.categories():
                sym = cat.symbol().clone()  # clone pour ne pas modifier l'original
                # Supprimer uniquement le dernier MarkerLine ajouté
                for i in reversed(range(sym.symbolLayerCount())):
                    sl = sym.symbolLayer(i)
                    if isinstance(sl, QgsMarkerLineSymbolLayer):
                        sym.deleteSymbolLayer(i)
                        break  # on supprime seulement le dernier ajouté
                # Recréer la catégorie avec le symbole modifié
                new_cat = QgsRendererCategory(cat.value(), sym, cat.label())
                new_categories.append(new_cat)
            # Recréer le renderer catégorisé
            new_renderer = QgsCategorizedSymbolRenderer(renderer.classAttribute(), new_categories)
            layer.setRenderer(new_renderer)
        layer.triggerRepaint()

    def restore_renderer(self, layer):
        renderer = self.saved_renderers.get(layer.id())
        if renderer is not None:
            try:
                layer.styleChanged.disconnect(self.on_style_changed)
            except TypeError:
                pass
            layer.setRenderer(renderer.clone())
            layer.styleChanged.connect(self.on_style_changed)
            layer.triggerRepaint()

    def on_style_changed(self):
        if self.layer is None:
            return
        if not self.is_affiche_sens_num:
            self.saved_renderers[self.layer.id()] = self.layer.renderer().clone()

    def run(self):
        projet = QgsProject.instance()
        if len(projet.mapLayers()) <= 0:
            QMessageBox.warning(self.iface.mainWindow(), "Attention", "veuillez charger un projet", Ok)
            return
        self.layer = self.iface.activeLayer()
        if not self.layer:
            return

        # événement de changement de style du layer pour sauvegarder le style original
        try:
            self.layer.styleChanged.disconnect(self.on_style_changed)
        except TypeError:
            pass
        self.layer.styleChanged.connect(self.on_style_changed)

        if not self.is_affiche_sens_num:
            self.saved_renderers[self.layer.id()] = self.layer.renderer().clone()


        if self.is_affiche_sens_num:
            # self.suppr_symb_sens_num(self.layer)
            self.restore_renderer(self.layer)
            self.is_affiche_sens_num = False
        else:
            # sauvegarde AVANT modification
            self.saved_renderers[self.layer.id()] = self.layer.renderer().clone()

            # bloque le sauvegarde automatique pendant le changement
            self.is_affiche_sens_num = True

            if self.layer.selectedFeatureCount():
                self.add_symb_sens_num(self.layer)
            else:
                self.add_symb_sens_num_all_layer(self.layer)
