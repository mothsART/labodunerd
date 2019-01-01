Title: Tuto Primtux
Category: misc
Tags: primtux html5 javascript
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: tuto-primtux
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Le dev frontend est devenu une jungle de plus en plus toufu.
HTML5 a introduit beaucoup de nouvelles fonctionnalités mais aussi leurs lots d’inexactitude, d'oublis etc.

N'étant pas foncièrement dev front mais plutôt full, (oui, il parait que ça existe pas) j'ai souhaité faire un mini jeu en HTML5 avec quelques animations.

## Premier constat : Javascript c'est le mal (et Flash le mal absolu)

Avant (ce qui à l'échelle de web représente la préhistoire alors qu'à l'échelle humaine c'était y'a quelques années) on utilisait du javascript pour faire de l'animation.
C'était long, fastidieux et ça plombait souvent (toujours) les perfs.
Maintenant, le support est natif donc les navigateurs savent le gérer, ça ne passe plus par le moteur javascript et ça utilise potentiellement le GPU. (sans parler de thread séparé donc non bloquant)

## Mon animation

Je souhaitais tout simplement créer un stand de tir avec des cibles mouvantes comme on peut en voir dans les foires.
Les cibles suivent donc idéalement un chemin non rectiligne et boucle.

### constat 1 : on utilise SVG ou pas ?

### constat 2 : j'aimerais que ça soit responsive

## Les étapes de mise en place

### 1 cible

### Plusieurs cibles

Maintenant qu'on est arrivé à faire ce que l'on voulait avec une cible, le but est d'avoir plusieurs cibles à la Queuleuleu.

Ben oui, mais si on fait ça, on retarde l'animation des cibles.

L'astuce est donc de mettre des valeurs négatives.

### liens

http://tobiasahlin.com/blog/curved-path-animations-in-css/
https://codepen.io/toptalblog/pen/qXRJeY
