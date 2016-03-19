Title: Pourquoi passer à Rust ?
Category: pourquoi-passer-a-rust
Tags: rust
Date: 2016-02-26 20:48
Slug: pourquoi-rust
Authors: Jérémie Ferry
Status: draft
Summary:

## Introduction

Depuis plusieurs mois, j'accorde un intérêt croissant pour le jeune language de programmation **Rust**.
Ayant déjà de bons acquis en C/C#/Python/Javascript, on peut naturellement se poser la question de pourquoi s'investir dans un nouveau language.

## Approfondir mes connaissances personnelles

Une raison, non dissimulé, vient du fait que j'exprime le besoin de sortir de mon périmètre de confort : d'apprendre ou ré-apprendre.
Pour celà, j'ai testé pas mal de langages : Ocaml, Haskell, Go langage.
Ni l'un ni l'autre n'a trouvé grâce à mes yeux (chacun pour des raisons différentes).

## Faire du bas niveau

Il y a 2 types de dev: ceux qui font du bas niveau et les autres.
Quant on fait du bas niveau, on s'oblige a comprendre comment fonctionne réellement un ordinateur.

La première catégorie est forcément mieux armé pour faire face à des problématiques complexes : de performance, latence, empreinte mémoire etc.

Bref, les problématiques rencontrés par tous les développeurs travaillant sur des projets sérieux.

Python, Javascript et C# (dans une moindre mesure) ne sont tout simplement pas fait pour ce genre de chose.
* D'une part, la gestion de la mémoire se fait via un ramasse-miettes (garbage collector).
* Ces langages passent par des machines virtuelles qui interpréte (via du bytecode) et convertisse à la volé en code machine.
Il est par conséquent impossible d'avoir du code aussi rapide en interprété quand compilé (par analogie, le chemin le plus court entre 2 points est la ligne droite). 
Même si on peut s'en rapprocher, le soucis de l'empreinte mémoire d'une VM et son temps de lancement reste insoluble.

J'imagine un avenir radieu (quoi, on y est déjà ?) ou l'on lancera en simultannée une appli Java, Python, Nodejs, C# et Perl.
Chacun utilise sa propre VM et prend 50 Mo (et je suis optimiste).
Résulat des courses : on utilise 250 Mo inutillement.
Pour du desktop, ça peut paraitre anodin (quoi que) mais pour du serveur ou de l'embarqué, ça peut devenir vraiment pénalisant.

## Oui, mais C fait du bas niveau

Le C (ou le C++) c'est idéal pour écrire du code bas niveau : pourquoi le remplacer par du Rust ?
Parce que c'est pas safe du tout, que ça n'utilise qu'un paradigme et que c'est pas adapté à du dev concurrent.

## Maitriser de bout en bout

La lubie du développeur est de maitriser son environnement au maximum.
Pour celà, le choix de son hardware et de son OS semble déjà une bonne base.
Open source et libre de préférence.

Ensuite, des problématiques plus pointues viennent se rajouter pour le développeur : 
En l'occurence, toute la stack employé pour aboutir à un résultat : soit les éditeurs et IDE choisit, les logiciels de versions, les hébergements etc.

Rust s'inscrit, pour moi,  dans cette quête.
D'une part, le language n'est pas initié par une grosse firme (Redmond, Google et cie) mais par un organisme à but non lucratif (Mozilla foundation).

## Me lancer dans des nouveaux projets

## Inconvénients

- Ré-apprendre depuis le début entraine des frustrations (je ne pensais jamais autant) :
Prendre 1 heure pour faire quelque chose qui nous prend 5 minutes dans un autre langage est forcément ingrat mais ça fait parti du jeu...

- Rust est un langage neuf ce qui sous-entend peu de doc (surtout dans la langue de molière), de topics sur des forums et des libs innexistantes, incomplètes etc.
