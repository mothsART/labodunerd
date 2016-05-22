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

* Javascript : utiliser le mode strict => https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Strict_mode dans des fonctions

Résoud pas mal de soucis de navigateurs : variables non déclarés et autre

* Javascript utilise plusieurs types : undefined, null, undeclared, bool

Le mieux est de faire un test sans égalité => if (maVar) ou if(!var)

* <a href="..." onclick="monappel();return false;"></a>

ou <a href="..." onclick="monappel();"></a>

function monappel() {
    ...;
    return false;
}