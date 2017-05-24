Title: Ma stack Frontend
Category: frontend
Tags: frontend, css, javascript
Date: 2016-04-24 12:20
Slug: stack-frontend
Authors: Jérémie Ferry
Status: published
Summary:

## Intro (Gros WIP Unstable!!!)

Ma stack côté frontend (en constante évolution).

Comme tout **bon** développeur, je suis fainéant :
faire et refaire des tâches ingrates (cqfd: automatisable) me répugne.
De plus, j'aime avoir une certaine assurance sur le code produit. (surtout sur le javascript!)

Pour la partie frontend, je me suis créé un socle de démarrage avec une compilation de tout ce qui est hype (presque tout) côté JS.

mon dépôt : [https://github.com/mothsART/frontend_workflow](https://github.com/mothsART/frontend_workflow)

Mon usage est de le cloner dans un projet mère et de supprimer le .git dès qu'il est suffisament mature.

## Assurance qualité (QA)

- Utilisation des linter : **csslint**, **stylelint** et **eslint**

eslint est utilisé avec l'option **fix** qui permet de corriger automatiquement les soucis rencontrés.

Csslint n'a malheureusement pas cette fonctionnalité.

StyleLint se distingue de Csslint en utilisant browserList.

- **csscomb** : organise les instructions css
- **cssbeautify** : arange le css pour qu'il soit lisible : espacements et les 
indentations parfaitement respectées.
- **autoprefixer** : plugin PostCSS qui ajoute les préfixes propres aux navigateurs.

## BrowserList

Permet de définir quels navigateurs sont supportés.

Le package.json contient sa configuration.

Ca concerne les modules **autoprefixer** et **stylelint**.

## Examples

Pour donner un réel périmètre fonctionnel de cette stack, je créé au fur à mesure des fichiers d'exemples css, javascript et des composants Vue.js.
Le but est bien évidement de démmarrer un nouveau projet avec de la matière.

Néanmoins, il est possible de partir, via une commande avec un projet vierge :

    #!sh
    gulp clean

## Mise en prod

Une mise en prod de fichiers statiques a ses exigences.
Il faut:

- concaténer les fichiers (une requête HTTP par ressource)
- les minifier
- vu qu'on utilise de la transpilation : générer des css.map/js.map

L'usage des extrémistes de Nodejs va plus loin en incluant le css dans le javascript: Je ne suis pas fan donc vous ne trouverez rien de ce genre.

## Frameworks et libs employés

- [NPM](./npm.html)
- [NodeJS](./nodejs.html)
- [Gulp](./gulp.html)
- [BabelJS](./babeljs.html)
- [Vue](./vue.html)
- [PostCSS + CssNext](./postcss.html)

## Sublime text

- Css lisible : extension de Sublime text

## Récapitulatif des commandes principales

1. Cloner le dépôt :

Copier le projet

    #!sh
    git clone https://github.com/mothsART/frontend_workflow.git
    cd frontend_workflow


2. Installer les dépendances

on parcours le fichier package.json et on installe l'ensemble des dépendances

    #!sh
    npm install


3. Commencer à travailler (ça fait un watch)

On se met en mode debug :

    #!sh
    npm start


4. On Crée les fichiers destiné à la prod :

Transpilation, concatènation et minifification des fichiers via :

    #!sh
    gulp


5. Avant de commiter, on déclenche un process d'**assurance qualité**

Si l'on désire supprimer les fichiers d'exemples

    #!sh
    gulp clean

Opération inverse (reafficher les exemples)

    #!sh
    git checkout -- app/