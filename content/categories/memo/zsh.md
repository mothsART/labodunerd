Title: Aide mémoire Zsh
Category: Aide-memoire
Tags: zsh, linux
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: aide-memoire-zsh
Authors: Jérémie Ferry
Status: published
Summary:

Et oui, pauvre mortel, je ne retiens pas toujours les fonctions utiles de ZSH et son pendant naturel "Oh my Zsh"

## Utilitaires

### Git

    #!bash
    git list # donne la liste des gitignores pouvant être créé à la volé
    git rust # créé un fichier .gitignore spécifique à rust
    cat monfichier.extension | colorize # afficher en couleur un fichier (utilise la lib python "pygmentize")

### Rust

    #!bash
    cargo # autocomplétion de l'utilitaire cargo

### Python

    #!bash
    pyfind # recherche uniquement les fichiers .py
    pyclean # supprime tous les fichiers bytes-code d'un projet

### Rsync

    #!bash
    alias rsync-copy="rsync -avz --progress -h"
    alias rsync-move="rsync -avz --progress -h --remove-source-files"
    alias rsync-update="rsync -avzu --progress -h"
    alias rsync-synchronize="rsync -avzu --delete --progress -h"

### Editeur

    #!bash
    st # sublime-text

### Web search

    #!bash hl_lines="2"
    google pattern1 pattern2 # va lancer un navigateur avec les mots recherchés
    github pattern1 pattern2 # va lancer github avec les mots recherchés
    wiki pattern1 pattern2 # va lancer duckduckgo avec les mots recherchés dans la catégorie "wiki"
    news pattern1 pattern2 # va lancer duckduckgo avec les mots recherchés dans la catégorie "news"
    youtube pattern1 pattern2 # va lancer duckduckgo avec les mots recherchés dans la catégorie "youtube"
    map pattern1 pattern2 # va lancer duckduckgo avec les mots recherchés dans la catégorie "map"
    image pattern1 pattern2 # va lancer duckduckgo avec les mots recherchés dans la catégorie "image"

### zsh-navigation-tools

    #!bash
    n-cd
    n-alias

## Mes scripts d'à moi

