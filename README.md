# ProfLycee
Package, sans prétention, pour quelques commandes LaTeX utiles au lycée !

Pour le moment :

- deux macros pour créer, dans un environnement TikZ, des courbes d'interpolations et des tangentes ;
- deux macros pour configurer un environnement de Calcul Formel et pour créer les lignes ;
- un environnement pour présenter du code python (via pythontex) ;
- un environnement pour exécuter du code python et présenter le résultat dans une <i>console</i> ;
- des environnements pour présenter un "émuler" un terminal WIN/UNiX/OSX ;
- une macro pour simuler un cartouche de type "capytale".
- deux macros pour créer, dans un environnement TikZ, un pavé droit ou un tétraèdre.

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

![illustr](./test/proflycee-test-capytala.png?raw=true "testcap")

## Solides de l'espace

Une macro <code>pavePL[...]</code> pour un pavé droit.

Une macro <code>tetraPL[...]</code> pour un tétraèdre.

![illustr](./test/proflycee-test-pave.png?raw=true "testpave")
