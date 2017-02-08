Title: Que pensez de Swift ?
Category: misc
Tags: swift, rust
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: swift-langage
Authors: Jérémie Ferry
Status: published
Summary:

## 

### Philosophy

Rust is meant to be a safer C++. Rust is meant to be safe above all else.
Swift is meant to be a performant Python/Ruby. Swift is meant to be a programmer-centric and familiar coding experience.

### Concurrency

Rust uses a pretty conventional thread API
Swift uses "Grand Central Dispatch" code execution queues, code blocks, and thread pools to optimize performance and perform synchronization.

### Memory Management

Ownership and borrowing is the cornerstone concept for shared memory and concurrency in Rust.
Swift uses compile time ARC, which is like static compiler placed manual memory management. (pas vraiment un Garbage Collector mais un Automatic Reference Counting)
Both languages have means of unmanaged memory, and direct-use (but unsafe) pointers

### C code Compatibility

Swift is ABI compatible with C. So code can be intermixed with existing C or objC code base. This is unique to Swift.
REPL, Live coding & JIT

Swift has a live coding playground, REPL and can JIT in development before being compiled native.
