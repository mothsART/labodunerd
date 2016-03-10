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

## Tmuxp

Cette lib python permet de configurer facilement des espaces de travail pour **Tmux**.

Un simple :

    #!bash
    tmuxp load

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


Si vous voulez concatener plusieurs espaces de travail en un, c'est possible :

### Remarques

Il manque sans doute le support de **Toml** : le meilleur format de conf de tout les temps!