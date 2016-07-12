Title: Pourquoi Wayland
Category: reflexion
Tags: wayland, linux
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: pourquoi-wayland
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Beaucoup de bruit autours de **Wayland** (et de **Mir**) sans savoir ce que ça va apporter par rapport au serveur X (Xorg).
Du coup, j'essai d'éclaircir un peu par mes recherches.

## De la sécurité

## De l'abstraction

On sépare les clients : typiquement chaque zone de rendu (pour simplifier on peut dire fenêtres)

Chaque client passe par un protocole pour émettre des événements, en recevoir et pour mettre à jour son buffer.

Ce protocole c'est Wayland qui passe toutes ces infos normalisés à un compositeur.

Le compositeur est donc complétement isolé des fenêtres.

## KISS

Wayland sert grosso modo à récupérer les buffers CPU (**shared memory (SHM)**) et GPU (**GEM’s buffer sharing**) des différentes fenêtres et les transmettre avec leur ordre d'affichage à un composer via un protocole.
Ni plus, ni moins.

Une API C minimal sans prise en charge de buffer exotique.

Par conséquent plus simple à développer et à entretenir.

## Les bienfaits de la page blanche

Wayland c'est aussi un projet jeune qui ne traine pas les **deadcodes** de Xorg et son historique.

De plus, plein de nouvelles technos linux ont émmergé depuis quelques années :

- **Edev**
- **KMS** (**Kernel-based mode-setting**)
- **EGL** 

## Compositeurs

Les devs de Wayland fournisse **weston** : compositeur de référence et de démo de Wayland.

## Et Mir dans tout ça

Ubuntu a décidé depuis 2013 de se la jouer perso en créant **Mir**.
Ce choix est fait principalement pour répondre à un besoin criant d'avoir quelques chose d'opérationnel pour du tactile.
A priori, ça porte du fruit.

Néanmoins, Mir fait office de protocole et de compositeur.
Il est donc 

## liens

http://mupuf.org/blog/2014/02/19/wayland-compositors-why-and-how-to-handle/
