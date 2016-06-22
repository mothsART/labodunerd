Title: GIT config
Category: Aide-memoire
Tags: git, linux
Date: 2016-02-14 00:00
Modified: 2016-02-14 00:00
Slug: mon-gitconfig
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

L'utilisateur avancé de **GIT** à forcément un gitconfig "couteau suisse" sous la main.
Voici une partie du mien avec les commentaires adéquats.

## config

    #!sh
    [alias]
        ci = commit
        co = checkout
        st = status
        t = tag
        c = commit
        ch = checkout

        br = branch

        push = "push --recurse-submodules=on-demand"

        prev = checkout HEAD^1

        next = "!sh -c 'git log --reverse --pretty=%H master | awk \"/$(git rev-parse HEAD)/{getline;print}\" | xargs git checkout'"

        last = "!sh -c 'git checkout $(git describe --tags $(git rev-list --tags --max-count=1))'";

## Explication

### les alias

prev: permet d'aller au commit précédent (attention: vous serez en **detached head**)

next: permet d'aller au commit suivant (attention: vous serez en **detached head**)

last: permet de se déplacer à la dernière version, soit au tag ayant la valeur la plus grande. (attention: vous serez en **detached head**)

