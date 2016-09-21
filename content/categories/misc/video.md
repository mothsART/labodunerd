Title: videos
Category: misc
Tags: linux, ffmpeg, mencoder
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: videos
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

## ffmpeg

ffmpeg -framerate 1/1 -i camp%3d.png -c:v libx264 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p out.mp4 | ffmpeg -i out.mp4 etape.gif

## Mencoder

mencoder -oac mp3lame -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -vf flip,mirror premier_toboggan.MOV -o premier_toboggan.avi

mencoder -vf flip,mirror premier_toboggan.MOV -o premier_toboggan.avi

mencoder -oac mp3lame -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -vf flip,mirror premier_toboggan.MOV -lavdopts threads=4 -o premier_toboggan.avi

### convertir le son en mp3 + retourner la vidéo + traitement sur 4 threads

mencoder -oac mp3lame -ovc x264 -vf flip,mirror premier_toboggan.MOV -lavdopts threads=4 -o premier_toboggan.avi

## Liens

http://sebsauvage.net/wiki/doku.php?id=ffmpeg

