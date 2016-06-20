Title: Aide mémoire GIT
Category: Aide-memoire
Tags: git, linux
Date: 2016-02-14 00:00
Modified: 2016-02-14 00:00
Slug: aide-memoire-git
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

GIT est un super utilitaire mais son nombre de commandes est juste exponentiel.

## Tags

### ajout
    #!bash
    git tag montag 1b2e1d63ff (numéro du commit)
    git tag montag mon_nom_de_branch
    git tag montag (ajout du tag sur le commit pointé par le **Head**)
    git push --tags (envoi des commits en remote + les tags)


### suppression

    #!bash
    git tag -d mon_tag
    git push origin :refs/tags/mon_tag (supprime en remote)

## Reflog

Reflog permet de lister toutes les actions faites sur un dépôt.
A la différence de **git log**, il va lister également les actions de suppression qui ne sont plus présente sur notre historique GIT.
Cette commande est très utile pour récupérer des commits/tags/branches qui ont été supprimé ou pour revenir sur un historique précédent !


## Cherry-pick + cherry

**git cherry** permet de lister la différence entre 2 branches

Donne la liste des commits de différence entre les 2 branches

    #!bash
    git cherry branch1 branch2

## shortlog

    #!bash
    git shortlog -sne --all
    git shortlog -sne --all | wc -l => liste les autheurs sur l'ensemble des dépôts

## remote

On supprime de notre *repository local* toutes les branches remote qui n'existent plus

    #!bash
    git remote prune origin

On compte toutes les branches **remote mergées**

    #!bash
    git branch -r --merged origin/integration | wc -l

## fetch

On récupère toutes les données du **repository remote**
    #!bash
    git fetch --all

## gc

## fsck

## Sous modules

J'oubli à chaque fois l'ordre pour mettre à jour un sous-module.
Mon exemple pour mon plugin **Ace Editor** :

    #!bash
    git clone --recursive https://github.com/mothsART/pelican-plugins.git
    cd ace_editor
    git checkout master
    git pull
    cd ..
    git add -A
    git c -m "..."
    git push

