Title: Pourquoi je boude Node.Js
Category: reflexion
Tags: javascript, web
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: pourquoi-je-boude-nodejs
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

NodeJS est à la mode.
Quand je parle de NodeJS, je parle bien entendu de toute la mouvance autours de Javascript.

Le principe :
    il n'existe pas d'alternative (simple) à Javascript à l'heure actuelle pour faire du web.

Les avantages :
    - la communauté
    - les librairies/frameworks ne cessent de s'étoffer
    - utiliser le même langage côté serveur et client
    - langage asynchrone par nature

Les inconvénients
    - le bazar : plein de libs à l'état alpha : juste inutilisable en production!
    - explosition de l'archive : 38 Ko de React.js + 85 Ko de Jquery + etc.
    - code interprété donc lent (même avec du **JIT**)
    - impératif donc de POO ou de fonctionnel : Ecmascript 6 et 7 améliore sensiblement les choses.
    - notion de typage inexistant (oblige à faire des tests unitaires sur du typage!!!)
    - très peu de tests de sécurité (mémoire, qualité) : **use strict** améliore les choses ainsi que l'utilisation d'outils tel que **JSLint**...
    - l'asynchrone est basé sur les callback : pénalisant sur des projets complexes => ecmascript 7 va améliorer ça en utilisant nativement **async** et **await**.
    - l'utilisation de libs bas niveau (C ou C++)
    - Pour toutes les raisons si dessus, utiliser Javascript pour du serveur est sans doute un mauvais choix.

## Bonne pratique aujourd'hui

**Babel.js** et **Emscripten** semble être les bonnes technos du moment.

## Et demain

Depuis la proposition d'un bytecode commun par Mozilla (asm.js), les choses ont pas mal évolués et (Webassembly)[http://www.developpez.com/actu/97050/Google-Microsoft-et-Mozilla-proposent-une-demonstration-fonctionnelle-de-WebAssembly-le-projet-ambitionne-de-devenir-le-code-binaire-du-web/]
semble LA solution commune.

Une fois que 90% navigateurs sur le marché auront cet API stable de disponible, il sera aisé de se passer complètement de Javascript : envisageable dans 5 à 10 ans selon mon indicateur pifométrique.

La transition se fera avec des outils comme **Emscripten**.

En attendant, il faudra implémenter cet API dans chacun des langages : Un boulot pharaonique en somme qui risque de prendre du temps.

## Conclusion

Les besoins du web ne cesse de s'accroitre. Les usages se diversifies.
Javascript est incontournable et vit son heure de gloire.
Mais tout à une fin et il vaut mieux ammorcer la chute plutôt que de la subir.

Il sera sans doute possible dans moins de 10 ans de faire du web en se passant totalement de Javascript et donc d'utiliser des langages plus modernes, moins permissifs et plus réactifs tel que **Rust**.
