Title: Aide mémoire sur le réseau et l'admin sys
Category: Aide-memoire
Tags: linux, arp, nmap, admin sys
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: memo-admin-sys
Authors: Jérémie Ferry
Status: published
Summary:

# Intro

Autant le dire, je suis une bille en réseau mais je fais tout pour m'améliorer.
Voici quelques astuces que j'ai glané.

## w

Donne la liste des utilisateurs sur une machine

## arp -a

Renvoie que la liste des adresses déjà inscrites dans la table ARP.

## nmap

    #!bash
    nmap -sP 192.168.0.*
    sudo nmap -sP x.y.z.*

[http://blog.nicolargo.com/2007/08/nmap-le-scanneur-de-reseau.html](http://blog.nicolargo.com/2007/08/nmap-le-scanneur-de-reseau.html)

## lsof -i

## Obtenir la liste de ses adresses IP locales

LANG=c ifconfig | grep -B1 "inet addr" |awk '{ if ( $1 == "inet" ) { print $2 } else if ( $2 == "Link" ) { printf "%s:" ,$1 } }' |awk -F: '{ print $1 ": " $3 }'

## Donner son adresse IP publique

curl ipinfo.io/ip

## Saisir une IPv6 dans son navigateur

La mettre entre crochet => [la::super::ip::v6]

## donner le nom de domaine d'un poste sur le réseau locale

hostname

## changer le hostname

sudo hostname TRUCMUCH



