Title: Can I Diff
Category: 
Tags: 
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Un développeur passe son temps à utiliser des différentiels pour déterminer rapidement ce qui a changé dans un ou plusieurs fichiers.

Le plus commun est bien entendu la commande diff, particulièrement décocratisé à partir de **git diff**.

## diff et cmd

leur pendant graphique : kdiff, meld

=> pratique pour comparer des dossiers complets

## Certains fichiers textes ne sont pas adaptés

Quand on découvre diff, on peut croire à tord qu'il va couvrir tous les besoins.
Cependant, il est mal approprié aux fichiers xml et html :
Les ajouts de noeuds parents peuvent être particulièrement pénalisant.

il existe des outils dédiés :

https://github.com/GuillaumeGomez/html-diff-rs

## Les fichiers binaires

Quand il n'y a pas de solutions dédiés :

https://superuser.com/questions/125376/how-do-i-compare-binary-files-in-linux

## Images

Avec Image Magick :

    #!bash
    sudo apt-get install imagemagick imagemagick-doc
    compare -compose src img_origine.png img_modifie.png img_difference.png

