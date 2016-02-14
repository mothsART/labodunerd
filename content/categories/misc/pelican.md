Title: Pelican
Category: Misc
Tags: zsh
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: pelican
Authors: Jérémie Ferry
Summary:

# Pelican

## Intro

Ce site est mon 2ème essai d'utilisation d'un générateur de site statique.
J'utilise pour la 2ème fois Pelican : j'ai hésité à passer par autre chose : Jekyl ou Hexo principalement.

Néanmoins, j'ai préféré continuer avec Pelican... je sais que le diable ce cache dans les détails, et qu'après un usage intensif, je ne vais trouver que les défauts mais néanmoins avoir des difficultés à les résoudres via des patchs.

## Pré-requis technique

* Markdown : J'ai finalement abandonné RestructuredText pour Markdown :
    plus de doc, plus flexible, (si je veux un jour changer de moteur statique) des éditeurs WYSIWYG plus aboutis.

* Gestionnaire de commentaires : Disqus

* Moteur de template pratique : Jinja est un bon cru ;)

* Possibilité de créer des pages avec des templates personnalisés

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

    * la création d'un id par ligne -> url avec une ancre

    * doc : [http://prismjs.com/plugins/wpd](http://prismjs.com/plugins/wpd)

    * Autolinker : [http://prismjs.com/plugins/autolinker](http://prismjs.com/plugins/autolinker)

* création d'un plugin permettant l'i18n sans l'obligatation d'avoir au minimum 2 langues. (pas trouvé via le plugin "i18n_subsite")

* création d'un thème perso, comprenant l'internationnalisation.

