Title: Réflexion autours des DVCS
Category: réflexion
Tags: git, darcs, hg, mercurial
Date: 2016-02-26 20:48
Slug: reflexion-dvcs
Authors: Jérémie Ferry
Status: published
Summary:

## Introduction

GIT a semble-t-il gagner dans la guerre des **Logiciel de gestion de versions** (**DVCS**)

Pourtant, son remplaçant est peut-être à la porte.

Je vais lister ici les points positifs et négatifs de GIT.

## Points positifs

- Popularité : Github et quelques autres forges (**Bitbucket**, **Gitlab**) ainsi que l'utilisation par de gros projets ont assis sa domination.
- Documentation : la doc est clair est exhaustive et le net permet de trouver une réponse à quasiment toutes les questions s'y référent
- Instantanéité sur de très gros projet : GIT fonctionne sous forme de snapshot et ressemble, à s'y méprendre à un Système de fichier.
Ce fonctionnement lui garanti une réactivité innégalable (qui a évincé Bazaar et Mercurial)
- la gestion des branches : le parti pris de GIT est d'avoir des commits, totalement indépendant des uns des autres dont le seul lien sont des tags : et oui, une branche sous GIT est en réalité un ensemble de commits ayant le même tag.
Du coup, ça donne une vrai souplesse d'utilisation.
- possibilité d'utiliser une vrai API via **libgit2**
- Fork et contribution à un projet facilité avec **Gihub**
- les hooks : des triggers à chaque
- la config : l'historique et la popularité de GIT lui on donné la possibilité d'une configuration très abouti
- interfaces graphiques : un large choix : **gitk**, **GIT Extensions** etc.

## Points négatifs

- pas de suivi de bugs ni de wiki (voir **fossil**) mais pourrait être facilement possible en normalisant des sous-modules.
- ne fonctionne pas selon la **théorie des patchs** tel que le fait **Darcs** ou **[PIJUL](http://pijul.org)**
- permettre des hooks à partir de langages de haut niveau est souvent délicat et nécessite de passer un fichier shell en amont
