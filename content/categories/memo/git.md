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

## Clone 

Avec des sous-modules

    #!bash
    git clone --recursive depot

## Recherche d'un bug

    #!bash
    git bisect

## Ajout/Reset Partiel

    #!bash
    git add -p/git reset -p

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
    git push origin :refs/tags/mon_tag #supprime en remote

## Branches

### ajout

    #!bash
    git checkout -b ma_branche

### suppression

    #!bash
    git branch -D ma_branche
    git push origin --delete ma_branche #supprime en remote (GIT >= 1.7)
    git push origin :ma_branche #supprime en remote (GIT < 1.7)

## Reflog

Reflog permet de lister toutes les actions faites sur un dépôt.
A la différence de **git log**, il va lister également les actions de suppression qui ne sont plus présente sur notre historique GIT.
Cette commande est très utile pour récupérer des commits/tags/branches qui ont été supprimé ou pour revenir sur un historique précédent !


## Cherry-pick + cherry

**git cherry** permet de lister la différence entre 2 branches

Donne la liste des commits de différence entre les 2 branches

    #!bash
    git cherry branch1 branch2

## log

    #!bash
    git log -n 10 # n'afficher que les 10 derniers commits

## shortlog

    #!bash
    git shortlog -sne --all
    git shortlog -sne --all | wc -l => liste les autheurs sur l'ensemble des dépôts

## remote

On supprime de notre **repository local** toutes les branches remote qui n'existent plus

    #!bash
    git remote prune origin

On compte toutes les branches **remote mergées**

    #!bash
    git branch -r --merged origin/integration | wc -l

## fetch

On récupère toutes les données du **repository remote**

    #!bash
    git fetch --all

## pull = fetch + merge

perso, j'ai définit mon pull pour faire un **pull --rebase** dans mon **.gitrc**

## rebase

soit

    #!bash
    git checkout master
    git rebase serveur

soit

    #!bash
    git rebase master serveur

git rebase -i : permet de changer l'entête d'un commit => squasher ses commits

git rebase -p / git rebase --preserve-merges => permet de garder l'historique des fusions...

garder un fichier local -> git checkout --ours /path/to/file (si l'on veut tous les fichiers :  git checkout --ours *)
garder un fichier distant -> git checkout --theirs /path/to/file

puis git add /path/to/file

## Ignore

exclusion globale (dans ~/.gitconfig):
[core]
    excludesfile = ~/.gitignore

exclusion locale : .git/info/exclude

Ignorer un fichier déjà tracké :
git update-index --assume-unchanged <file>
(en savoir + : https://www.kernel.org/pub/software/scm/git/docs/git-update-index.html)
(opération inverse : git update-index --no-assume-unchanged <file>)

    #!bash
    git update-index --no-assume-unchanged 

## cherry

Considérons 2 branches => **master** et **topic**

    #!bash
    git cherry -v topic | grep -e "^+" | grep -v "\[nc\]" | tee /dev/tty | wc -l

donne la liste des commits présent dans la **topic** et non dans la **master**

et son inverse :

    #!bash
    git cherry -v master | grep -e "^+" | grep -v "\[nc\]" | tee /dev/tty | wc -l

donne la liste des commits présent dans la **master** et non dans la **topic**

## Diff

    #!bash
    git diff -b (git diff --ignore-space-change)
    git diff -w (git diff --ignore-all-space)
    git diff --color-words=.


juste les fichiers : git diff --stat
git diff --name-status

## Amend

    #!bash
    git commit --amend --no-edit

Rajoute au dernier commit tous les fichiers du staging + tous les fichiers non traqués et renome l'intitulé du commit

    #!bash
    git commit -a -u --amend -m "new message"

## Stash

    #!bash
    git stash --include-untracked === git stash save -u

réapplique le stash avec l'index originel :

    #!bash
    git stash apply --index

Explication : http://www.git-attitude.fr/2014/09/15/30-options-git-qui-gagnent-a-etre-connues/#stasher-plus efficacement avec save et -u

    #!bash
    git stash save -u 'Nom du stash'
    git stash pop --index

## Push

Pousser une branche qui vient d'être créé :

    #!bash
    git push -u origin NomDeLaNouvelleBranche

Suppression d'un commit en remote : http://stackoverflow.com/questions/1338728/delete-commits-from-a-branch-in-git

En local

    #!bash
    git reset --hard HEAD~1

En remote

    #!bash
    git push origin HEAD --force

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

## Suppression Branche remote

git push origin --delete <branchName> (exemple: git push origin --delete 14_79_000_0)
(ancienne méthode (git < 1.7): git push origin :<branchName>)nch 

## Suppression Commit en remote

supprime le dernier commit : git push -f origin HEAD^:ma_Branch_en_remote

## Suppression répertoire de travail

    #!bash
    git reset HEAD === git reset HEAD^0

## Suppression de commit

    #!bash
    git reset HEAD^ === git reset HEAD^1

## Suppression d'un fichier sur un commit

    #!bash
    git reset HEAD^ -- $file
    git commit --amend

## Rebase interactif

https://blog.guillaume-gomez.fr/Git-tips

## Equivalences

    #!bash
    git checkout -b ticket-12 === git branch ticket-12 + git checkout ticket-12

git checkout --track origin/correctionserveur === git checkout -b correctionserveur origin/correctionserveur (--track évite donc les erreurs dans le nom des branches locales)

## Compter le nombre de commits (sur toutes les branches)

http://stackoverflow.com/questions/1265040/how-to-count-total-lines-changed-by-a-specific-author-in-a-git-repository

    #!bash
    git shortlog -sne --all

    #############
    # http://tilap.net/git-trouver-lister-les-fichiers-modifies-par-utilisateur/
    listFilesByAuthor = log --pretty="%H" --author="Jeremie" | while read commit_hash; do git show --oneline --name-only $commit_hash | tail -n+2; done | sort | uniq
    #############
    # must install Ruby
    #moststats = "ls-files -z | xargs -0n1 git blame -w | ruby -n -e '$_ =~ /^.*\((.*?)\s[\d]{4}/; puts $1.strip' | sort -f | uniq -c | sort -n"
    #############
    statsByAuthor = log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
    #############
    stats = "!sh -c 'git log --pretty=\"format:%aN\" -"


## Recherche

// rechercher dans le projet une expression précise -> renvoi le(s) fichier(s) concerné(s)

    #!bash
    git grep "DossierDeDemande dossier = demandesSurServiceConnecte.First(); // lol"

//rechercher une expression précise sur un fichier -> renvoi le n° de commit, l'intitulé et son auteur

    #!bash
    git log -Slol -- sources/Dicsit.SiteWeb/LogiresoNet/Areas/Coordination/Controllers/SuiviController.cs

    #!bash
    git diff -G <regex>
    git grep <regex>


## Dépôt distants

    #!bash
    git remote -v show => donne les url en fetch et en push
    
    git remote rm origin
    
    git remote add origin <url>
    
    git remote set-url origin http://FerryJ%40MARSH.LOCAL:monmotdepasse@southp/Git/Dicsit.Core.git => changer de dépôt
    git remote set-url origin http://FerryJ%40MARSH.LOCAL:monmotdepasse@southp/Git/Dicsit.git
    
    git clone --recursive http://FerryJ%40MARSH.LOCAL:monmotdepasse@southp/Git/Microsoins.NET.git
    git clone --recursive http://FerryJ%40MARSH.LOCAL:monmotdepasse@southp/Git/Dicsit.Core.git

## Github

La problématique : j'ai forké un projet git et j'ai soumis un fork il y a longtemps.
Le projet en lui même à évolué et on me demande de rebasé mes commits.

https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request

    #!bash
    git remote add pelican https://github.com/getpelican/pelican
    git fetch pelican
    git rebase -i HEAD~3
    git rebase pelican/master
    git push -f

## Liens

[http://www.git-attitude.fr/2014/09/15/30-options-git-qui-gagnent-a-etre-connues](http://www.git-attitude.fr/2014/09/15/30-options-git-qui-gagnent-a-etre-connues)

[http://stackoverflow.com/questions/2221658whats-the-difference-between-head-and-head-in-git](http://stackoverflow.com/questions/2221658/whats-the-difference-between-head-and-head-in-git)


