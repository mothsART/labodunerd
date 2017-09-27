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
Qui plus est, ça me permet de faire du **Rust**, de faire de l'algo sur de l'image matricielle, d'apprendre l'API de GTK... 
Et potentiellement de faire profiter d'autres personnes et, pourquoi pas, de succiter des vocations.

## N'importe quoi, y'a ImageMagick ou Gimp

Ben, justement... c'est tout sauf simple.
L'un nécessite de faire de la ligne de commande et le 2ème est une usine à gaz longue à démarrer, gourmande en ressources et réservé à la retouche photo.

Bref, je veux respecter la philosophie Unixienne : faire une chose et une seul.
Rester KISS.

## Fonctionnalités

* Comparer des images via des métriques
* Comparer les méta-données
* utilisation via GIT : un peu comme https://gist.github.com/StanAngeloff/1716699

## Equivalents

ImageMagick
Beyond
geeqie

## Références

https://askubuntu.com/questions/209517/does-diff-exist-for-images