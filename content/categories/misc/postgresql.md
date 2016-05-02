Title: Le stockage côté Javascript
Category: frontend
Tags: javascript frontend stockage sql
Date: 2016-03-19 16:00
Modified: 2016-03-19 16:00
Slug: stockage-frontend
Authors: Jérémie Ferry
Status: draft
Summary:

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


# Création de <table>

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

# Insertion

    #!sql
    INSERT INTO films VALUES
    ('UA502', 'Bananas', 105, DEFAULT, 'Comedy', '82 minutes');
    INSERT INTO films (code, title, did, date_prod, kind)
    VALUES ('T_601', 'Yojimbo', 106, DEFAULT, 'Drama');

http://stackoverflow.com/questions/9025515/how-do-i-import-modules-or-install-extensions-in-postgresql-9-1-9-2-9-3-9-4

    CREATE EXTENSION earthdistance;

http://www.postgresql.org/docs/9.1/static/fuzzystrmatch
