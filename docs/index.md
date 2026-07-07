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
<td style="text-align: center;"><p><strong>Manuel utilisateur du plugin
«sens de numérisation» </strong></p>
<p><strong>v0.4.2</strong></p></td>
</tr>
<tr>
<td style="font-size: 16px;text-align: center;">Développeur  : Gérôme PECHEUR (IGN)</td>
</tr>
</tbody>
</table>




## Sommaire

- [1. Prérequis](#prerequis)

- [2. Présentation](#presentation)

- [3. Utilisation](#utilisation)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="prerequis" style="color: white;margin:0;" >1. Prérequis</h2>
</div>

- Version de QGIS : 3.28 ou supérieur

- Le plugin « maitre » doit préalablement être installé : 
[maitre-qgis-plugin sur GitHub](https://github.com/IGNF/maitre-qgis-plugin)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="presentation" style="color: white;margin:0;" >2. Présentation</h2>
</div>

Ce plugin affiche sur le layer actif, le sens de numérisation sous la
forme d’une petite flèche sur chaque entité

Seuls les layers de type linéaire sont prise en compte.

Il se « lance » via le menu IGN ou via le
bouton<img src="images/image2.png"
style="width:0.29025in;height:0.27498in" /> dans la barre d’outils
(suivant la configuration du plugin maitre)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="utilisation" style="color: white;margin:0;" >3. Utilisation</h2>
</div>

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
