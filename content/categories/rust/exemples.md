Title: Des exemples Rust
Category: rust
Tags: rust
Date: 2016-12-11 00:00
Slug: exemples-rust
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

Des exemples de code Rust que je réutilise (mais que je n'arrive pas à mémoriser)

## Enum récursif

    #!rust
    #[derive(Debug)]
    enum A {
        G(i32),
        H(Vec<A>),
    }
    
    fn main() {
        let a1: A = A::G(2);
        let a2: A = A::G(3);
        let a3: A = A::H(vec![a1, a2]);
        println!("{:?}", a3);
    }

## BTreeMap

    #!rust
    use std::collections::BTreeMap;
    
    #[derive(Debug)]
    enum A {
        G(i32),
        H(Vec<A>),
        I(BTreeMap<i32, A>),
    }
    
    fn main() {
        let ah = A::H(vec![A::G(2), A::G(3)]);
        
        let mut map = BTreeMap::new();
        map.insert(1, A::G(20));
        map.insert(1, A::H(vec![A::G(10), A::G(20)]));
        
        let ai = A::I(map);
        println!("{:?}", ah);
        println!("{:?}", ai);
    }

## Passer de str à String et inversement

### str à string

    #!rust
    let machaine_str:&'static str = "ma chaine";
    let machaine_string:String = machaine_str.to_owned();

ou

    #!rust
    let machaine_str:&'static str = "ma chaine";
    let machaine_string:String = machaine_str.to_string();

### String to str

    #!rust
    let manouvellechaine_str:&str = &*machaine_string;

Des traits pour de la programmation générique :
https://github.com/apasel422/eclectic

des websockets :

https://github.com/housleyjk/ws-rs