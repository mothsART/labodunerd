Title: Bench Linux
Category: Aide-memoire
Tags: linux
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: bench-linux
Authors: Jérémie Ferry
Status: published
Summary:

## Vérifier si l'accélération graphique est actif

glxinfo | grep "direct rendering"

## lancement du benchmark de Mesa (implémentation libre d'opengl)

Afin de ne pas être limité par la fréquence de rafraichissement (en général 60) Il peut être préférable d'entrer la commande suivante. N'oubliez pas d'exécuter dans la fenêtre du terminal ctrl+c pour shunter glxgears.

vblank_mode=0 glxgears

## Bench CPU

 7z b

