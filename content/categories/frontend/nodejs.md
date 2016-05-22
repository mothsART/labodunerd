Title: NodeJS
Category: frontend
Tags: javascript, nodejs
Date: 2016-05-23 23:10
Slug: nodejs
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

C'est bien de redéfinir ce qu'est **NodeJS** car il y a souvent beaucoup de confusion (et d'enthousiasme irrationnel) autours de cette techno.

Historiquement, **Javascript** à pris réellement ses titres de noblesse lorsque Google à lancé son navigateur Chrome.
Pour ce démarquer, ce navigateur disposait d'un moteur indépendant, dopé aux emphétamines (grâce à son **JIT**) implémentant le **Javascript** comme jamais : ce moteur, c'est **V8**.

En rajoutant des API (**CommonJS**) à ce moteur, **NodeJS** est né avec la possibilité d'utiliser des outils en ligne de commande (**CLI**) ainsi que l'accès au disque, tout ça en utilisant un langage basé sur les évènements et par conséquent du code non bloquant (l'asynchrone)!

Le gros buzz autours de **NodeJS** (plus précisément **Meteor**), c'est la possibilité de créer un serveur de toute pièce et par conséquent se passer d'un serveur tel que Apache et d'un langage de serveur tel que Python.

L'idée est attrayante en soit si et seulement si le Javascript n'était pas un langage aussi mauvais...

## Quand utiliser NodeJS

### Pour moi, NodeJS c'est excellent pour :

- les pré/post-processeur tel que postcss
- l'utilisation de transpileur tel que babel.js
- la création de bundles : fichiers concaténer et minifier
- de l'assurance qualité sur des fichiers statiques : css/js

Néanmoins, tous ces points dépendent en grande partie d'une énorme communauté très active. Ces 4 points auraient sans doute été bien plus prolifique si ils avaient été développé dans un vrai langage bas niveau (Rust par exemple)... mais bon, il faut savoir être pragmatique et profiter des atouts de cette techno.

### C'est plus que passable pour :

- du serveur web (comparer **Nodejs** à **Nginx** c'est comme comparer mon neveu a Nadal au tennis... juste pas au même niveau)
- du langage serveur : les **ORMs** et **Frameworks** sont trop jeune et le langage est vraiment, mais vraiment trop permissif!
Ne pas oublier que plus un langage et permissif, et plus le temps de débuggage (surtout après mise en prod !!) est considérable.
Aucun développeur, aussi masochiste soit-t-il ne devrait s'imposer ça.

Un site web ou une appli en prod n'a pas les mêmes contraintes que 

### C'est franchement mauvais pour :

- tout traitement non lié directement au web et principalement quand ça nécessite d'exploiter le **CPU/GPU**, que la **gestion de la mémoire** est critique (JIT + ramasse-miette ne pourra jamais rivaliser avec un langage compilé)
Même si la facilité de rendre asynchrone certaines tâches peut sembler une solution à tous les problèmes d'optimisation, il n'en ai rien.

Exemple expliquant tout le leurre autours de la techno NodeJS:
Si un moteur permet de lancer en simultannée 3 tâches de 10 secondes chacune,on se retrouve avec une durée totale de 10 secondes.
Un deuxième moteur permet de lancer les mêmes tâches mais en 1 secondes chacune.
Que le traitement du second moteur soit synchrone ou asynchrone, il sera de toute façon au moins 3 fois plus rapide que le premier.

J'ai souvent remarqué que certaines solutions de perfs résolus par de l'asynchronisme était en réalité un déni du réel problème.
La solution se trouvait plutôt dans un comportement **lazy**, du **caching**, des soucis d'architecture, d'algorithme ou pire, de requêtage (sql or no)...
Bref, la solution était ailleurs.

C'est pas adapté pour faire du langage serveur. **Meteor** est un projet très intéressant, un proof of concept assez révolutionnaire mais rien, absolument rien de ce qui est fait en **Javascript** côté serveur n'est pas reproductible avec un autre langage... et surtout, pour un coût très différent (un code plus concis, une équipe plus réduite etc).
