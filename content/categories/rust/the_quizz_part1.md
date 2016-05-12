Title: The QuiZz : Parti 1
Category: rust
Tags: rust, gettext, cli, postgresql
Date: 2016-10-05 19:12
Slug: the-quizz-part-1
Authors: Jérémie Ferry
Status: published
Summary:

## The QuiZz : Partie 1

Après mon apprentissage de Rust (doc, des tutos etc.), j'ai décidé de m'atteler à un projet un peu plus abouti.

Comme toujours, je pars du principe qu'il vaut mieux se lancer sur des projets minimalistes et allez au bout plutôt que de partir dans du gargantuesque et bacler.

**The QuiZz** c'est donc un logiciel créé dans l'optique d'apprendre **Rust** et ses librairies, le tout en plusieurs étapes :
[https://github.com/mothsART/the_quizz](https://github.com/mothsART/the_quizz)

## L'étape 1 : le minimum syndical mais quelques bases tout de même

### Utilisation de Rustbox

**[RustBox](https://github.com/gchp/rustbox)** est une implémentation de **Termbox** en Rust.

En somme, ça permet de faire des appli en **cli** à la manière de **NCurses** mais via une API la plus simple possible.

### The QuiZz en français

J'ai toujours préféré réfléchir à l'**i18n** dès la conception.
Pour celà, **gettext** reste l'indispensable.

La lib Rust qui l'implémente est vraiment très spartiate mais fait son job.
Néanmoins, il m'a fallu utiliser **[Babel](http://babel.pocoo.org/en/latest)** pour compiler mon **.po**.

### Contenu dans PostGreSQL

En terme de base de donnée SQL, **PostGreSQL** est, pour ma part, ce qui se fait de mieux donc autant commmencer par là.

Même constat : le wrapper est minimaliste mais suffisant.

## Le concept

On abonde le soft de questions/réponses et l'utilisateur final utilise une IHM lui permettant d'obtenir des questions (au hasard pour l'instant) et d'y répondre.

Pour simpler au maximum, **The QuiZz** ne permet que de poser des questions fermés : <kbd>Oui</kbd> ou <kbd>Non</kbd>.

C'est très basique mais par conséquent très simple à appréhender.

Enfin, le logiciel répond par **✔** ou **✘**.

## Populariser sa base

    #!sql
    create TABLE questions (
    id SERIAL PRIMARY KEY,
    entitled VARCHAR NOT NULL,
    explanation VARCHAR NULL,
    source VARCHAR NULL,
    response BOOLEAN NOT NULL
    );

    insert into questions (entitled, response) values ('Rust est-il un langage interprété ?', false);
    insert into questions (entitled, response) values ('Cargo est-il le gestionnaire de paquets de Rust ?', true);

## IHM

- Pour lancer le soft, on fait : **cargo run**
- Pour en sortir, on appuie sur la touche **q**
- Pour sélectionner une réponse, on peut s'aider des flêche gauche <kbd>←</kbd> et droite <kbd>→</kbd>
- Pour valider une sélection, on appuie sur entrée
 Sinon, on peut utiliser les raccourcis clavier <kbd>o</kbd> pour **Oui** (Attention, en anglais, on utilise <kbd>y</kbd>) et <kbd>n</kbd> pour **Non**.

## Evolution pour l'étape n° 2

Pour l'étape 2, je ne toucherais strictement à rien de l'existant.

Mon but est de reproduire le comportement du soft cette fois ci sous la forme d'une appli web via **[Iron](http://ironframework.io)** et d'utiliser **[RiotJS](http://riotjs.com/fr)** côté client.

## Vers l'infini et au delà

Dans le désordre, voici les évolutions possibles :

- abstraction pour utiliser d'autres bases de données SQL et NoSQL (**Redis** sans doute en priorité !)
- une IHM de type Dashboard : édition des questions, statistiques etc.
- une appli Android
- un choix de réponses possibles > 2
- des réponses ouvertes
- 
- pfuu, j'avais dit que c'était pas un projet sérieux
