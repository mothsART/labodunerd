Title: le todo du developpeur
Tags: dev_todo
Date: 2016-04-24 11:30
Modified: 2016-04-24 11:30
Authors: Jérémie Ferry
Status: draft

## Lister mes softs/scripts

* lso : ls -la amélioré -> En Rust
*

* tmuxp amélioré

## à réaliser

* des extensions à django-cms

==========================================


* NOTIFICATIONS
	* dunst

* Music Player
	* ncmpcpp

* Gestionnaire de mot de passe :
    * keeppassx en cli : kpcli (http://sourceforge.net/projects/kpcli/)

* [mountavfs]:
    // examples :
    // tree archive.zip#/
    // cat archive.zip#/dir/dir/file.txt
    * use auto-completion on a path in archive (like cat)

* give GIS on ip:
    * curl ipinfo.io/173.194.40.87
    * use a python interface

* python traceback colorize with "Pygments"!!!!

* use RetroShare : http://fr.wikipedia.org/wiki/RetroShare

* LDAP

* use Node.js and NPM on Virtualenv
===================================
http://lincolnloop.com/blog/

$ curl http://nodejs.org/dist/node-latest.tar.gz | tar xvz
$ cd node-v*
$ ./configure --prefix=$VIRTUAL_ENV
$ make install


* http://linuxfr.org/users/xfennec/journaux/cv-un-petit-outil-pour-surveiller-vos-copies

* Pragma : http://www.fsd.it/fonts/pragmatapro.htm#.UpxlvbXuJsl && http://www.indiegogo.com/projects/pragmatapro-the-ideal-programming-typeface-open-source

* [script: web_search] :
    * list all categories (!bang) on a python -> better: use a redis database
        * use it on auto-completion
        * and update list. (cron : 1 per month)

* my "conky" (replace with a QT app?!)
    * cpus, ram, swp, download, file transferts, decompression (ie : big zip file)
	http://www.mumbly58.fr/wp-content/uploads/2013/12/Capture-d%C3%A9cran-11122013-200950.png
    * cron task (like backup)
    * birthday's
    * webservices

* Add an interactive rebase GUI with drag + drop editing (Ncurse + QT4 + web) : see git-cola

* use a syslog serveur and a generic "syslog conf" to all my parc.

* use jabber on cli : poezio or EMACS extension...

[Blender] :
    * SVG output (http://blenderartists.org/forum/showthread.php?282824-SVG-output-script : python script)

[facebook <iframe>] : http://monprojetpourdieu.com/

[Give] :
    * without argument, list all my yaml files + auto-completion on list
    * use python file instead of yaml? or BDD like Redis?
    * "give crawl" : search a new file.
    * git commit on "coffre_open" use a git hook than launch "give crawl"...

[weboob] : using table like my postgresql conf
[commande "lso"] : using table like my postgresql conf

[Fabric] :
    * deploy file :
        * init timezone : http://sametmax.com/changer-la-timezone-sous-ubuntu-server-en-ligne-de-commande/
    * use a cron script on my server to :
        * update minor lib version on all projects
        * save old requirements.txt on my server + on the project
        (example : requirements/requirements_2013-23-11 ($ date +%d-%m-%y) or in a compression file : xz (LZMA2 with) or 	 LZMA)
    * give an API to chow changes.
    * Cron on my Desktop my server changes.
    * give a list of outdated packages on my projects (can be a good choice to basculate on a greater version)

[Django] : middleware for Pyscss : no using on production...

[virtualenv] launch a tmux :
http://lincolnloop.com/blog/tmux-stay-focused/
    * 1 window + 2 panels : ./manage.py + livereload
    * 1 window : ssh connection
    * 1 window : mc connection

[livereload] :
    * save diff when i edit on chrome...
    * colorized
    * change apparence of date...

[Backup]:
    * using "Brebis"

* use git-flow + zsh completion (http://superuser.com/questions/623831/how-to-get-git-flow-completions-for-zsh-working)
* use git-extras = https://github.com/visionmedia/git-extras

