Title: PostGreSQL
Category: Aide-memoire
Tags: postgres, postgresql, sql
Date: 2016-05-04 19:55
Slug: postgresql
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Mon aide-mémoire pour l'indéboulonable **PostGreSQL** : la meilleur base SQL libre !

## Commandes

**\q** : quitter

**\h** : aide

**\d** : liste les tables et les sequences

**\d nom_de_table** : donne le détail d'une table

**\dt** ou **SELECT * FROM pg_catalog.pg_tables** : liste uniquement les tables

**\l** : liste les bases

## Changer le mot de passe (de l'utilisateur postgres)

    #!bash
    sudo -u postgres psql

puis

    #!bash
    \password

## Load / Dump

**pg_dump dbname > outfile**

## Piste d'exploration

### Commits/RollBacks et save points

### Utilisation d'extensions

## Liste toutes les bases

    #!sql
    SELECT * datname FROM pg_database WHERE datistemplate = false;

## Liste toutes les tables

    #!sql
    SELECT * 
    FROM information_schema.tables 
    WHERE table_type = 'crossject_base' 
        AND table_schema = 'public' 
    ORDER BY table_type, table_name;

## Création de table

    #!sql
    CREATE TABLE films (
        code        char(5),
        title       varchar(40),
        did         integer,
        date_prod   date,
        kind        varchar(10),
        len         interval hour to minute,
        CONSTRAINT code_title PRIMARY KEY(code,title)
    );

## Insertion

    #!sql
    INSERT INTO films VALUES
    ('UA502', 'Bananas', 105, DEFAULT, 'Comedy', '82 minutes');
    INSERT INTO films (code, title, did, date_prod, kind)
    VALUES ('T_601', 'Yojimbo', 106, DEFAULT, 'Drama');

[http://stackoverflow.com/questions/9025515/how-do-i-import-modules-or-install-extensions-in-postgresql-9-1-9-2-9-3-9-4](http://stackoverflow.com/questions/9025515/how-do-i-import-modules-or-install-extensions-in-postgresql-9-1-9-2-9-3-9-4)

    #!sql
    CREATE EXTENSION earthdistance;

[http://www.postgresql.org/docs/9.1/static/fuzzystrmatch](http://www.postgresql.org/docs/9.1/static/fuzzystrmatch)

## Sequences

[http://dgriessinger.developpez.com/postgresql/sequences](http://dgriessinger.developpez.com/postgresql/sequences)

## Liens

[http://www.gcolpart.com/howto/postgresql.php4](http://www.gcolpart.com/howto/postgresql.php4)

[http://www.system-linux.eu/index.php?post/2016/03/10/installation-et-administration-Postgresql](http://www.system-linux.eu/index.php?post/2016/03/10/installation-et-administration-Postgresql)