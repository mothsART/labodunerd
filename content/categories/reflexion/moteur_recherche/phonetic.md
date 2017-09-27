Title: Phonetic
Category: reflexion
Tags: phonetic, phonex, metaphone
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Phonetic

Sur PostgreSQL : https://www.postgresql.org/docs/9.1/static/fuzzystrmatch.html

https://fr.wikipedia.org/wiki/Homonymie
http://www.easter-eggs.com/Recherche-approximative-avec
http://sebsauvage.net/wiki/doku.php?id=php:recherche_floue

CREATE EXTENSION fuzzystrmatch;

### Soundex

### Phonex

Soundex pour le français : http://www.trickytools.com/downloads/phonex2.c

### Double metaphone

Il est dit double car il peut retourner un code primaire et secondaire. (0 à 4 caractères)
Il est par conséquent bien plus précis que le **Soundex** et également plus adapté aux langues non anglophone.

Il a **16 consonnes** (le 0 représente le th anglais) :
      B  X  S  K  J  T  F  H  L  M  N  P  R  0  W  Y

Transformations:

   B ----> B      unless at the end of word after "m", as in "dumb", "McComb"

   C ----> X      (sh) if "-cia-" or "-ch-"
           S      if "-ci-", "-ce-", or "-cy-"
                  SILENT if "-sci-", "-sce-", or "-scy-"
           K      otherwise, including in "-sch-"

   D ----> J      if in "-dge-", "-dgy-", or "-dgi-"
           T      otherwise

   F ----> F

   G ---->        SILENT if in "-gh-" and not at end or before a vowel
                            in "-gn" or "-gned"
                            in "-dge-" etc., as in above rule
           J      if before "i", or "e", or "y" if not double "gg"
           K      otherwise

   H ---->        SILENT if after vowel and no vowel follows
                         or after "-ch-", "-sh-", "-ph-", "-th-", "-gh-"
           H      otherwise

   J ----> J

   K ---->        SILENT if after "c"
           K      otherwise

   L ----> L

   M ----> M

   N ----> N

   P ----> F      if before "h"
           P      otherwise

   Q ----> K

   R ----> R

   S ----> X      (sh) if before "h" or in "-sio-" or "-sia-"
           S      otherwise

   T ----> X      (sh) if "-tia-" or "-tio-"
           0      (th) if before "h"
                  silent if in "-tch-"
           T      otherwise

   V ----> F

   W ---->        SILENT if not followed by a vowel
           W      if followed by a vowel

   X ----> KS

   Y ---->        SILENT if not followed by a vowel
           Y      if followed by a vowel

   Z ----> S

https://github.com/Freyskeyd/nlp
http://aspell.net/metaphone/metaphone-kuhn.txt
http://aspell.net/metaphone/dmetaph.cpp

Sous PostGreSQL : select dmetaphone('gumbo');
=> ça ne marche pas bien dès qu'il y a des caractères accentués.

### Distance de Levenstein

### Références

http://www.norvig.com/spell-correct.html

http://stackoverflow.com/questions/487003/how-to-detect-a-typo-in-a-product-search-and-suggest-possible-corrections

PostGreSQL implémente la distance de levenstein, le double metaphone :

https://github.com/Freyskeyd/nlp

