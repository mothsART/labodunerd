Title: RecalBox
Category: raspberry
Tags: raspberry, recalbox, retro-gamming
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: recalbox
Authors: Jérémie Ferry
Status: published
Summary:

## Memo RecalBox

Utilisez le nom d'utilisateur **root** et le mot de passe **recalboxroot**

**\\RECALBOX** ou **\\192.168.1.30**

### SSH

Tapez : **ssh root@recalbox.local**

ou **arp -a** (donne la liste des ordis sur le réseau locale)
puis 
ou  **ssh root@monIp**


## Activer le Wifi 

aller au fichier **/recalbox/share/system/recalbox.conf** :

    #!sh
    ## Activate wifi (0,1)
    wifi.enabled=1
    ## Wifi SSID (string)
    wifi.ssid=maFreeBox
    ## Wifi KEY (string)
    ## Escape your special chars (# ; $ -) with a backslash : $ => \$
    wifi.key=motMonDePasseFreebox

Et surtout ne pas utiliser le canal 13 pour le wifi
