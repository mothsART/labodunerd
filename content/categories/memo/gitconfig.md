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

        lpush = "!git --no-pager log origin/$(git currentbranch)..HEAD --oneline"
        lpull = "!git --no-pager log HEAD..origin/$(git currentbranch) --oneline"
        whatsnew = "!git diff origin/$(git currentbranch)...HEAD"
        whatscoming = "!git diff HEAD...origin/$(git currentbranch)"

    [pull]
        rebase = true


## Explication

### les alias

**prev**: permet d'aller au commit précédent (attention: vous serez en **detached head**)

**next**: permet d'aller au commit suivant (attention: vous serez en **detached head**)

**last**: permet de se déplacer à la dernière version, soit au tag ayant la valeur la plus grande. (attention: vous serez en **detached head**)

**lpush**: listera les commits qui seront poussés lors du prochain git push origin $(git currentbranch)

**lpull**: listera les commits que l’on s’apprête à merger lors du prochain git pull

**whatsnew**: détaillera sous forme d’un diff ce qui va être poussé au prochain git push origin $(git currentbranch)

**whatscoming**: détaillera sous forme d’un diff ce qui va être mergé au prochain git pull.

### le pull

Petit rappel : le **pull** est en réalité un **fetch** suivi d'un **merge**.
On s'en rend pas forcément compte (surtout quand il n'y a rien à mergé).

Mais, ça c'est le comportement par défault du **pull**.
Il est possible de le forcer à faire un **rebase** (git pull --rebase) et ceci directement dans la config de GIT.

Si ponctuellement, vous désirez faire un merge, ça reste possible :

    #!sh
    git pull --no-rebase
