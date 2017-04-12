Title: Ma stack Rust
Category: rust
Tags: rust
Date: 2016-04-24 12:00
Slug: stack-rust
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

En vrac, les outils que j'utilise et perfectionne dans mon apprentissage et mon utilisation du language **Rust**.

## MAJ de Rust

On installe Rustup si il n'est pas présent :

    #!bash
    curl https://sh.rustup.rs -sSf | sh

Puis on installe une version Nightly

Plusieursfonctionnalités non stabilisés sont disponibles sur la version nightly (notamment l'api de linter utilisé par **Clippy** dans le paragraphe suivant)

    #!bash
    rustup install nightly

* On met à jour sa version de Rust

Ceci va mettre à jour notre version stable de Rust (par exemple passer de la 1.14 à la 1.16) mais aussi mettre à jour notre version **nightly** sur le dernier instantanné. (commit github)

    #!bash
    rustup update

## Assurance qualité avec le Linter Clippy

Dans Rust, il y a des bonnes pratiques ainsi que des faiblesses dans le compilateur de Rust (eh oui).
Pour pallier à ça, il existe l'utilitaire **Clippy**, un outil d'analyse statique qui va appliquer environ 200 règles sur le code parcourus.

Pour utiliser **Clippy**, il faut actuellement utiliser Rust en nightly :

    #!bash
    rustup default nightly

puis dans le fichier toml

    #!toml
    [dependencies]
    clippy = {version = "*", optional = true}

    [features]
    default = []

Et dans le fichier main.rs or lib.rs:

    #!rust
    #![cfg_attr(feature="clippy", feature(plugin))]
    #![cfg_attr(feature="clippy", plugin(clippy))]

Enfin, lancer l'analyse via :

    #!bash
    cargo build --features "clippy"

## Sublime-Text

- Support de la coloration synthaxique de Rust [https://packagecontrol.io/installation](https://packagecontrol.io/)
- BeautifyRust : formate le code Rust pour qu'il suive les bonnes conventions de codage. (et évite d'y penser)
Nécessite et utilise : **[rustfmt](https://github.com/rust-lang-nursery/rustfmt)**
- RustAutocomplete

Vous n'utilisez pas **Sublime** ou vous désirez en savoir d'avantage : https://areweideyet.com/

## Editeurs en ligne

- [editeur](https://play.rust-lang.org)
- [editeur multi-fichiers](http://www.tutorialspoint.com/compile_rust_online.php) : permet d'éditer, compiler et exécuter des projets complets (répartis sur plusieurs fichiers) tout en proposant des outils d'import et d'export
- [compilateur GCC](http://rust.godbolt.org)


## [Cargo graph](#cargo-graph)

Si vous désirez connaitre les dépendance de votre projet, vous pouvez étendre les fonctionnalités de **cargo** avec **[cargo graph](https://github.com/kbknapp/cargo-graph)**.

Pour simplifier encore les choses, je me suis créé un petit script python :

    #!python
    import os
    import sys
    import subprocess
    import toml
    
    os.chdir(sys.argv[1])
    package_name = ''
    with open("Cargo.toml", "r") as conffile:
        config = toml.loads(conffile.read())
        package_name = config["package"]["name"]
    
    subprocess.call(
        "cargo graph --optional-line-style dashed --optional-line-color red"
        * " --optional-shape box --build-shape diamond"
        * " --build-color green --build-line-color orange"
        * " >| {0}.dot".format(package_name),
        shell=True
    )
    subprocess.call(
        "dot -Tpng > {0}.png {0}.dot".format(package_name),
        shell=True
    )

et dans mon **.zshrc** :

    #!sh
    graph () {
        CARGO_PACKAGE_PATH=$PWD;
        VIRTUAL_PATH="my_scripts"
        launchPythonScript "python3 ./cargo_graph.py $CARGO_PACKAGE_PATH"
    }

Du coup, en appelant mon utilitaire **graph**, je vais créer automatiquement à la source de mon projet, un fichier **projet.dot** et **projet.png** correspondant.
Le nom du projet est directement récupérer dans le Cargo.toml.


## bot Irc [Playbot](https://github.com/redox-os/playbot)

    #!rust
    playbot: std::mem::size_of::<bool>()

équivalent à :

    #!rust
    fn main() {
        println!("{:?}", std::mem::size_of::<bool>());
    }

## Exemples

http://dev.unhandledexpression.com/slides/devoxx-2016/

## Recherche de libs

https://docs.rs/
https://crates.io/

## Coverage

https://users.rust-lang.org/t/tutorial-how-to-collect-test-coverages-for-rust-project/650

https://github.com/hyperium/hyper/blob/master/.travis.yml

## Débuggage

Dans votre bashrc et/ou zshrc :

    #!sh
    export RUST_BACKTRACE=1

    #sh
    strace cargo run --bin projet

Rust fait beaucoup de vérifications au niveau de la compilation mais ne peut bien évidement pas couvrir la partie dynamique.
Il subsite donc des erreurs à l'exécution : pour les débusquer, **gdb** est notre ami.

    #!sh
    gdb target/debug/le_fichier_concerne
    (gdb) run

## Déploiement

    #!sh
    cargo build --release

https://github.com/mmstick/cargo-deb

## En vrac

http://rust.developpez.com/faq