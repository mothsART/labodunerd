Title: Aide mémoire Tmux
Category: Aide-memoire
Tags: tmux, tmuxp, python, linux
Date: 2016-02-26 20:48
Slug: aide-memoire-tmux
Authors: Jérémie Ferry
Status: published
Summary:

## Introduction

Ca fait maintenant 2 bonnes années que j'utilise **Tmux** à la place du viellissant **Screen**.

Tmux est un **multiplexeur** de terminal **configurable** qui gère aussi bien les raccourcis clavier que les interactions de la souris.

## Raccourci dans Tmux

- killer la fenêtre courante et tous les panes qu'elle contient
<kbd>Ctrl</kbd> + <kbd>a</kbd> puis <kbd>&</kbd>
- 

## Tmuxp

Cette lib python permet de configurer facilement des espaces de travail pour **Tmux**.

### Configurer son .zshrc ou .bashrc

Ajouter ceci pour avoir l'autocompletion

    #!bash
    eval "$(_TMUXP_COMPLETE=source tmuxp)"

### Tmuxp Load
Un simple :

    #!bash
    cd ~/.tmuxp && tmuxp load

va me proposer l'autocompletion et me donner ma liste de fichiers yaml d'espace de travail :

![tmuxp load](static/images/tmuxp_load_labodunerd.png)

Par exemple, pour manager ce site, j'utilise cette config :

    #!yaml
    session_name: labodunerd website
    windows:
    
    - window_name: labodunerd
      layout:  main-vertical
      shell_command_before:
      - workon labodunerd
      panes:
        - pelican content
        - shell_command:
          - cd output
          - python -m http.server
    
    - window_name: labodunerd (git)
      layout:  main-vertical
      shell_command_before:
        - workon labodunerd
      panes:
        - git st
        - shell_command:
          - cd output
          - git st
    
    - window_name: ace_editor plugin (git)
      layout:  main-vertical
      shell_command_before:
        - workon labodunerd
      panes:
        - shell_command:
          - cd pelican-plugins/ace_editor
          - git st
        - shell_command:
          - cd themes/lab
          - git st


et le résultat de son chargement :

![tmuxp load](static/images/tmuxp_labodunerd.png)

Si vous voulez concatener plusieurs espaces de travail en un, c'est possible.

### Tmuxp freeze

Permet de faire un snapshot de votre tmux.

### Tmuxp import

Il existe 2 gros concurrent à tmuxp : 

- teamocil
- tmuxinator

Les fichiers de configuration sont sensiblement différents mais les fonctionnalités restent les mêmes.
Cet outil en cli permet de les convertir en un format lisible pour Tmuxp.

### Tmuxp convert

On peut actuellement utiliser 3 types de fichiers de config différents :

- du python pure
- du yaml
- du json

Si l'on veut passer de l'un à l'autre, cet outil en cli est juste indispensable

### Remarques

Il manque sans doute le support de **Toml** : le meilleur format de conf de tout les temps!

## Etendre vos super-pouvoirs avec Tmux

### une ligne de commande permettant de supprimer l'ensemble des sessions Tmux

Rajouter ceci dans votre **.zshrc** ou votre **.bashrc** :

    #!bash
    function tmux_kill_all_sessions() {
        tmux ls;
        local tmux_session=`tmux ls | grep --color=never : | cut -d. -f1 | awk '{print substr($1, 0, length($1))}' | awk -F: '{print $2}'`;
        # "awk -F: '{print $2}'" => permet de supprimer le numéro de ligne
        # préfixé par grep (dût à GREP_OPTIONS='-n')
        tmux kill-session -t "$tmux_session";
    }
    alias tmuxkillallsessions='tmux_kill_all_sessions'
