Title: Installation de ma Raspberry-PI avec Raspbian
Category: raspberry
Tags: raspberry, linux, shell, raspbian
Date: 2016-06-23 21:50
Slug: installation-raspberry-raspbian
Authors: Jérémie Ferry
Status: draft
Summary:

## Intro

Voici ma procédure pour installer **Raspbian** sur une **Raspberry PI v2**
(ARM v7)

Je me suis inspiré de https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

### download

On va sur https://downloads.raspberrypi.org/raspbian/images/
et on choisit la dernière :

curl -O https://downloads.raspberrypi.org/raspbian/images/raspbian-2016-05-31/2016-05-27-raspbian-jessie.zip
curl -O https://downloads.raspberrypi.org/raspbian/images/raspbian-2016-05-31/2016-05-27-raspbian-jessie.zip.sha1

sha1sum -c 2016-05-27-raspbian-jessie.zip.sha1
