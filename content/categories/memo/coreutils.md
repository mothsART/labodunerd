Title: Coreutils
Category: Aide-memoire
Tags: sh, linux
Date: 2016-05-28 18:30
Slug: coreutils
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

## $PATH

variable linux incontournable donnant la liste des répertoires contenant des programmes executables.

    #!sh
    echo $PATH | tr : \\n

## pk-config

## stat

permet de tester si un fichier existe et donner le 

## sync

Découvert avec une installation de **raspberry pi** : permet de synchroniser les mémoires avec le disque.
Ecrit sur le disque toutes les données dans les tampons en mémoire. Ceci peut inclure les superblocs modifiés, les inœuds modifiés, et les écritures différées.

## strace

permet de tracer les appels systèmes.

argument **e** : permet de filtrer avec un motif

## dd (dcfldd : dd avec une barre de progression)

## df -h

donner la liste des périphériques montés

## diff

diff -s <file1> <file2> : indique si 2 fichiers sont identiques

équivalent à 

## split et cat

découper des fichiers (split) en morceaux de taille définit puis les réassembler.

split -b50m fichier partie > 

## Destruction de données

On force les zéro sur toute la partition :
dd if=/dev/zero of=/dev/hda conv=notrunc

shred

    #!bash
    for n in `seq 7`; do dd if=/dev/urandom of=/dev/sda bs=8b conv=notrunc; done

## hexum

## truncate

réduire la taille d'un fichier à 0
truncate -s 0 /home/skyminds/error.log

## eval

