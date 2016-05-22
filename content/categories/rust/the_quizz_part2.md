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

## Pré-requis

Pour suivre, il vous faudra connaitre les grandes lignes de fonctionnement du dev web.

On va donc utiliser le mini-framework **iron** pour celà et quelques plugins utiles (rajouté dans le fichier cargo.toml) : 

## côté serveur (Rust)

- staticfile : permet d'inclure des fichiers statiques (javascript, css, polices, images etc.)
- router : préciser les différentes urls de l'applicatif (en GET et POST)
- mount : outil glue permettant de délivrer des routes et des données statiques au sein du même serveur.

## côté client

Pour ceux qui ne l'on pas encore compris, j'ai un vrai mépris pour les technos autours de Javascript : c'est unsafe à souhait et à tous les désavantages d'un langage interpreté.

Néanmoins va essayer d'en tirer le meilleur en utilisant RiotJS (raison [ici]()) et Babel.js (raison [ici]())


### Si vous utilisez une mauvaise version de NodeJS

* 1 Clear NPM's cache:

        #!sh
        sudo npm cache clean -f

* 2 Install a little helper called 'n'

        #!sh
        sudo npm install -g n

* 3 Install latest stable NodeJS version

        #!sh
        sudo n stable

### installation des dépendances

    #!sh
    sudo npm install riot -g
    sudo riot --type babel source.tag

### installation de webpack

    #!sh
    sudo npm install webpack -g


## installation de postcss

sudo npm install postcss-loader --save-dev

sudo npm install precss --save-dev
sudo npm install autoprefixer --save-dev