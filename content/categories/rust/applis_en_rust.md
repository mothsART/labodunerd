Title: Applis en Rust
Category: rust
Tags: 
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: applis-rust
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Le langage Rust : c'est encore un truc qui sert à rien ?!

Ben non, y'a plein de libs qui l'utilisent !

Des libs peut-être mais des vrais soft derrières ?

## Des softs en Rust

- **[Servo](https://github.com/servo/servo)**

- **RedOS** : un OS en Rust : [RedOs](https://www.redox-os.org/)

- **RipGrep** : un remplacement de Grep (avec des perfs halucinantes) :
[https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

- **Exa** : un remplacement de la commande **ls** mais en mieux :
[https://the.exa.website](https://the.exa.website)

- **Fd** : un digne remplaçant de la commande **find** :
[https://github.com/sharkdp/fd](https://github.com/sharkdp/fd)

- **Bat** : un remplaçant de **cat** proposant la coloration synthaxique et l'intégration de Git :
[https://github.com/sharkdp/bat](https://github.com/sharkdp/bat)

- **Hyperfine** : un remplaçant de **time** :
[https://github.com/mothsART/hyperfine](https://github.com/mothsART/hyperfine)

- **SVGCleaner** : minifier du svg :
[https://github.com/RazrFalcon/svgcleaner](https://github.com/RazrFalcon/svgcleaner)

- **Basic-http-server** : remplace **python -m http.server** (cargo install basic-http-server) :
[https://github.com/brson/basic-http-server](https://github.com/brson/basic-http-server)

- [Snatch](https://github.com/derniercri/snatch)

- **Alactritty** : est un terminal récent qui utilise le processeur graphique (via OpenGL).
C’est probablement le terminal le plus performant aujourd’hui.
En revanche, il ne couvre encore que peu de fonctionnalités (pas encore d’historique, par exemple).
[Alactritty](https://github.com/jwilm/alacritty)

- **Sozu** : Un reverse proxy qui est reconfigurable à chaud, qui est rapide et sécurisé. (sans aucun crash)

[Sozu](https://www.sozu.io/)


## Installation sous Ubuntu ou Debian

Pour simplifier l'utilisation de plusieurs de ces softs, j'ai décidé de les précompiler, les empaqueter et les mettre à dispo sur un PPA :

enjoy : [https://launchpad.net/~jerem-ferry/+archive/ubuntu/rust](https://launchpad.net/~jerem-ferry/+archive/ubuntu/rust)

Si vous désirez savoir comment je m'y suis pris, vous trouverez le détail ici : [https://forum.ubuntu-fr.org/viewtopic.php?id=2023943](https://forum.ubuntu-fr.org/viewtopic.php?id=2023943)
