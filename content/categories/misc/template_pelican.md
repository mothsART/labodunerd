Title: Pelican's Template
Category: Misc
Tags: pelican
Date: 2016-02-14 00:00
Modified: 2016-02-14 00:00
Slug: pelicans-template
Authors: Jérémie Ferry
Summary:

# Title1

## Title2

### Title3

#### Title4

##### Title5

###### Title 6

**strong text** + *italic text*

[http://blog.getpelican.com](http://blog.getpelican.com)

[link to pelican's doc](http://docs.getpelican.com)

[link to pelican's doc with title](http://docs.getpelican.com "read pelican's doc")

Keyboard shortcuts : <kbd>Alt</kbd><kbd>Q</kbd>

* 1
* 2
* 3
    * 3.1
    * 3.2

# Code Bash

    #!bash
    cat file | wc

# Code Python

    #!python
    def fib(n):
        a, b = 0, 1
        while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
    fib(1000)
