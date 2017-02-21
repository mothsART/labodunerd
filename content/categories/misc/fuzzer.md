Title: Fuzzer
Category: misc
Tags: fuzzer, python, rust
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: fuzzer
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Ca fait un moment que je me passionne pour le fuzzing sans vraiment écrire à ce sujet.

## Fuzzer connus et spécificité

###  (ZZUF)[http://caca.zoy.org/wiki/zzuf]

Complètement **stochastique**.
Le fuzzer de licaca et Vlc : très bon pour les codecs et formats vidéos

### AFL

Provient de C++.

* afl est un fuzzer intelligent dans le sens ou il va changer l'input pour explorer de nouvelles branches du code.
(il change des octets au hasard, regarde si c'est passé par un nouveau chemin dans le code, et si ça change pas, ente une nouvelle approche)

*  il peut partir d'un existant (passage d'un fichier valide) et créer de l'entropie autours.


Variante pour python : http://jwilk.net/software/python-afl
Variante pour Rust : https://github.com/frewsxcv/afl.rs

### QuickChef

Provient de Haskell.

Variante pour Rust : https://github.com/BurntSushi/quickcheck

### (Fusil)[http://fusil.readthedocs.io/]

Provient de la communauté **Python**

