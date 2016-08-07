Title: NPM
Category: frontend
Tags: nodejs, npm, javascript
Date: 2016-05-15 14:5
Slug: npm
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Si l'on veut faire du dev frontend de qualité, NodeJS et son gestionnaire de dépendance, NPM est désormais indispensable.

## NPM

Npm va chercher ses dépendances dans un fichier packages.json (éditable via npm init)

### installer les dépendances

    #!sh
    npm install

Si certaines dépendances facultatives pose soucis :

    #!sh
    npm install --no-optional
### installer les dépendances utilisé uniquement en développement

    #!sh
    npm install --save-dev

### installer une dépendance de manière global

    #!sh
    npm install -g eslint

### Lancer le site web localement

    #!sh
    npm start

### Mise en production

    #!sh
    npm run build --production

## Installer la bonne version de NodeJS

Si vous installer une version trop récente, vous courez tout droit à la catastrophe.

    #!sh
    sudo npm install n
    sudo n 5.11.1
