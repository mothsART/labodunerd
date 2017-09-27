Title: Phonectic Lab
Category: rust
Tags: phonetic, distance, rust
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: phonetic-lab
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Ce projet est un banc de test autours des principes de la phonétic et des moteurs de recherche se basant sur ces algorithmes.

L'idée est de comparer les différents algorithmes de distance (Jaro, Levenstein) et d'en déterminer des éventuels heuristiques :
selon certaines conditions, on utilisera un algorithme plutôt qu'un autre afin de proposer dans un ensemble de recherche, des performances optimales.

Ce banc de test permettra également de comparer les performances brutes de plusieurs moteurs de base de données : SQL et NoSQL.

Des benchmarks en situations "réels" me permettrons d'en tirer des conclusions. (peut-être inédites)

Enfin, il me permettra de tester mon propre moteur de phonétic dédié à la langue française !