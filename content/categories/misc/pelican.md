Title: Pelican
Category: Misc
Tags: zsh
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: pelican
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Ce site est mon 2ème essai d'utilisation d'un générateur de site statique.
J'utilise pour la 2ème fois Pelican : j'ai hésité à passer par autre chose : Jekyl ou Hexo principalement.

Néanmoins, j'ai préféré continuer avec Pelican... je sais que le diable ce cache dans les détails, et qu'après un usage intensif, je ne vais trouver que les défauts mais néanmoins avoir des difficultés à les résoudres via des patchs.

## Pré-requis technique

* Markdown : J'ai finalement abandonné RestructuredText pour Markdown :
    plus de doc, plus flexible, (si je veux un jour changer de moteur statique) des éditeurs WYSIWYG plus aboutis.

* Gestionnaire de commentaires : <del>Disqus</del> **[Isso](http://posativ.org/isso/)**

* Moteur de template pratique : **[Jinja](http://jinja.pocoo.org/)** est un bon cru ;)

* Possibilité de créer des pages avec des templates personnalisés

### Plugins utilisés

* Tag cloud : ajout de badges
* Ace editor
* Sitemap
* assets
* liquid_tags.video
* tag_cloud

* filetime_from_git : juste indispensable pour les feignasse comme moi qui n'ont pas envie d'éditer les dates de création et de modification d'un article. (attention, les dates sont modifiés sur l'article produit et non le source en markdown)

## Plugins à intégrer

* post_stats : étendre les fonctionnalités
* subcategory


### Mes contributions

Comme souvent, je trouve souvent des limitations/bugs à mes usages lorsque j'utilise une lib.
Pelican ne déroge pas à cette règle.

Voici mes contributions à ce générateur de site statique qui ne demande qu'à être connu :

* Rajout de badges (compte le nombre de tags) sur le plugin **tag_cloud**
[https://github.com/getpelican/pelican-plugins/commit/f4d717ff2d7b4c6ec621e82fdb441f6b1e37a3fc](https://github.com/getpelican/pelican-plugins/commit/f4d717ff2d7b4c6ec621e82fdb441f6b1e37a3fc)

[https://github.com/getpelican/pelican-plugins/commit/b5aaca7a68b993754e79e50e6dbbfcc8114ed761](https://github.com/getpelican/pelican-plugins/commit/b5aaca7a68b993754e79e50e6dbbfcc8114ed761)

[https://github.com/getpelican/pelican-plugins/commit/9e1d20653afb170b7bb5753e138ca64ce39af276](https://github.com/getpelican/pelican-plugins/commit/9e1d20653afb170b7bb5753e138ca64ce39af276)

* création d'un plugin permettant l'utilisation aisé de Ace Editor :

    Ace est juste fantastique -> [https://ace.c9.io/build/kitchen-sink.html](https://ace.c9.io/build/kitchen-sink.html) et sa page github [https://github.com/ajaxorg/ace](https://github.com/ajaxorg/ace)

    Il a beaucoup d'avantages :

    * coloration synthaxique

        Il lui manque cependant des choses :

        - la création d'un id par ligne -> url avec une ancre

        - doc : [http://prismjs.com/plugins/wpd](http://prismjs.com/plugins/wpd)

        - Autolinker : [http://prismjs.com/plugins/autolinker](http://prismjs.com/plugins/autolinker)

* création d'un thème perso :

    - [] I18n sur l'ensemble du site et des plugins
    - [x] Possibilité de changer de thème via un **dropdown bootstrap** + préservation du thème choisi dans un cookie. (qui a dit que les cookies avait besoin d'un site dynamique ?)
    - [] **en cours** : page 404
    * [] **en cours** : Utilisation de **[Isso](http://posativ.org/isso)** à la place de **Disqus** : permet des commentaires anonymes.
    * [] **en cours** : Des URLs avec une ancre peuvent avoir des soucis avec un menu fixe :
      l'option ** SCROLL_TOP_MARGIN** permet de rajouter des pixels suplémentaires pour éviter cette contrainte.
    * [] **en cours** : Utilisation d'une page de référence pour mon template avec le maximum de règles : [pelicans-template.html](/pelicans-template.html)
    * [] détections des liens externes cassés https://github.com/silentlamb/pelican-deadlinks
    * [] créer des alias https://github.com/Nitron/pelican-alias
    * [] créer un plugin qui détecte un changement d'url (avec git) et crée un alias à la volée. (une url ne devrait jamais renvoyer vers un 404 quand il est déplacé)

## Contribution à venir

* création d'un plugin permettant l'i18n sans l'obligatation d'avoir au minimum 2 langues. (pas trouvé via le plugin "i18n_subsite")

* transformation des [] et [X] en checkbox => utile pour des todolistes

