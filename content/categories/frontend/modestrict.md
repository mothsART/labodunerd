Title: To be strict or not to be
Category: frontend
Tags: javascript, bench
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: strict-or-not
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Il est recommandé d'utiliser Javascript avec le mode strict.
Le mode strict c'est un passage à Ecmascript 5 et tous les navigateurs l'implémentent désormais.

## Oui, mais... pourquoi ?

- rendre toutes erreurs comme **explicites**
- Corriger les erreurs (surtout de typage) qui pose soucis au moteur Javascript pour de l'**optimisation**. (comprendre : conversion en bytecode)
- **interdire les mots clés de versions futures de Ecmascript**
- rendre **eval** et **arguments** plus compréhensible
- améliorer la **sécurité**

Voilà, j'ai fait un résumé de [ceci](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Strict_mode)


## Comme souvent, la réalité est plus nuancé

Me basant sur ce constat, je me suis pris au jeu et effectivement, un code **strict** est bien meilleur pour la détection des erreurs.

Reste un point qui me titillait (les 3 autres restent à mon sens du détail) :
est-ce que le mode strict améliore-t-il les performances ?

## Constat amer : Le mode strict n'améliore pas les performances

On nous aurait menti ?
Non : comme d'habitude, on nous a pas dit **toute** la vérité.

Après avoir fait des benchs un peu **naif**, je tombais sur un constat amer : mais les perfs en mode strict sont dégradés ?!

Après réflexion : j'ai enfin compris le poteau rose :

Si je test exactement le même code en mode strict et en mode non strict (et que celui-ci s'exécute en mode strict) : le code en mode non strict ira plus vite car celui-ci sera dépourvu de certaines vérifications.

En revanche, si l'on oubli de déclarer des variables (dans le cadre du bench, ce sera **volontairement** mais l'optique du mode strict c'est bien de détecter ce genre d'oublis **involontaires**), le code non strict sera plus lent que celui étant strict!!
En effet, le moteur javascript (qui fonctionne en réalité le même façon en mode strict que non strict : la seul différence résidera dans la présence ou non de ces fameux tests de pré-éxecution) va mettre plus de temps pour déterminer le type de la variable si elle n'est pas déclaré.

## Conclusion ?

Si l'on veut le code le plus rapide, le mieux est d'avoir un ***code strict** et surtout **ne pas le déclarer comme strict** !!!
On comprend mieux pourquoi aucune doc (de Mozilla ou autre) ne fait état de cette subtilité : ça serait se tirer une balle dans le pied. (genre : comment savoir si de gros sites sont réellement passés à Ecmascript 5 sans regarder si il y a une déclaration en mode strict ?)

Je conseillerais, si vous avez de vrais besoins d'optimisation (et que vous en avez la possibilité), de déclarer votre code en **mode strict** quand vous êtes en débuggage et ... en mode **non strict** quand vous êtes en prod.
Du coup, vous serez gagnant sur les 2 tableaux.

## C'est bien beau ton barratin mais qu'est-ce qui nous le prouve ?

Pour vérifier mes dires : voici quelques benchs qui témoignent de la véracité de mes propos : [bench]()

A bon entendeur ;)