Title: Bench de bases de données
Category: 
Tags: sql, db, bench, benchmark
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: db-bench
Authors: Jérémie Ferry
Status: published
Summary:

# Un Bench de Base de données

## Intro

Le stockage de données est omniprésent.
Pour celà, le développeur a à sa disposition une gamme incroyable de bases de données.

La diversé est tel que le choix peut vite devenir cornélien.

- les raisons sont rarement **que** technique : licence, accord commerciaux, habitude et compétence de l'équipe etc.
- bon nombre de projets gagneraient à utiliser plusieurs type de bases.

### Constat 1

La contrainte de vitesse d'exécution est rarement contournable.
Un jour ou l'autre, un dev, une équipe, une société y sera confronté : au pire des moments et de la pire des manière.

### Constat 2

Le cadre est souvent mal définit : à partir de quand un site web/une appli ne rempli pas/plus ses objectifs en terme de réactivité ?

### Constat 3

La résolution est souvent hasardeuse, lié aux préjugés, croyances, aux expériences précédentes ou que sais-je encore.
La réalité est souvent bien différente et plus complexe qu'elle n'y parait et le résultat peu concluent, inachevé etc.

L'objectif est ici de remettre tout à plat et de gommer les préjugés.
La démarche d'un bench est avant tout de répondre avec objectivité à une contraine sans opinion.

N'étant pas expérimenté dans l'exercice, je sais d'avance que je pars sur un terrain vierge avec une certaine naïveté.
Mais ne dit-on pas qu'**un idiot qui marche va plus loin qu'un intelligent assis**?

## Type de bases

Si on parcours le net, le résumé serait de dire qu'il existe 2 types de SGBD : les full SQL et les autres.
En réalité, les bases SQL ont tellement monopolisé le marché qu'on aurait tendance à mettre toutes les autres architectures dans le grand panier **ésotérique** du NoSQL.

Sauf qu'en étrapolent, un simple fichier .csv pourrait être du NoSQL.

il existe en réalité 4 grandes familles de NoSQL :

* base orientée **document** : mongoDb, couchDb, Riack
* base orientée **clé/valeur** : Redis
* base orientée **graph** : Neo4JS, OrientDb
* orienté **object** :ZoDb

## Raison du Bench => le caching

Soyons clair, cet article ne cherche pas à promouvoir quoi que ce soit.
Le comparatif ne se limitera qu'à des modèles de cache.
Le principe d'un cache est d'être **principalement** rapide d'accès en lecture.
J'occulte donc volontairement les benchs sur autre chose que l'accès à des données précédement stocké.

Un bench, pour qu'il soit un minimum pertinent, doit se faire au plus proche des conditions réels.
Ce Bench n'est donc qu'un point d'entrée, une démarche à suivre et se doit d'être étendu sur des recherches correspondant à des scénarios en situation réels :

* scénarios prévisionnels empiriques et exhaustifs dans le cas d'une pré-prod.
* scénarios exhaustifs construit à partir des logs sur un échelle de temps suffisament significative si possible majoré d'une marge : prévision d'une augmentation de l'activité, de changements d'usages etc.

Vos contraintes techniques, vous étant propre, elles peuvent être lié à plusieurs facteurs :

* besoin de type ACID ou non ?
* base de type client-serveur ou embarqué ?
* base réparti sur plusieurs serveurs ou non ?
* taille de base définit ou perspective de scalabilité ?
* transactions possibles ?
* procédures stockés ?
* etc.

## Langage et architecture

J'ai hésité sur le langage utilisé : comment donner une certaine généricité à ce projet alors que le langage de programmation a tendance à cloisonner les lecteurs, éventuels contributeurs etc.

Mais vu qu'il en fallait un, je suis parti en définitive sur Python (longue hésitation avec le C# et Rust).

Pourquoi :

* langage simple, proche du pseudo-code : juste idéal pour du prototypage
* mature (plus de 20 ans d'âge, ça commence à être un bon crue) et disposant de connecteurs tout aussi matures pour une variété incroyable de base de données
* haut-niveau pleinement orienté Objet
* interprété et disponible sur une variété d'archi
* ma propre expérience : c'est mon langage de prédilection (très peu d'aller/retour sur le net) quasi fluent.
* ipython, pardon **Jupyter** (je m'y ferais jamais) en mode **notebook** couplé aux libs **matplotlib**, **numpy**, **scipy** et **pylab** ... c'est juste une tuerie pour créer des graphiques complexes facilement et rapidement!
Aucun langage ne propose un combo de se genre à ma connaissance mais je serais ravi de me tromper.

Pour la version, je suis parti sur python 3.4+. (pas envie d'assurer sur ce type de projet de la rétro-compatibilité avec Python 2)

Pour l'architecture, je me suis basé sur le design pattern Adapter. (même si ça ressemble plutôt à un Proxy jusqu'à présent)

Les schéma parle mieux que les mots.

Je distingue le source de mon executable.
En effet, pour tester ce banc, j'utilise Docker : Ca permet de cloisonner l'environnement et surtout d'assurer des dépendances identiques pour chacun des utilisateurs.

Il serait sans doute judicieux d'utiliser une vrai VM afin d'ajouter des contraintes physiques bien définit : taille de la RAM, dimensionnement des CPUs etc. mais mon choix n'est pas encore arrêté (Qemu, VirtualBox, autre?) et l'int"rêt me semble minime.
(je suis prêt à changer d'avis : argumentaire et si possible chiffres à l'appui)

Poour l'utiliser, il vous faudra donc le DockerFile =>

## Et après ?

Ce n'est qu'un début... un amuse bouche.
Rome ne c'est pas contruit en 1 jour donc je me laisse l'experimentation pour perfectionner ce banc d'essai!
Le projet est sur Github et ne demande que des contributions.

Rajouter des types de base est l'objectif premier.
Le reste viendra ensuite.

Si vous désirez participer, n'ayez aucune hésitation!
La participation peut être de différents ordre.
Néanmoins, relancer d'un autre poste le banc de test et me témoigner des éventuels différences serait sans doute le point le plus
entousiasmant!

Mes intentions sont d'apprendre, perfectionner, consolider ou confronter mes acquis et je tolererais sans sourciller les critiques "constructives".

L'intérêt étant justement la remise en question, l'apprentissage et l'ouverture d'esprit.