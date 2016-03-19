Title: Encodage
Category: 
Tags: 
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: 
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

L'encodage fait parti de la culture du développeur.
Comme souvent, elle s'impose à lui : c'est quand il est confronté à des soucis d'encodage qu'il doit l'affronter.

Une fois confronté à ce type de problématique, il a besoin d'avoir les outils appropriés. En voici quelques un.

## BOM

Test si un fichier est en **UT-8 BOM** (courant sur windows pour distinguer que le fichier est bien encodé en UTF-8 et non pas en ISO-* ou Windows-1252)  :

    #!sh
    function has_bom {
        "Test if a file has an UT8 BOM (byte order mark)"
        echo $1;
        # echo `head -c 3 $1 | hexdump -C`;
        has=`head -c3 "$1" | grep -q $'\xef\xbb\xbf'`;
        if [ $? -gt 0 ]; then
            echo "no (error code -> $?)";
        else
            echo "yes (error code -> $?)";
        fi
    }

Lister les fichiers en **UT-8 BOM** (récursivement) :

    #!sh
    function bom_files {
        "List files on a tree with an UT8 BOM (byte order mark)"
        find . -type f -print0 | xargs -0 awk '/^\xEF\xBB\xBF/ {print FILENAME} {nextfile}';
    }