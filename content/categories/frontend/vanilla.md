Title: Vanilla-a-a-a-a
Category: frontend
Tags: javascript, jquery, xpath, benchmark
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: vanilla-a-a-a-a
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Dans mon existence de développeur, j'ai appris à ne pas me fier à des *on-dit*, les tendances (oui, les modes chez les web-dev, ça court le net) et toute forme d'approximation.
Si on veut être sur de quelques choses, il faut le vérifier.

Depuis plusieurs années, les modes se sont succédés dans le dev web frontend :
On est passé de Jquery à Angular puis à React. (sans couvrir toutes les autres technos)

Depuis toutes ces années, le seul qui n'a pas vraiment bougé reste Jquery quoi qu'on en pense ou qu'on en dise, il reste une des lib les plus utilisés.

Une mouvance encore jeune est de **remplacer Jquery par Vanilla** : en somme, javascript est désormais assez mure pour qu'il n'ai plus besoin d'utiliser une couche supplémentaire!

## Quels avantages

1. La rapidité d'exécution : un code natif est forcément plus rapide
2. la gestion d'une dépendance : les migrations d'une version de jquery à une autre a forcément un coût donc se passer de jquery c'est forcément éviter ce désagrément. (ceux qui ont fait ça sur un gros projet, doive se souvenir de la souffrance)

## Objectivité et Pragmatisme

Même si les défenseur de Vanilla n'ont pas forcément tord, son adoption n'est pas la même sur un nouveau projet que sur la maintenance d'un ancien.
De plus, cette migration se fera surtout pour de l'**IE >= 11**.
Enfin, beaucoup de librairies dépendent de Jquery et il n'est pas forcément simple de s'en passer.

## Bench

J'ai décidé, à mon niveau, de passer progressivement les parties les plus sensibles de mes applicatifs.

J'ai essayé d'identifier quels étaient les morceaux de code jquery que j'utilisais le plus et de comparer ces derniers avec du code natif sous 2 formes : vanilla et xpath (quand ça s'y prête).

Du coup, le résultat du bench me permet de décider ou non si le basculement est nécessaire ou supperflue.

Je vous laisse en juger : [Bench de comparaison de Jquery/VanillaJS/Xpath (en natif)](/labo/frontend/vanilla)

N'ayant pas inventé la poudre, il existe souvent un équivalent à mon code sous [jsperf](http://jsperf.com)

Néanmoins, mon bench me permet de faire **mes tests** rapidement... 
Quand j'ai des sources d'inspirations dans un test : je le signale en référence.

## Mes conclusions

- Tous les **sélecteurs jquery de premier niveau** : recherche d'id , de tag name ou de classes devrait automatiquement être converti en code natif : on divise le temps par 5 minimum pour un code à peine plus long.

- Les **boucles sur sélecteur Jquery ($.each) sont une hérésie!** Elles devraient disparaitres de cette librairie a tout jamais!
Les remplacer par des boucles natives est un moindre mal.(grosso modo : 1 rapport de 10)
En revanche, si vous êtes dans le cas d'un refactoring ou de la création de code, formater votre esprit pour ne pas utiliser de boucle sur sélecteur : il y a **toujours** un moyen de les contourner et ça vous évitera des bugs complexes à analyser, reproduire et corriger quand votre bout de code scalera de telle façon que le ralentissement bloquera votre site ou votre applicatif.
(et ça c'est dans le meilleurs des cas : quand ça freeze uniquement sur certains mobiles)

- les **sélecteurs jquery complexes** peuvent être remplacés par des **sélecteurs xpath**. Néanmoins, qui dit sélecteur complexes dit à 99% soucis d'architure.
Avant de se casser la tête avec un sélecteur compliqué, pensez d'abord à simplifier l'accès à un élément en lui rajoutant une classe ou un id !

## A venir

J'aimerais pouvoir identifier facilement les morceaux de code Jquery à modifier.
Pour cela, rien de mieux qu'une **expression régulière (regex)** disponible dans chacune des lignes : il vous suffit de l'appliquer à la source de votre projet via un utilitaire tel que **[ripgrep](https://github.com/BurntSushi/ripgrep)** et identifier facilement les fichiers et lignes nécessitant un update ! 
