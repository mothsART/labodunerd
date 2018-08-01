Title: Search diff image
Category: reflexion
Tags: rust
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: search-diff-image
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

La photo numérique nous a donné l'avantage de pouvoir prendre énormément de photos et de les trier par la suite.
Les avantages, pour ceux qui ont fait de l'argentique sont évidents.

Il reste que les inconvénients deviennent criants :
- une masse énorme de photos à regarder, trier, supprimer etc.

Ne serait-il pas possible d'identifier toutes les photos trop similaires ?

## La problématique

Un soucis en apparence simple.
IL est simple de vérifier que 2 images sont strictement identiques.
1 pixels de différence est c'est le drame : il faut comparer la matrice complète et le temps de traitement est par conséquent couteux.

Il faudrait donc 1 ou plusieurs hashs permettant de comparer des images sans reparcourir inlassablement leur contenu.

## Les solutions envisageables

### Comparer les ratios

Effectivement, il parait un peu débile de comparer une image en 16/9 avec une image en 4/3.

Petit piège néanmoins : les images qui ont subit une rotation ou un effet mirroir.

Un ratio peut être facilement stocké sous forme d'entier ou de valeur décimal.
Il est par conséquent facile de faire des tests sur une grande quantité de données.

### Comparer les espaces colorimétriques

Une image est divisé en plusieurs canaux : R, V, B, Opacité (PNG).

Ces valeurs sont des entiers donc on peut très facilement les trier. (médiane, moyenne, écart type)

On pourrait également étendre ce procédé sur des canaux plus proche de la perception humaine :

Pour celà, il y a TSV mais aussi L*a*b (CieLab)

### Comparer des applats de couleurs


La, on touche du doigt le machine learning.

### Liens

https://github.com/abonander/img_hash
https://github.com/abonander/img-dup



