Title: Tester c'est douter
Category: misc
Tags: test
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: tester-c-douter
Authors: Jérémie Ferry
Status: published
Summary:

## Tester c'est douter

Dans le paysage du développeur, les tests **automatisés** devraient être obligatoire et non plus une exception.

La réalité est souvent tout autre...

## Isolation

Le meilleur moyen de tester est d'isoler son application dans une image virtuel, un container etc.
On évite principalement les soucis liés aux dépendances.

## Couverture

Sauf contraintes techniques, il est nécessaire de couvrir avec des tests l'ensemble de l'applicatif : les zones les plus sensibles en premier, bien évidement.

## Logging et traces

Usage intensif de **Sentry**

## Tests pour le Web

### tests de monté en charge (Smoke testing) et performance (Load testing)

https://fr.wikipedia.org/wiki/Test_de_performance

* Apache bench
* Boom : https://github.com/tarekziade/boom
* Locust : https://github.com/locustio/locust
* Molotov : http://molotov.readthedocs.io/en/latest/
