from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QTabBar,QMessageBox,QAbstractItemView,QListWidget
from qgis.core import QgsSimpleMarkerSymbolLayer,QgsMarkerLineSymbolLayer

# QT6
try :
    Dialog = Qt.WindowType.Dialog
    WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowType.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
    Checked = Qt.CheckState.Checked
    Unchecked = Qt.CheckState.Unchecked
    ItemIsEnabled = Qt.ItemFlag.ItemIsEnabled
    ItemIsUserCheckable = Qt.ItemFlag.ItemIsUserCheckable
    MatchExactly = Qt.MatchFlag.MatchExactly
    RightSide = QTabBar.ButtonPosition.RightSide
    LeftSide = QTabBar.ButtonPosition.LeftSide
    Warning = QMessageBox.Icon.Warning
    YesRole = QMessageBox.ButtonRole.YesRole
    Ok = QMessageBox.StandardButton.Ok
    AcceptRole = QMessageBox.ButtonRole.AcceptRole
    NoSelection = QAbstractItemView.SelectionMode.NoSelection
    Triangle = QgsSimpleMarkerSymbolLayer.Shape.Triangle
    Arrow = QgsSimpleMarkerSymbolLayer.Shape.Arrow
    Interval = QgsMarkerLineSymbolLayer.Placement.Interval
# QT5
except :
    Dialog = Qt.Dialog
    WindowCloseButtonHint = Qt.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowStaysOnTopHint
    Checked = Qt.Checked
    Unchecked = Qt.Unchecked
    ItemIsEnabled = Qt.ItemIsEnabled
    ItemIsUserCheckable = Qt.ItemIsUserCheckable
    MatchExactly = Qt.MatchFlag.MatchExactly
    RightSide = QTabBar.RightSide
    LeftSide = QTabBar.LeftSide
    Warning = QMessageBox.Warning
    YesRole = QMessageBox.YesRole
    Ok = QMessageBox.Ok
    AcceptRole = QMessageBox.AcceptRole
    NoSelection = QListWidget.NoSelection
    Triangle = QgsSimpleMarkerSymbolLayer.Triangle
    Arrow = QgsSimpleMarkerSymbolLayer.Arrow
    Interval = QgsMarkerLineSymbolLayer.Interval