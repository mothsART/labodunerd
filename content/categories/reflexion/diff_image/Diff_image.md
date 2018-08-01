Title: Diff-image
Category: reflexion
Tags: rust
Date: 2017-07-27 00:00
Modified: 2017-07-27 00:00
Slug: diff-image
Authors: Jérémie Ferry
Status: published
Summary:

## Comparer 2 images

Je démarre un soft de comparaison d'images.

En effet, je trouve qu'un outil "simple" de ce genre n'existe tout bonnement pas.

Qui plus est, ça me permet de faire du **Rust**, de l'algo sur de l'image matricielle, d'apprendre l'API de GTK... 

Et potentiellement de faire profiter d'autres personnes et, pourquoi pas, de succiter des vocations.

## N'importe quoi, y'a ImageMagick ou Gimp

Ben, justement... c'est tout sauf simple.

L'un nécessite de faire de la ligne de commande et le 2ème est une usine à gaz longue à démarrer, 
gourmande en ressources et réservé à la retouche photo.

Bref, je veux respecter la philosophie Unixienne : faire une chose et une seul et rester KISS.

## Fonctionnalités

* Récupérer 2 images et visualiser les changements

## Fonctionnalités à venir

* Comparer des images via des métriques
* Comparer les méta-données
* utilisation via GIT : un peu comme https://gist.github.com/StanAngeloff/1716699

## A quoi ça ressemble ?

![Comparer des images](static/images/whatschanging/spot_the_diff.png)

## Comment on installe

Si vous êtes sur une distrib Ubuntu, j'ai créé un PPA :

    #!sh
    sudo add-apt-repository ppa:jerem-ferry/rust
    sudo apt-get update
    sudo apt-get install whatschanging

## Comment on compile

1. On installe Rust et Cargo (si ce n'est pas déjà fait)

        #!bash
        curl -f -L https://static.rust-lang.org/rustup.sh -O
        sh rustup.sh -y --channel=nightly

2. On Récupère les sources :

        #!bash
        git clone https://github.com/mothsART/whatschanging.git && cd whatschanging

3. On Lance (la première fois, c'est lent car ça récupère les dépendances et ça compile)

        #!bash
        cargo run

On peut désormais tester l'exemple du dessus (les 2 images sont dans les sources) ou comparer des images de son choix.

## Le code source

[https://github.com/mothsART/whatschanging](https://github.com/mothsART/whatschanging)

## Equivalents

* ImageMagick
* Beyond
* geeqie
* idiff
* https://www.diffchecker.com/image-diff
* https://github.com/kornelski/dssim

## Références

[https://askubuntu.com/questions/209517/does-diff-exist-for-images](https://askubuntu.com/questions/209517/does-diff-exist-for-images)
