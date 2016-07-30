Title: The QuiZz : Partie 2
Category: rust
Tags: rust, gettext, cli, postgresql
Date: 2016-05-14 12:12
Slug: the-quizz-part-2
Authors: Jérémie Ferry
Status: published
Summary:

## The QuiZz : Partie 2

Comme promis, la partie 2 ne va s'atteler qu'à fournir le même cahier des charges que le soft de la partie 1 mais pour une appli web.

[dépôt Git : Etape 2](https://github.com/mothsART/the_quizz/releases/tag/part2)

## Pré-requis

Pour suivre, il vous faudra connaitre les grandes lignes de fonctionnement du dev web.

On va donc utiliser le mini-framework [**Iron**](http://ironframework.io) pour celà et quelques plugins utiles (rajouté dans le fichier **cargo.toml**).

Pour donner un peu de charme au projet, je lui cole le framework **Bootstrap** avec le thème libre [**SB-Admin-2**](http://blackrockdigital.github.io/startbootstrap-sb-admin-2/pages/index.html)

Ok, c'est vraiment too much pour une partie 2 mais ça met les bases pour les étapes suivantes.

## côté serveur (Rust)

### Les plugins

- staticfile : permet d'inclure des fichiers statiques (javascript, css, html, polices, images etc.)
- router : préciser les différentes urls de l'applicatif (en GET et POST)
- mount : outil glue permettant de délivrer des routes et des données statiques au sein du même serveur.

### Templates

Je suis encore un utilisateur de **Django** et **Flask** et des langages de templates tel que **Jinja**.

J'ai découvert que **Jinja** était en parti supporté par **Rust** via [**Tera**](https://github.com/Keats/tera)

Vu que j'ai carte libre, je parts donc sur cette techno.

Pour compiler le template, il suffit d'utiliser

    #!sh
    cargo run --bin compile_templates


### Refactoring

Vu que l'on a désormais 2 applicatifs (**cli** et **web**), il est utile de partager des ressources en commun : tout est centralisé dans le fichier **lib.rs**

## Côté client

Pour ceux qui ne l'on pas encore compris, j'ai un vrai mépris pour les technos autours de **Javascript** : c'est unsafe à souhait et à tous les désavantages d'un langage interpreté.

Néanmoins, je vais essayer d'en tirer le meilleur en utilisant [**ma nouvelle stack frontend**](stack-frontend.html)

## IHM

L'utilisation d'une interface web n'étant pas véritablement équivalente, il y a quelques différences :

- pas de possibilité de quitter l'applicatif

### Si vous utilisez une mauvaise version de NodeJS

* 1 Vider le cache de NPM

        #!sh
        sudo npm cache clean -f

* 2 Installer un mini soft appelé tout simplement **n** qui gère exclusivement l'installation de NPM

        #!sh
        sudo npm install -g n

* 3 Installer la dernière version stable de NPM

        #!sh
        sudo n stable

## Bounty

Si vous utilisez **[Tmux et Tmuxp](aide-memoire-tmux.html)**, voici une petite config qui devrait vous simplifier la vie :

    #!yaml
    session_name: the quizz
    windows:
        - window_name: watch (web)
          layout:  main-vertical
          shell_command_before:
            - cd ~/misc/rust/the_quizz
          panes:
            - shell_command:
              - cd static
              - echo 'gulp riot'
            - cargo run --bin compile_templates
            - cargo run --bin the_quizz_web
        - window_name: cli
          layout:  main-vertical
          shell_command_before:
            - cd ~/misc/rust/the_quizz
          panes:
            - shell_command:
              - cargo run --bin the_quizz
            - git status

## Conclusion

Y'a vraiment beaucoup de dépendances abordées dans cette étape.
Les évolutions devraient ralentir de ce côté pour la suite.

## Evolution pour l'étape n° 3

- Je viens de découvrir un **ORM** (viable) pour Rust : [diesel](http://diesel.rs) ça serait vraiment bête de s'en priver!

- Utilisation des [**API Html5** de stockage](http://caniuse.com/#search=namevalue-storage) et d'utilisation du [mode offline](http://caniuse.com/#feat=offline-apps)

- Version Cli : détection des évènements souris