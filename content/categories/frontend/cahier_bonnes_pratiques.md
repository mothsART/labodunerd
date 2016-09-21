Title: Cahier de bonnes pratiques Javascript
Category: frontend
Tags: javascript
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: bonnes-pratiques-js
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Ce cahier est dédié à de l'usage de javascript dit **classique**  ce qui sous-entend, pas de frameworks révolutionnaires style **Angular**, **React** et autre.
Pas d'utilisation de transpiler tel que Typescript, CofeeScript ou même BabelJS.

Du javascript en mode vanilla avec potentiellement un peu de Jquery.

## Mode strict

* Javascript : utiliser le mode strict => https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Strict_mode dans des fonctions

Résoud pas mal de soucis de navigateurs : variables non déclarés et autre

## Les différents types de Javascript

Javascript utilise plusieurs types : undefined, null, undeclared, bool.

Si l'on ne connait pas le type par avance et qu'on veut un test d'existance, le mieux est de faire :

**if (maVar)** ou **if(!var)**

## Les appels d'évenements sur les éléments HTML (ou unobstrusive)

Même si les outils de développement sont de plus en plus efficace, ne pas savoir d'ou provient un action peut devenir agacent.
De plus, avec le tout mobile, l'utilisation ingénieuses des ressources est primordiale.
Un évènement devrait être dans 99% du temps sur l'élément en lui evitant les observeurs gourmand.


### Un lien avec un évènement onclick doit utiliser un return false

* <a href="..." onclick="monappel();return false;"></a>

ou <a href="..." onclick="monappel();"></a>

function monappel() {
    ...;
    return false;
}