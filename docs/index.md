<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><img src="images/image1.jpeg"
style="width:1.38681in;height:1.47153in"
alt="logo_IGN_pour_lettre" /></td>
<td style="text-align: center;"><strong>Manuel utilisateur du plugin
« sens de numérisation »</strong></td>
</tr>
<tr>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

| Version | Date       | Modifié par    | Historique des modifications |
|---------|------------|----------------|:----------------------------:|
|         |            |                |                              |
| 1.0.0   | 07/07/2025 | Gérôme PECHEUR |  Première version diffusée   |

**Sommaire**

[1 Prérequis](#prérequis)

[2 Présentation](#présentation)

[3 Utilisation](#utilisation)

# Prérequis

- Version de QGIS : 3.28 ou supérieur

- Le plugin « maitre » doit préalablement être installé et configuré

# Présentation 

Ce plugin affiche sur le layer actif, le sens de numérisation sous la
forme d’une petite flèche sur chaque entité

Seuls les layers de type linéaire sont prise en compte.

Il se « lance » via le menu IGN ou via le
bouton<img src="images/image2.png"
style="width:0.29025in;height:0.27498in" /> dans la barre d’outils
(suivant la configuration du plugin maitre)

# Utilisation 

Si on essaye d’afficher le sens de numérisation sur un layer qui n’est
pas de type linéaire, un warning s’affiche dans QGIS

<img src="images/image3.png"
style="width:5.15035in;height:0.27934in" />

On active/désactive l’affichage par appuis successif sur le bouton
<img src="images/image2.png"
style="width:0.29025in;height:0.27498in" />

2 cas possibles :

1 : Le layer actif n’a aucune sélection, dans ce cas toutes les entités
affichent une petite flèche.

<img src="images/image4.png"
style="width:3.00223in;height:1.50508in" />

2 : Des entités sont sélectionnées, dans ce cas, seuls ces entités
affichent une petite flèche

<img src="images/image5.png"
style="width:2.49555in;height:1.9131in" />
