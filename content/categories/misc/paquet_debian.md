Title: Créer des paquets Debian
Category: misc
Tags: debian, linux
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: creer-paquet-deian
Authors: Jérémie Ferry
Status: published
Summary:

## 

Autoriser la signature d'un paquet GPG

gpg --no-default-keyring -a --export 7929777B | gpg --no-default-keyring --keyring ~/.gnupg/trustedkeys.gpg --import -