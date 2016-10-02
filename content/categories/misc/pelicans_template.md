Title: Pelican's Template
Category: Misc
Tags: template
Date: 2016-02-14 00:01
Modified: 2016-09-24 22:45
Slug: pelicans-template
Authors: Jérémie Ferry
Status: published
Summary:

## Title 2

### Title 3

#### Title 4

##### Title 5

###### Title 6

**strong text** + *italic text*

[http://blog.getpelican.com](http://blog.getpelican.com)

[link to pelican's doc](http://docs.getpelican.com)

[link to pelican's doc with a target _blank](http://docs.getpelican.com){:target="_blank"}

[link to pelican's doc with title](http://docs.getpelican.com "read pelican's doc")

Keyboard shortcuts : <kbd>Alt</kbd><kbd>Q</kbd>

## Lists

* 1
* 2
* 3
    * 3.1
    * 3.2
        * 3.2.1
        * 3.2.2
    * 3.3
* 4

## Bash code

    #!bash
    cat file | wc

## Python code

    #!python
    def fib(n):
        a, b = 0, 1
        while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
    fib(1000)

## Picture
![tmuxp load](static/images/tmuxp_load_labodunerd.png)

## Movie
{% video ./static/movies/camp_paleolithic.mp4 100% 100% /./static/images/camp_paleolithic.jpg %}