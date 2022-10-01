# ProfLycee
Package, sans aucune prétention, pour quelques commandes LaTeX potentiellement utiles au lycée !

Pour le moment :

- Quelques commandes pour des courbes lisses avec gestion des extrema et des dérivées.
- Quelques commandes pour simuler une fenêtre de logiciel de calcul formel, en TikZ.
- Quelques environnements (tcbox) pour présenter du code python ou pseudocode.
- Quelques environnements (tcbox) pour présenter des commandes dans un terminal (win ou mac ou linux).
- Un cartouche (tcbox) pour présenter des codes de partage capytale.
- Une commande pour tracer un pavé en droit, en TikZ, avec création des nœuds liés aux sommets.
- Une commande pour simplifier des calculs sous forme fractionnaire.
- Une commande pour simplifier l’écriture d’un ensemble, avec espaces « automatiques ».
- Une commande pour créer, en TikZ, la toile pour une suite récurrente.
- Une commande pour créer, en TikZ, un cercle trigo avec options.
- Une commande pour afficher un petit schéma, en TikZ, sur le signe d’une fonction affine ou d’un trinôme.
- Deux commandes pour, en TikZ, créer des petits schémas « de signe ».
- Une commande pour travailler sur les statistiques à deux variables (algébriques et graphiques).
- Quelques commandes pour convertir bin/dec/hex avec certains détails.
- Une commande pour, en TikZ, créer un pixelart avec correction éventuelle.
- Une commande pour, en TikZ, créer un SudoMaths non forcément 9×9.
- Des commandes pour effectuer des calculs de probabilités avec des lois classiques.

## Courbe d'interpolation

La commande <code>\splinetikz[...]</code>, trace un ensemble de <i>splines</i> grâce notamment à une liste de points sous la forme <code>x1/y1/d1§x2/y2/d2§...</code> et une liste des coefficients de <i>compensation</i> sous la forme <code>C1G/C1D§C2G/C2D§...</code> (qui peut être simplifiée si on le souhaite !).

Également de quoi tracer, grâce à la commande <code>\tangentetikz[...]</code>, (une ou) des tangentes à l'aide de triplets <code>xa/ya/da§...</code> pour tracer une (portion de) tangente via <code>da*(x-xa)+ya</code>.

![illustr](./test/proflycee-test-splines.png?raw=true "testsplines")

## Émulation fenêtre de calcul formel

Une commande <code>\paramCF[...]</code> pour paramétrer la *fenêtre de travail* du calcul formel.

Une commande <code>\ligneCF[...]</code> pour créer les lignes de la *fenêtre de travail*.

![illustr](./test/proflycee-test-calcformel.png?raw=true "testcalc")

## Code et console Python

Un environnement <code>envcodepythontex[...]</code> pour présenter du code Python via pythontex.

Un environnement <code>envconsolepythontex[...]</code> pour présenter une console Python.

Un environnement <code>envconsolepythonminted[...]</code> pour présenter du code Python via minted.

![illustr](./test/proflycee-test-codepython.png?raw=true "testcode")

## Terminal Win/UNiX/OSX

Un environnement <code>PLtermwin[...]</code> pour un terminal Win.

Un environnement <code>PLterunix[...]</code> pour un terminal UNiX.

Un environnement <code>PLtermosx[...]</code> pour un terminal OSX.

![illustr](./test/proflycee-test_terminals.png?raw=true "testterminals")

## Cartouche Capytale

Un cartouche <code>liencapytale(*)[...]{...}</code> pour un cartouche de partage de lien capytale.

![illustr](./test/proflycee-test-capytale.png?raw=true "testcap")

## Solides de l'espace

Une macro <code>pavePL[...]</code> pour un pavé droit.

Une macro <code>tetraPL[...]</code> pour un tétraèdre.

![illustr](./test/proflycee-test-pave.png?raw=true "testpave")

## Fractions et ensembles

Une macro <code>convertfraction</code> pour simlifier (dans la mesure du possible) une division.

Une macro <code>ensPL</code> pour écrire un ensemble d'éléments entre accolades.
  
## Suite récurrente et toile

Une commande<code>recurrPL</code> pour tracer (dans la mesure du possible) la "toile" d'une suite récurrente.

![illustr](./test/proflycee-test-recurr.png?raw=true "testrecurr")

## Cercle trigo

Une commande <code>cercletrigoPL</code> pour tracer rapidement un cercle trigo, avec affichage ou non de valeurs/équations.

![illustr](./test/proflycee-test-trigo.png?raw=true "testrigo")
