Title: Pourquoi Rust
Category: reflexion
Tags: rust, python, Java, Javascript, C, C++, C#
Date: 2016-03-20 10:00
Modified: 2016-03-20 10:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Depuis maintenant 1 an, je m'intéresse de près au langage Rust.
Qu'est ce qui peut motiver le choix d'un nouveau langage alors qu'il en existe déjà un nombre incalculable ?

## Pré-requis

Je connais très bien Python, C# et le C... un peu moins Java et encore moins le C++.

Sur tous les langages cité, j'ai une nette préférence pour le Python : simple, explicite, haut niveau.
C'est un language incroyable pour du script et du prototypage.

C# est aussi un bon cru, même si, il faut l'avouer, c'est souvent l'IDE Visual Studio qui lui donne autant de pouvoir.

## Les raisons

- différenciation entre *espace de nommage* et appel d'un attribut (propriété et méthodes).
C'est un peu déroutant quand on vient de Python et C# qui utilise que le **.** point délimiter les 2 aspects.
Problème => des confusions et des conflits possibles entre un nom et une propriété! En un mot : inadmissible !
Rust a choisi de distinguer les 2 et c'est tout bonnement pythonnesque : explicite is better than implicite => **::** délimiter les espaces de nommage et **.** pour appeler un attribut.

- variable immuable par défaut : parce qu'au final, il y a pas besoin d'avoir beaucoup de variables qui sont réécrites et que si elles le sont, c'est elles qui sont la cause d'effets de bord.
Réduire leur nombre, c'est assuré ses arrières et identifié la variable problématique plus rapidement.

- détection des **dead code** dès la compilation

- spécification explicite de la durée de vie d'une variable.

- Les objets invalides ne sont pas acceptés (ou difficilement contournables) : http://blog.guillaume-gomez.fr/Rust/1/10
Franchement, vu le nombre de bugs rencontrés en C# de ce genre (et la rigueur nécessaire pour les éviter au maximum), ce choix est pour moi du pain béni.

## Conclusion

Rust m'a supris : j'ai mis du temps avant d'avoir des bugs d'exécution vraiment pénalisant.
En définitive, rust vous invite à réduire la partie **dynamique** de votre programme et par conséquent gère un grand nombre des soucis directement à la compilation.

Peut importe le language utilisé, on ne peut garantir un programme comme stable!
La notion de bug étant elle-même confuse : c'est un comportement non désiré mais le simple fait qu'un comportemnent non documenté soit 
Néanmoins, on peut limiter le champ 

zero-cost abstractions
move semantics
guaranteed memory safety
threads without data races
trait-based generics
pattern matching
type inference
minimal runtime
efficient C bindings