Title: Bug
Category: reflexion
Tags: bug
Date: 2016-05-01 13:30
Slug: bug
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Mais qu'est-ce qu'un bug et pourquoi le développeur à ce sentiment d'inachevé ?
Je vais tenter via cet article de remettre les choses à plat sur ces notions, pris comme acquis et qui ne le sont généralement pas.

## Garantir un logiciel comme stable

Pour les développeur, je vous invite à vous mettre l'espace d'un instant dans la peau d'un commercial, décisionnaire ou tout simplement du client final.

Quel sont ses attentes : un logiciel qui **marche** si on pousse la naïveté à son paroxisme.
Mais derrière ce constat relativement simpliste, ce cache énormément de subtilité : 
- quel sont les temps de réactivité maximal autorisés pour que l'applicatif ne réponde plus au attente ?
- qu'est ce que l'on peut clairement identifié comme non désiré ? L'ergonomie, par exemple peut tout à fait être fonctionnel sans tout de fois satisfaire le client.

## Constat

Le problème est pris bien souvent à l'envers.
Ce qui régis les lois de l'informatique, se sont des lois physiques et mathématiques même si certaines abstractions nous semble parfois oublier cette dimension.

Pour comprendre un fonctionnement complexe, il est utile bien souvent de le fractionner en plusieurs problématique simples : https://fr.wikipedia.org/wiki/Diviser_pour_r%C3%A9gner_(informatique)

## Entrée / sortie

Un programme informatique est un ensemble d'opérations destinées à être exécutées par un ordinateur.
Il se résume donc à des entrées et des sorties possibles. (cf: univers des possibles)

Imaginons un programme qui renvoi une réponse en fonction de 2 entrées.
Les entrées sont 2 valeurs booléennes (vrai ou faux) et la sortie est une valeur booléenne.
Notre programme se prénome "démarrer la voiture" et les entrées sont respectivement : "insérer la clé" et "mettre sa ceinture".

Notre cahier des charges de se programme définit que la seul condition pour que la voiture démarre est que les 2 conditions initiales soit valides.

Combien de possibilité s'offre à nous ?
4 : 
- on a pas inséré la clé
- on a inséré la clé mais pas mis sa ceinture
- on a inséré la ceinture mais pas la clé
- on a inséré la clé et mis sa ceinture

Dans ce cas simple, il est facile de déterminer que notre programme fonctionne dans tous les cas possibles.

## Logiciels complexes : explosion combinatoire

Maintenant, abordont des logiciels tel que nous les connaissons.
Les entrées sont : les saisies du clavier, de évènements provenant de la souris, le système d'exploitation ainsi que navigateur utilisé, de Web services interrogés etc.

On peut vite se rendre compte que l'arbre des possibles est difficile à estimer mais qu'il se rapproche innexorablement vers l'infini. (surtout si il y a de la récursivité)

## Le leure du générique

Une lubie de beaucoup de programmeur est la généricité.
Un point commun pour plusieurs parties du logiciel.
Celà part souvent d'une bonne intension -> moins de code à produire donc une meilleur maintenance.
Néanmoins, l'effet pervers est de créer des parties qui font trop de choses, qui sont difficiles à retoucher et qui engendre par conséquent trop de conditions différentes. 
De plus : si le code générique comporte un bug, il risque fortement d'impacter tout l'applicatif là ou un autre bug n'aurait toucher qu'un effet marginal. 

## Solutions à envisager

### l'approche fonctionnel ou comment réduire les effets de bord

l'effet de bord fait parti de la hantise du programmeur.
Un correctif va entrainer une régression à un ou plusieurs endroits de l'applicatif sans lien direct avec la partie en question.
Le bug est par conséquent détecté plus tard, au plus mauvais moment (en production, par le client, le vendredi soir à la veille du départ en vacances)
Je parlais tout à l'heure de fractionnement et d'entrées / sorties.
L'effet de bord provient des variables globales réutilisés dans différents contexte.
L'approche fonctionnel annule totalement ce comportement : on déclare explicitement les variables muables (ça réduit déjà) puis on donne une durée de vie à ces dernières.
Résultat : on peut raisonner en réel boite noir ou une boite n'a strictement aucune influence sur une autre.

### API

C'est à la mode surtout avec les web services qui poussent comme les champignons.
Les meilleurs API sont les plus concices à mon sens.
Elles doivent également cacher les coulisses. (le fonctionnement interne)
L'utilisation doit de se fait être intuitive.

### Soigner les points d'entrée

Il vaut mieux contraindre un utilisateur plutôt que lui donner trop de libertés.
Moins de libertés sous-entend moins de possibles et par extension, moins de bugs.
Il vaut mieux avoir une politique de droits minimum et les étendre si besoin plutôt que l'inverse.

Dans une appli web, les points d'entrée peuvent être la grande variété de navigateurs (ayant chacun des comportements spécifiques).
Effectuer certains traitement côté serveur plutôt que côté client vont éviter ce type de bugs.

### tests unitaires et couverture

Si l'on veut donner un cadre à notre logiciel, les tests automatisés sont primordiaux.
Ces derniers obligent à mieux fractionner notre code en des zones minimales et donc réduire le champ des possible.
De même, ça oblige à chainer les process : chaque étapes sont indépendantes et leur concaténation réalise un scénario.
Si toutes nos fonctions sont testés et que par conséquent tout le code de notre applicatif est utilisé pendant l'automatisation des tests, on parle d'une couverture total.

Une couverture partiel donnera un indicatif : les zones non couvertes sont potentiellement moins sécurisé que celles couvertes.

Autre avantage des tests : la lecture des tests unitaires par un développeur donne directement le cahier des charges en réel de l'applicatif.

Si l'on met au point des tests unitaires dans un applicatif qui n'en avait pas auparavant, il faut impérativement s'attaquer aux parties génériques en priorité et au stockage de données (la suppression étant le point critique par excellence).

### Fuzzing ou comment le hasard peut être notre allié

Le fuzzing est un sujet à part. C'est un bon moyen de débusquer des bugs que l'on aurait sans doute difficilement trouvé par des méthodes classiques.
C'est une technique qui nécessite néanmoins de l'investissement et de l'expertise.
A privilégier sur des logiciels finis, ou l'on veut débusquer des soucis de sécurité.

## Conclusion

On peut dire qu'un logiciel à atteind ses objectifs si il fonctionne dans l'ensemble des cas d'un cahier fonctionnel. (donc une liste fini)
Il n'est dans ce cas aucunement exent de bugs, bien au contraire : il en reste sans doute une infinité.
La nuance est qu'ils ne sont pas pénalisant pour l'utilisateur.

Cette réflexion ne parle pas des autres aspects quant à la satisfaction cliente : à savoir la qualité du suivi, de l'assistance, de la réactivité, de l'ergonomie, de la pédagogie etc.