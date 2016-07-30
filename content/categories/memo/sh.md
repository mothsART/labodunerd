Title: Aide mémoire sh
Category: Aide-memoire
Tags: sh, linux
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: aide-memoire-sh
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

    #!bash
    find . | grep actual

## Sed

Remplacer une occurence par une autre sur un ensemble de fichiers

    #!bash
    sed -i s/leMauvaisTexte/leBonTexte/g *