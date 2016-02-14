Title: Aide mémoire GIT
Category: Aide-memoire
Tags: git, linux
Date: 2016-02-14 00:00
Modified: 2016-02-14 00:00
Slug: aide-memoire-git
Authors: Jérémie Ferry
Summary:

# Aide-Memoire GIT

## Intro

GIT est un super utilitaire mais son nombre de commandes est juste exponentiel.

## Tags

### ajout
    #!bash
    git tag montag 1b2e1d63ff
    git tag montag mon_nom_de_branch
    git tag montag (ajout du tag sur le commit pointé par le head)
    git push --tags (envoi des commits en remote + les tags)


### suppresion

    #!bash
    git tag -d mon_tag
    git push origin :refs/tags/mon_tag (supprime en remote)
