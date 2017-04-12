Title: Brainstorm autours de la Correction Gramatical
Category: reflexion
Tags: grammaire, phonetique, token, rust
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: brainstorm-correction-grammatical
Authors: Jérémie Ferry
Status: draft
Summary:

## Intro

Brainstorm autours de la création d'un Correcteur orthographique.

1. Utilisation de Rust :
- performance !
- future plugin de Servo ?
2. API permettant de l'utiliser sous forme d'appli CLI, serveur etc.
3. Utilisation de Token (https://github.com/cjqed/rs-natural)
4. Utilisation de ma lib de phonetique (phonex)

5. Grammalecte n'utilise pas de  Token et s'en sort pourtant très bien.
Voir pour utiliser 2 processus de reconnaissance en simultanné.

6. Utilisation de wiktionnaire
7. Utilisation d'une base SQlite et/ou une version de Redis sans client/serveur (embed redis : **vedis**)

## Liens

### Grammalecte

http://linuxfr.org/news/grammalecte-correcteur-grammatical
https://www.dicollecte.org/grammalecte/outils.php

### QDictionnaire

http://linuxfr.org/news/version-3-0-de-qdictionnaire
http://www.gillesmaire.com/tiki-index.php?page=qdictionnaire

un dictionnaire des noms des communes 
un dictionnaire des prénoms
un dictionnaire des synonymes
un dictionnaire des conjugaisons 
un dictionnaire de citations 
un dictionnaire des mots communs 
un dictionnaire des abréviations 
un dictionnaire de rimes
un éditeur poétique

### Verbiste

https://perso.b2b2c.ca/~sarrazip/dev/verbiste.html

### divers

http://www.norvig.com/spell-correct.html

http://www.reverso.net/spell-checker/french-spelling-grammar/
http://bescherelle.com/