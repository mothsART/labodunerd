Title: Connect Four
Category: rust
Tags: rust, jeu, puissance 4, webpack, javascript, vuejs, sass, postcss 
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: puissance4
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Vous aimez jouer au Puissance 4 et vous ne trouvez pas votre bonheur.
Voici peut-être un alternative pour vous !

Un jeu de puissance 4 en réseau !

## y'a quoi de neuf

Ce jeu n'a aucune prétention. C'est un puissance 4 classique avec aucune surprise dans le gameplay.

Néanmoins, ses atouts actuels :

- **full web** : vous n'avez besoin que d'un navigateur sans extension flash ou autre MST...
- **full responsive** : si vous êtes adeptes du pixel art, passez votre chemin : 
ça reste désespérément lisse et adapté à la taille de votre écran. (tablette, smartphone, ordi etc.)
- **jeu en réseau** : parce que jouer à tour de rôle sur son ordi, c'est un peu démodé, non ?
- **open source (license BSD)** : parce que je souhaites que mon projet profites à tous sans restriction
- **prix libre** : si vous estimez que ce que je fais à de la valeur, vous pouvez participer financièrement selon votre ressenti, vos moyens etc.
- **ergonomie** : rien de plus énervent dans un jeu ou logiciel qu'un parcours non intuitif
Tout doit rester simple, sans de vaines explications.

Et ses atouts futurs :

- **mode tournoi** avec gestion admin et stats : pour ceux qui aime les classements
- multi-langues : Le puissance 4 est un jeu universel mais une interface adapté à votre langue natale c'est quand même mieux, non ?
- appli native : pourquoi s'embetter avec un navigateur ?
- mode cli : pour les gros Geek qui ne sorte jamais de leur terminal
- un ou plusieurs bots : parce qu'il faut bien penser aux Connor en herbes qui rêve d'aligner 4 pions de la même couleur face à Skynet
- une API pour créer son propre Bot : parce qu'il existe des gars assez taré pour créer Skynet
- une ou plusieurs librairies qui permettrons de créer d'autres jeux avec un miminum d'efforts (gestion des utilisateurs espace admin, tournoi etc.)
- plusieurs jeux en simultannées pour le même joueur ou chaque partie est cloisonné dans un onglet
- réactivité
- paquet Debian
- image docker
- site de démo

## C'est bien beau tout ça mais si je veux essayer, je fais comment ?

Pour l'instant, tu compiles comme un grand.

1. On installe les dépendances manquantes

        #!bash
        apt-get update
        apt-get install curl git sqlite file clang make
 
2. On installe Rust et Cargo (si ce n'est pas déjà fait)

        #!bash
        curl -f -L https://static.rust-lang.org/rustup.sh -O
        sh rustup.sh -y --channel=nightly

3. Récupérer les sources :

        #!bash
        git clone https://github.com/mothsART/connect_four.git && cd connect_four

4. Lancer le serveur web HTTP (dans un terminal à part)

        #!bash
        cargo run --bin web

5. Lancer le serveur Webscoket (dans un autre terminal)

        #!bash
        cargo run --bin ws

6. On lance son petit navigateur chéri :

    * Si l'on est sur la même machine que le serveur : 127.0.0.1:8000 (ou localhost:8000) suffira
    
    * Si l'on est sur une autre machine appartenant au même réseau locale : ip_du_poste_serveur:8000

## Je suis sceptique : ça ressemble à quoi ?

La liste des utilisateurs connectés :

![La liste des utilisateurs connectés](static/images/connect_four/user_list.png)

Le jeu en cours entre l'utilisateur PrimTux et Windows :

![Le jeu en cours entre l'utilisateur PrimTux et Windows](static/images/connect_four/game_in_progress.png)

Sans Surprise, c'est l'utilisateur PrimTux qui gagne : 
![Sans Surprise, c'est l'utilisateur PrimTux qui gagne](static/images/connect_four/win.png)

## Sous le capot

Le but du projet est de s'étoffer et de vivre à l'épreuve du temps... tout un programme.

* Pour la partie serveur, je me suis rabattu sur Rust et le WebSocket.
Rust, car c'est un langage moderne à mon sens : sureté tout en gardant des performances plus qu'honorables
WebSocket car c'est la meilleur techno web pour avoir de l'interactivité 

Le stockage se fait dans une base de donnée SQLite

* Pour le code client, j'ai choisi une infrastructure à la pointe du web : config via **Webpack**, framework **Vue.js**, **Saas** et **PostCSS**.

## Vous pouvez être acteur du projet

Et oui, vous pouvez mettre une pierre à l'édifice.

Comment ? 

Déjà, en y jouant et en y prenant du plaisir !
En témoignant de votre entousiasme via un commentaire, un mail, une attention, un don.
En proposant des évolutions, des critiques, en remontant des bugs.

En proposant une traduction.

Enfin, en participant au code source, bien sur !

