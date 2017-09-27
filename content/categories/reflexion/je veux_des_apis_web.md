Title: Les APIS web oubliés
Category: reflexion
Tags: svg, js, frontend
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: le-format-svg
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Je suis un dev web et je passe trop de temps sur des choses merdiques.
Du frontend franchement basique.

## Une api pour transform()

On peut, en toute logique utiliser depuis un petit moment déjà les propriétés css **transform: scale(5px 8px) translate(2px 200px)**

C'est franchement excellent. Maintenant quand on veut éditer une valeur avec javascript, ça se corse tout d'un coup car il existe strictement rien : faut parser, et éditer avec une merdique concaténation de chaines !!! What !

Bref, quand on connait la nature de javascript (dangereux tant qu'on a pas blindé de 1000 tests unitaires) et qu'on est obligé de faire plein de code boilerplate ...

On se pose vraiment la question : était-il difficile de faire une API pour ça plutôt qu'importer une nième librairie ou faire le job moi-même ?!

## Même constat pour la propriété viewbox en SVG

## passer des couleurs d'un format d'image à l'autre

C'est super, en css, on peut utiliser toute forme de couleur : hexadécimal, rgb, rgba et même hsl et hsla.
C'est cool sauf que quand on fait du dev web, on utilise souvent des librairies différentes non compatibles. Du coup, ben, on a besoin de convertir des couleurs dans des espaces colorimétriques différents.
Et bien sur, faut se faire tout à la main car y'a rien de natif.

Fillez-nous des apis, merde.

## Faire du calc() dans les média queries

On peut désormais utiliser des tailles en pourcentage, en rem, en vw, vh etc.
On peut additionner ces valeurs mais quand on veut faire du responsive... ben on ai baisé car les média queries ne supporte pas **calc()**
Du coup, on est obligé de tricher, d'utiliser du javascript etc.

## SVG

Le SVG, j'aime ça, j'en fais de plus en plus mais plus j'avance et plus je comprend que c'est encore à des années lumières de remplacer flash !
Quand je vois qu'il y a 15 ans, j'étais capable de faire des trucs en flash sur lesquel je galère en SVG à l'heure actuelle alors que j'ai franchement plus de bouteil.
Je me dis qu'il y a comme un soucis.
Et puis, quand CanIUse me dit que le SVG 1.1 est supporté à 100% par tous les navigateurs, j'ai l'impression que c'est valable que sur des cas d'école.
La réalité du terrain est tout autre et faut beaucoup de patience et de malice pour pouvoir avoir un fonctionnement équivalent partout.
Alors ne me parlez pas de SVG dans du HTML ou l'inverse : là on s'aventure dans le nonamesland : on voit très clairement que les moteurs de rendu ont intégré le SVG après coup en cachant la misère.
La complémentarité SVG/HTML n'a jamais été pensé au départ et les bugs irrésolubles sont légion.
(Je porte de gros espoir sur Servo qui ne pourra que s'en sortir mieux en partant d'une feuille blanche)

* **Opération de recadrage** : 

Quand on veut recadrer un document complet : plus de viewbox avec des valeurs négatives par exemples... ben, ça existe pas : faut utiliser **transform** (ou tout recadrer à la main)!

Pour moi, les fonctions **scale** **translate**, c'est pas fait pour ça!

ça entraine de la complexité alors que l'on veut tout simplement remettre à niveau un document au complet.

* **Opérations booléennes natives** :

Ca nécessite des libs externes pour faire le boulôt.
**C'est du foutage de gueule, ça devrait être natif !**
