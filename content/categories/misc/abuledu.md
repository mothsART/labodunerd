Title: AbulEdu
Category: misc
Tags: linux, libre
Date: 2016-07-12 21:40
Slug: abuledu
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Etant un jeune papa et défenseur d'un numérique ouvert, citoyen (liberté, égalité, fraternité) et responsable, j'ai décidé de participer au projet **[AbulEdu](https://fr.ulule.com/developpement-dabuledu)**.

Pour l'instant, ça ne concerne que la création d'illustrations.

L'objectif est à multiple tranchants : elle va concerner **[Wikipédia Commons](https://fr.wikipedia.org/wiki/Utilisateur:MothsART)**, **[VikiDia](https://fr.vikidia.org/wiki/Utilisateur:MothsART)** et **[OpenClipArt](https://openclipart.org/user-detail/mothsart)** dans la foulée.

## Les pré-requis

Avant de participer bêtement, je me suis mis en relation avec des membres de l'association.

Leurs directives étaient claires et fondées sur 3 axes

- Besoin d'illustrations vectorielles en 
**[découverte du monde](http://media.eduscol.education.fr/file/Progressions_pedagogiques/78/2/Progression-pedagogique_Cycle2_Decouverte_du_monde_203782.pdf)**

- L'inventaire systématique de ressources libres nécessaires pour les 8-11 ans en histoire, géographie, biologie et mathématiques :
[Leur thésaurus](http://thesaurus.abuledu.org/thesaurus/vocab/index.php)

- Des productions artistiques sous la forme d'histoires courtes : je ne pense pas paticiper pour l'instant.

## Contraintes documentaires

Avant de me lancer dans la production d'une illustration, je vais tout d'abord m'assurer qu'elle n'existe pas et qu'il y ai une vrai valeur ajouté.

Ensuite, je vais me documenter à minima sur le contexte.
Par exemple, une illustration historique nécessitera de se documenter afin d'éviter les anachronismes.

## Contraintes Techniques

Développeur avant tout, je me mets des jalons techniques pour :

- booster ma productivité (la contrainte de temps est hyper importante)
- Fournir une expérience utilisateur optimale

Pour les illustrations vectorielles, j'utiliserais exclusivement **Inkscape** (Outil libre mature).

Les couleurs choisis seront, dans l'idéal définit selon 2 contraintes :

- contraintes d'impression (conversion en CMJN possible sans que ce soit trop pénalisant)
- contrainte de dyschromatopsie (daltonnisme) :
Le daltonisme représente 8 % de la population masculine et 0.5 % de la population féminine => ces chiffres sont par conséquent non anodin. (j'ai par ailleurs plusieurs personnes daltonniennes dans mon entourage)
Les enfants sont bien entendus concernés par cette anomalie.
Il est donc important que les illustrations soient pleinement fonctionnel avec leur déficience et n'entrave en rien leur apprentissage.

Je n'utiliserais pas :

- de filtres SVG
- de flou (le seul usage possible serait pour une image avec une focale marqué)
- le moins possible de transparence
- peu ou pas de dégradés
- peu ou pas de courbes de béziers (là c'est clairement personnel et lié à mon style : je trouve que je passais beaucoup de temps à éditer des courbes de bézier alors que l'ajout d'un ou 2 points avec des arrêtes tranchantes était plus efficasse)

On pourrais définir ça comme de l'extrémisme mais j'ai remarqué que ce type d'usage est :

- Rarement adéquate pour mon style de dessin. (plus pour du photo-montage)
- Gourmant en ressource à l'édition (et je déteste bosser sur mes illustrations avec un poste qui ram, tricher avec des calques masqués pour éviter les lenteurs etc.)
- Gourmant en ressource pour l'utilisateur final : ça c'est encore plus pénalisant car je souhaite que l'expérience utilisateur soit la meilleur et pour le champ le plus large possible.
Dans l'idéal, il faudrait que l'illustration soit visible pour un pc reconditionné, ayant déjà d'autres applicatifs (plus ou moins gourmant d'ouvert).
- Support Hétérogène : là je parle principalement des filtres SVG : tous les moteurs de rendu ne les supportent pas ou pas pleinement.

### Optimisation du SVG

[SVGO](https://github.com/svg/svgo)

[Bien comprendre SVG](https://vimeo.com/179313779)

## Cohérence graphique

Ca peut paraitre évident mais néanmoins nécessaire.
Mes illustrations resterons cantonnés sur le même style : plutôt réaliste (sans être photo-réaliste), stylisé (pas de détails inutiles et chronophage à la création) pas ou peu de contours, des contrastes de couleurs marqués.

La plupart du temps, je vais composer mes dessins à partir de plusieurs sources sur Internet avec une étape intermédiaire papier pour composer mon image.

Sur Inkscape, je pose les grandes lignes (proportions) et affine jusqu'à arriver au résultat final.

## License

Comme la paternité de l'oeuvre n'a pas vraiment d'importance à mon sens, je choisi la **[License Creative Commons CC0 Transfert au Domaine Public](https://creativecommons.org/publicdomain/zero/1.0/deed.fr)** ou plus occasionnellement la **[cc-by-sa](https://creativecommons.org/licenses/by-sa/3.0/deed.fr)**.

## Fréquence

Pou l'instant, je me met un objectif bas : 1 contribution par mois **obligatoire** pour la constance.
Après, je serais quitte de dépasser...

## L'épreuve du feu

Faire participer mes enfants au projet!

Leur intérêt, avis, impression doit avoir une conséquence favorable ou une remise en question.

## Conclusion

Après la réflexion, l'action !

## Mes réalisation

[Campement du Paléolithique](./abuledu-camp-paleolithique.html)

[Mastondonte](https://commons.wikimedia.org/wiki/File:Mastodonte.svg)
