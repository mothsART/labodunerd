Title: Ce n'est qu'un au revoir JSON
Category: 
Tags: 
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Là ou je peux me passer de JSON, je le fais sans regret.
C'est un langage à mon goût **batard**, illisible, faiblement typé...
très dépendant du langage Javascript... tout aussi mauvais.

## JSON n'est pas fait pour de la configuration

Quand je vois des fichiers de conf de plusieurs centaines de lignes, je pleure du sang...
T'oublis une virgule et paf !

Si l'on veut un truc propre pensé pour de la config et rien que pour de la config, il faut choisir **TOML**.

Et surtout : **IL NE PERMET PAS DE COMMENTAIRES !!!**

**VDM** : Quand je vois les fichiers package.json de npm et que j'aimerais juste commenté des lignes pour mes tests.

## JSON ne peut pas remplacer du XML

JSON n'a pas de format DTD et encore moins de XSL Shema officiel.
Pour valider un document, c'est du coup compromis.

## JSON n'est pas un bon format pour de l'échange de donnée

Si l'on souhaites échanger des données, je considère qu'il faut forcément réfléchir à un format le plus concit possible. La bande passante à forcément un coût.

Dans ce cas, je conseil vivement un format binaire et mon choix se porte naturellement vers **MessagePack** : un format binaire pour représenter des structures de données.

Si l'on veut valider des données avant l'envoi ou après réception de données, rien n'empêche de passer par un format XML intermédiaire.

## Conclusion

Il y a des formats qui doivent appartenir au passé...
(Les formats binarisés de Json n'étant que des jambes de bois)