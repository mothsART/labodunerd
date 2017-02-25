Title: Editeur WYSIWYG de SVG interactifs
Category: frontend
Tags: javascript, svg, linux, primtux, deb
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: editeur-svg-interactif
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

L'objectif est simple : éditer un fichier SVG statique afin de le présenter comme un contenu interactif. 
Permettre l'ajout des zones cliquables pouvant être zoomés et enrichies d'une explication

Les fichiers générés (page Html contenant le svg) pouvant servir à divers usages :

- contenus éducatifs
- support de présentation
- etc.

![tmuxp load](static/images/editeur_svg/editeur_svg_exemple1.png)

## Objectifs techniques

1. créer des illustrations interactives avec toujours le même gabarit : une légende contenant des indices titrés et un descriptif pour une zone de l'illustration.
Un exemple est disponible : [https://mothsart.github.io/labo/frontend/edit_interactive_svg/examples/campement.min.svg](https://mothsart.github.io/labo/frontend/edit_interactive_svg/examples/campement.min.svg)

2. permettre des zooms sur les zones décrites

3. avoir un contenu responsive (vu que le contenu est pleinement vectoriel, pourquoi s'en priver)

4. être et rester simple d'utilisation (**[KISS](https://fr.wikipedia.org/wiki/Principe_KISS)** et **[philosophie Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix)**) et productif pour enrichir une illustration à vocation pédagogique.

5. rester simple à développer et maintenir

6. utilisation hors ligne et intégré dans une distribution Linux via un paquet .deb

## Version de démo en ligne

Il est possible d'utiliser directement la dernière version sur :
[https://mothsart.github.io/labo/frontend/edit_interactive_svg/](https://mothsart.github.io/labo/frontend/edit_interactive_svg/)

Des illustrations effectués intégralement à partir de cet éditeur seront rapidement mise en ligne.

## Explication d'utilisation

1. On glisse et on dépose (ou on choisi via son explorateur de fichiers) son fichier svg statique. (si possible sans animation et javascript)
On arrive sur une  interface nous permettant d'éditer ce fichier.

2. On ajoute des indices dans la légende. Ces derniers s'affichent également sur notre illustration si l'on clique sur les icones d'affichages (des yeux).

3. On les positionnes au gré de nos envies (en restant appuyé sur le clic gauche) sur l'indice à déplacer.

4. Un menu déroulant sur l'indice est disponible afin de l'éditer :
Il est possible de changer la couleur, de zoomer mais également d'ajouter/editer le titre et la description de notre indice.

5. L'accès au **mode show** nous permet de visualiser le rendu final. (avec les animations sur les indices si le zoom a été paramètré).

6. Il est possible de changer l'odre de nos indices (en les sélectionnant et les glissants) et d'en supprimer ainsi que de les afficher ou non. (pratique si l'on ne veut se concentrer que sur un éventail précis)

6. Le bouton save permet de convertir notre travail en un fichier html. (équivalent au **mode rendu**)

7. Si l'on veut repartir d'une feuille blanche, il suffit de cliquer sur **Delete**.

## Utilisation dans une distribution

Il est possible d'installer un ppa afin de profiter de l'éditeur dans Ubuntu :

[https://launchpad.net/~jerem-ferry/+archive/ubuntu/app-illustration](https://launchpad.net/~jerem-ferry/+archive/ubuntu/app-illustration)

## Participer au logiciel

Les sources du projet sont disponibles sur Github : [https://github.com/mothsART/editInteractiveSVG](https://github.com/mothsART/editInteractiveSVG)

Il est possible de me rapporter des bugs directement via les issues du dépôt mais également sur le forum de PrimTux :
[http://forum.primtux.fr/viewtopic.php?pid=8870](http://forum.primtux.fr/viewtopic.php?pid=8870)
