Title: Macros rust
Category: rust
Tags: rust
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: macros-rust
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

### println!

    #!rust
    use std::fs::File;
    
    fn main() {
        let x = File::open("nop");
        println!("{:?}", x);
        println!("");
        println!("{:#?}", x);
    }

format!

write!

try!

undefined!

assert!

assert_eq!

panic!

unreachable!

unimplemented!

column!

line!

file!

vec!

log_syntax!

trace_macros!