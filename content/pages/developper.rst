Developpeurs
============

:date: 2016-09-23 10:20
:tags: developper, developpeur
:slug: developpeurs
:authors: Ferry Jérémie
:summary: Venez améliorer LinkManager

LinkManager est pour l'instant le fruit d'un développeur qui le peaufine sur son temps libre.
Il n'est par conséquent pas adapté à tous les usages et nécessite d'être améliorer.

Le dépôt du projet est présent sur : https://github.com/mothsART/linkmanager

Vous pouvez donc le forker facilement.

Virtualenv
----------

Pour le développement, il est fortement conseillé d'utiliser virtualenv et virtualenvwrapper.
Vous travaillerez, par conséquent, dans un environnement isolé.

.. code-block:: bash

    mkvirtualenv -p /usr/bin/python3 linkmanager

Git
---

Un bon usage est de passer par git-flow.

Une branch master pour la version actuellement disponible (stable)
Une branch develop pour la version à venir (unstable)

Des tags pour les versions majeurs publiés (v0.2, v0.4 etc.)

Pour améliorer la qualité du code : il est également vivement conseillé d'utiliser des Hooks Git (flake8 par exemple).

Lib
---

- flake8 : du PEP8 + Pyflakes (assurance qualité en python)

- argcomplete : programme cli d'auto-complétion
- clint : lib d'amélioration de la ligne de commande ()

- arrow : meilleur lib pour manipuler de dates/heures
- path.py : manipuler des chemins facilement

- Flask : Framework web minimaliste permettant de lancer LM en mode serveur web
- Flask-Assets : les ressources (css, js) sont compressés et inlinés (une requête)

- pytest : de meilleurs tests unitaires que *doctests* ou *unittest*
- pytest-cov + coverage : couverture de tests
- invoke : permet d'automatiser des tâches (digne remplaçant de *fabric*)
- fakeredis : utilisation de Redis sous forme de Mock (objets simulés)
- tox : lancer les tests sur plusieurs versions de Python

- requests : API simple pour faire des requêtes
- requests-futures : permet d'étendre **requests** pour qu'il soit asynchrone
- beautifulsoup4 : API d'utilisation de HTML


Unit Test + Coverage
--------------------

Dès le démarrage du projet, l'auteur a désiré l'orienté sur de l'intégration continue.
Des tests unitaires pour l'api ont été développé ainsi que des test fonctionnels (scénarios d'usage).
Pour éviter des zones non couvertes (donc potentiellement bugés), une couverture du code est également assuré.


Pour lancer la couverture de test, il suffit de lancer

.. code-block:: bash

    invoke test

et si on veut lancer un fichier de test en particulier :

.. code-block:: bash

    python -m pytest linkmanager/tests/db.py

Afin de garantir le portage sur plusieurs version de python, on utilise Tox.
Sur Github, Travis (via un fichier .travis.yml) assure qu'une version passe bien l'ensemble des tests unitaires.

Deploiement
-----------

Avant tout déploiement, il faut changer de version.
Pour éviter de changer plusieurs fichiers et potentientiellement se tromper dans la manip, j'ai développé une petite tâche.

Donner sa version actuelle

.. code-block:: bash

    invoke version

Changer de version (ici : passage à la 1.0.1)

.. code-block:: bash

    invoke version -e=1.0.1

- Sur Pypi

    Enregistrer une version sur Pypi :

    .. code-block:: bash

        python setup.py register -r pypi

    Mettre en ligne une nouvelle version :

    .. code-block:: bash

        python setup.py sdist upload -r pypi

    Tester sur serveur Pypi de test :

    .. code-block:: bash

        python setup.py sdist upload -r test # (http://peterdowns.com/posts/first-time-with-pypi.html)

    Installation d'une version de test :

    .. code-block:: bash

        sudo pip3 install -i https://testpypi.python.org/pypi linkmanager


- Sur PPA

    .. code-block:: bash

        dch -a

        dch -i --create
        dh_make --createorig
        debuild -S
        dput ppa:jerem-ferry/linkmanager linkmanager_0.1_source.changes

    Installer sur PPA :

    .. code-block:: bash

        dput ppa:jerem-ferry/link-manager


Benchmarks
----------

En cours.
Pour assurer un bench optimal, il me semble nécessaire d'utiliser une machine virtuel avec un cadre définit (RAM/CPU/IO)
Vagrant ou Docker?

Les éléments à tester :

- lib json vs simplejson
- Redis vs MongoDB

Pour tester le serveur :

- Boom (https://github.com/tarekziade/boom) :

  .. code-block:: bash

      boom http://localhost:8080 -c 100 -n 100

Docker
------

Afin de garantir un bon fonctionnement de LinkManager, j'ai décidé d'utiliser ce manifique outil qu'est "Docker".
Ca m'a permis d'automatiser les règles d'installation et de me garantir le bon fonctionnement dans un environnement vierge.
(gestion des dépendances etc.)

Pour les retours de bugs, c'est idéal : on peut se mettre dans les mêmes conditions.

Afin de partager à tous mes DockerFiles, j'ai créé un dépôt Github dédié :

https://github.com/mothsART/linkmanager_docker

Suivi du projet
---------------

http://forum.ubuntu-fr.org/viewtopic.php?id=1552011
