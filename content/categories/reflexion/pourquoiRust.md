Title: Pourquoi Rust
Category: reflexion
Tags: rust, python, Java, Javascript, C, C++, C#
Date: 2016-03-20 10:00
Modified: 2016-03-20 10:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Depuis maintenant 1 an, je m'intéresse de près au langage **Rust**.
Qu'est ce qui peut motiver le choix d'un nouveau langage alors qu'il en existe déjà un nombre incalculable ?

Ayant déjà de bons acquis en C/C#/Python/Javascript, on peut naturellement se poser la question de pourquoi s'investir dans un nouveau language.

## Approfondir mes connaissances personnelles

Sur tous les langages cité, j'ai une nette préférence pour le **Python** : simple, explicite, haut niveau.
C'est un language incroyable pour du script et du prototypage.

**C#** est aussi un bon cru, même si, il faut l'avouer, c'est souvent l'IDE **Visual Studio** qui lui donne autant de pouvoir.

Une raison, non dissimulé, vient du fait que j'exprime le besoin de sortir de mon périmètre de confort : d'apprendre ou ré-apprendre.
Pour celà, j'ai testé pas mal de langages : **Ocaml**, **Haskell**, **Go langage**.
Ni l'un ni l'autre n'a trouvé grâce à mes yeux (chacun pour des raisons différentes).

## Faire du bas niveau

Il y a 2 types de dev: ceux qui font du bas niveau et les autres.
Quant on fait du bas niveau, on s'oblige a comprendre comment fonctionne réellement un ordinateur.

La première catégorie est forcément mieux armé pour faire face à des problématiques complexes : de performance, latence, empreinte mémoire, sécurité etc.

Bref, les problématiques rencontrés par tous les développeurs travaillant sur des projets sérieux.

**Python**, **Javascript** et **C#** (dans une moindre mesure) ne sont tout simplement pas fait pour ce genre de chose.
* D'une part, la gestion de la mémoire se fait via un ramasse-miettes (garbage collector).
* Ces langages passent par des machines virtuelles qui interpréte (via du bytecode) et convertisse à la volé en code machine.
Il est par conséquent impossible d'avoir du code aussi rapide en interprété quand compilé (par analogie, le chemin le plus court entre 2 points est la ligne droite). 
Même si on peut s'en rapprocher, le soucis de l'empreinte mémoire d'une VM et son temps de lancement reste insoluble.

J'imagine un avenir radieu (quoi, on y est déjà ?) ou l'on lancera en simultannée une appli **Java**, **Python**, **Nodejs**, **C#**, **Ruby** et **Perl**.
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

**Rust** s'inscrit, pour moi,  dans cette quête.
D'une part, le language n'est pas initié par une grosse firme (Redmond, Google et cie) mais par un organisme à but non lucratif (**Mozilla foundation**).

## Me lancer dans des nouveaux projets

## Inconvénients

- Ré-apprendre depuis le début entraine des frustrations (je ne pensais jamais autant) :
Prendre 1 heure pour faire quelque chose qui nous prend 5 minutes dans un autre langage est forcément ingrat mais ça fait parti du jeu...

- **Rust** est un langage neuf ce qui sous-entend peu de doc (surtout dans la langue de molière), de topics sur des forums et des libs innexistantes, incomplètes etc.

## Les gros avantages

- différenciation entre *espace de nommage* et appel d'un attribut (propriété et méthodes).
C'est un peu déroutant quand on vient de **Python** et **C#** qui utilise que le **.** point délimiter les 2 aspects.
Problème => des confusions et des conflits possibles entre un nom et une propriété! En un mot : inadmissible !
**Rust** a choisi de distinguer les 2 et c'est tout bonnement pythonnesque : explicite is better than implicite => **::** délimiter les espaces de nommage et **.** pour appeler un attribut.

- variable immuable par défaut : parce qu'au final, il y a pas besoin d'avoir beaucoup de variables qui sont réécrites et que si elles le sont, c'est elles qui sont la cause d'effets de bord.
Réduire leur nombre, c'est assuré ses arrières et identifié la variable problématique plus rapidement.

- détection des **dead code** dès la compilation

- spécification explicite de la durée de vie d'une variable : ça fait parti des trucs les plus dur à assimilé mais après le mur passé, on produit vraiment du soft de qualité : la mémoire est cloisonné et par conséquent n'est pas gaché.

- Les objets **invalides** (vide) ne sont pas acceptés (ou difficilement contournables) : http://blog.guillaume-gomez.fr/Rust/1/10
Franchement, vu le nombre de bugs rencontrés en C# de ce genre (et la rigueur nécessaire pour les éviter au maximum), ce choix est pour moi du pain béni.

## Conclusion

Rust m'a supris : j'ai mis du temps avant d'avoir des bugs d'exécution vraiment pénalisant.
En définitive, rust vous invite à réduire la partie **dynamique** de votre programme et par conséquent gère un grand nombre des soucis directement à la compilation.

Peut importe le language utilisé, on ne peut garantir un programme comme stable! (cf: la notion de bug)

zero-cost abstractions
move semantics
guaranteed memory safety
threads without data races
trait-based generics
pattern matching
type inference
minimal runtime
efficient C bindings