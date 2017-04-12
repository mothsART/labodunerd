Title: Utiliser des logs avec Rust
Category: rust
Tags: rust, log
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: logs-rust
Authors: Jérémie Ferry
Status: published
Summary:

## Utiliser les logs en Rust (encore en brouillon)

Sur n'importe quel soft sérieux, les logs sont innévitables.
Voici mes experimentations dans le logging en Rust.

## La variable RUST_LOG

 Selon le renseignement de cette variable, on obtient un filtrage sur les logs de notre application.

 Cette variable utilise les expressions réglières

Utilisation (Ne pas afficher que les logs de type **info**) :

    #!sh
    RUST_LOG=info cargo run

On filtre les logs de type **error** et commançant par la chaine **Read**

    #!sh
    RUST_LOG=error/Read cargo run --bin cli


On filtre sur le module **cli** et sur le type **debug**

    #!sh
    RUST_LOG=cli=debug cargo run --bin cli

## slog

La crate **log** a quelques limitations que **slog** va étendre.

Entre autre :

- apporter de la couleur sur le terminal pour les différents type de log. (erreur en rouge, warn et orange etc.)
- changer les formats d'affichage facilement
- utiliser d'autre sortie que **stdout** : en html, en json, journald 
