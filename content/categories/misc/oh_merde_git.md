Title: Oh Merde Git
Category: misc
Tags: linux, libre, git, tuto, traduction
Date: 2016-07-12 21:40
Slug: oh-merde-git
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Voici la traduction de [http://ohshitgit.com](http://ohshitgit.com)

Pour éviter d'inonder cette traduction par des mots fleuries, j'ai décidé de remplacer **Shit** (litéralement **Merde**) par **Flûte**. (juron au combien moderne dans la francophonie)

## Oh Flûte GIT

Git est un outil complexe : il est facile de se tromper et trouver comment réparer vos erreurs est délicat...

La documentation de GIT tiens du paradoxe de l'oeuf et de la poule pour un débutant :

Il est quasi impossible de trouver une solution à un disfonctionnement si vous ne connaissez pas le nom exact de l'outil qui permet de le résoudre.

Donc voici quelques situations auquel j'ai été confronté et comment j'ai fini par m'en sortir : le tout expliqué dans un français intelligible.

## Oh flûte, j'ai dût utiliser Git n'importe comment ! Rassurez-moi : Git est pourvu d'une machine à remonter le temps magique ?!

    #!bash
    git reflog
    # Vous voyez l'historique de toutes vos actions sur GIT et ceci dans l'ensemble des branches !
    # chacune a un index HEAD@{index}
    # à vous de chercher la ligne juste avant que vous cassiez tout
    git reset HEAD@{index}
    # le résultat de la machine à remonter le temps

Cette commande vous permettra de soit :

* revenir juste avant des suppressions accidentelles
* supprimer des tâches qui ont cassés votre dépôt
* revenir juste avant une fusion **flûtique**
* tout simplement revenir à un état ou tout fonctionnait bien

J'utilise **reflog** ÉNORMÉMENT!!

Je tire mon chapeau aux très nombreuses personnes qui ont suggérées d'ajouter cette fonctionnalité à GIT!

## **Oh flûte GIT**, je viens de commiter et me suis apperçu juste après qu'il manque des choses

    #!bash
    # effectuez vos changements
    git add . # ou ajoutez manuellement des fichiers
    git commit --amend
    # suivez les instructions afin d'éditer ou de conserver l'intitulé du commit
    # C'est bon : désormais, votre dernier commit contient vos derniers changements

Ceci m'arrive habituellement quand je commit et que je lance des tests/analyseurs syntaxique... et VDM (Vie de flûte), j'ai oublié un espace après un signe d'égalité.

Vous pouvez bien évidement effectuer le changement dans un nouveau commit et utiliser **rebase -i** afin de fusionner les 2 commits mais l'astuce précédente est un million de fois plus rapide.

## **Oh flûte GIT**, j'ai besoin de changer l'intitulé du commit

    #!bash
    git commit --amend
    # suivez les instructions afin d'éditer l'intitulé du commit

Souvent provoqué par l'exigence stupide de la mise en forme des intitulés d'un commit. 

## **Oh flûte GIT**, j'ai accidentellement commité quelque chose sur la branche master qui aurait du se trouver dans une toute nouvelle branche

    #!bash
    # Créer votre nouvelle branche à l'état actuelle de la branche master
    git branch votre-toute-nouvelle-branche
    # Supprimer froidement votre commit de la branche master
    git reset HEAD~ --hard
    git checkout votre-toute-nouvelle-branche
    # Votre commit n'existe désormais que dans votre nouvelle branche :)


Remarque: ceci ne fonctionnera pas si vous avez déjà envoyé (pushé) vos changements sur **origin**.

Si vous avez fait d'autres choses avant, vous devrez effectuer **git reset HEAD@{number}** à la place de **git reset HEAD~**.
Tristesse infinie.

## **Oh flûte GIT**, j'ai accidentellement commité sur la mauvaise branche !

    #!bash
    # supprimez le dernier commit tout en gardant les changements effectués 
    git reset HEAD~ --soft
    git stash
    # déplacez-vous sur la bonne branche
    git checkout le-nom-de-la-bonne-branche
    git stash pop
    git add . # ou ajoutez manuellement des fichiers
    git commit -m "votre entête"
    # C'est bon: vos changements sont désormais sur la bonne branche

Beaucoup de personnes m'ont suggérés d'utiliser le **cherry-pick** dans ce cas de figure.

Peux-importe : utilisez ce qui a le plus de sens pour vous !

    #!bash
    git checkout le-nom-de-la-bonne-branche
    # Sélectionnez le dernier commit de la branche master afin de le copier sur votre branche
    git cherry-pick master
    # supprimez-le désormais de la branche master
    git checkout master
    git reset HEAD~ --hard

## **Oh flûte GIT**, j'ai effectué un diff mais rien ne se passe ?!

    #!bash
    git diff --staged

Git ne vous montrera pas les fichiers qui ont déjà été ajoutés dans la zone de transit (staging area) sans l'ajout de cet argument.

Fichier sous ¯ \ _ (ツ) _ / ¯ (oui, c'est une fonctionnalité, pas un bug, mais c'est déconcertant et non évident la première fois qu'il vous arrive!)

## Tous ce bruit assourdissent ne m'aide pas plus => j'abandonne.

    #!bash
    cd ..
    sudo rm -r fucking-git-repo-dir
    git clone https://some.github.url/fucking-git-repo-dir.git
    cd fucking-git-repo-dir

## Avertissement

L'auteur de ce court tutoriel ne se prétend pas être un expert GIT. (et son traducteur encore moins)

Ce n'est pas non plus une documentation exhaustive mais un bon point d'entrée pour les débutants.

Et oui, il existe mille et une autre façon de faire les mêmes choses avec d'avantage de théorie, de purisme mais j'en suis arrivé à écrire ses étapes simplifiées après plusieurs essais-erreurs successifs, ponctués de jurons et de colères incontrollables.

J'ai eu l'idée, assez folle, de partager le condensé de mes solutions avec une dose non dissimulable de légèreté et de blasphème.

## Conclusion

A ceux qui trouve que j'ai pris un peu trop de liberté sur la traduction de cet article, je leur dit litéralement : **flûte**!

Néanmoins, ils sont autorisés à me soumettre leurs améliorations !
C'est d'ailleurs aussi à ça que sert **GIT** !