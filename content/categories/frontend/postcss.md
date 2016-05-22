Title: PostCSS
Category: frontend
Tags: css, postcss, javascript
Date: 2016-05-14 13:40
Slug: postcss
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Le css a des lacunes dont plusieurs pré-processeurs ont essayé (less, sass, stylus) de combler les lacunes.

Le soucis d'une surcouche c'est que ça nécessite d'apprendre un langage supplémentaire tout en connaissant bien le css généré.

En parallèle, les dernières spécifications du W3C comblent pas mal du déficit.
Elles ne seront pas implémenté sur tous les navigateurs avant un moment... alors qu'est-ce qu'on peut faire ?

Ben utiliser les dernières nouveautés et les compiler dans un format supporté actuellement ?!

C'est là, tout le défi et tout l'intérêt de **PostCSS** !

## Goodies

- On choisi quels sont les navigateurs impactés : on génére par conséquent du css valide pour ces navigateurs !
- utilisation de variables
- détecter des erreurs à la compilation plutôt qu'à l'execution.
