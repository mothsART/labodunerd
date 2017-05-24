Title: Mes scripts pour Raspberry
Category: raspberry
Tags: raspberry, script, zsh
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: scripts-raspberry
Authors: Jérémie Ferry
Status: published
Summary:

## Mes Scripts pour Raspberry

Un script qui simplifie l'usage de **dd** avec une belle barre de progression !!

Nécessite **pv** et **dialog** pour fonctionner :

    #!bash
    apt-get install pv, dialog

A mettre dans votre .bashrc ou .zshrc (de votre utilisateur root)

    #!bash
    function copy() {
        # dd with a progress bar
        #pv -n "$0" | dd of="$1" bs=1M conv=notrunc,noerror
        # with a dialog
        (pv -n "$0" | dd of="$1" bs=128M conv=notrunc,noerror) 2>&1 | dialog --gauge "Running dd command (cloning), please wait..." 10 70 0
    }

Et on l'appelle ainsi : 

    #!bash
    copy mon-image-raspian.img /dev/emplacement

Je me suis inspiré de https://www.raspberrypi.org/documentation/installation/installing-images/linux.md