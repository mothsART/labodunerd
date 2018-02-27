Title: Memo Diesel.rs
Category: Rust
Tags: rust, sql, diesel
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Je suis depuis quelques temps le projet Diesel.rs : le seul ORM en Rust digne de ce nom.

J'ai pas mal galéré à suivre ce projet tant qu'il nétait pas en version 1.0 avec tous les changements d'API.

Depuis quelques mois, il existe une version 1.0.

Il faut néanmoins encore pas mal fouiller pour trouver certains oublis dans la doc ou les exemples.

## Créer des requètes conditionnels

Et oui : souvent on veut créer des requètes selon des paramètres (notamment pour mieux factoriser le code).

Avec Diesel, il faut utiliser ".into_boxed()"

let mut sql = connect_four::schema::users::dsl::users
.filter(connected.eq(true).and(playing.eq(false)))
.into_boxed();

if (condition) {
    sql = connect_four::schema::users::dsl::users
    .filter(connected.eq(true).and(playing.eq(false)))
    .into_boxed();
}


