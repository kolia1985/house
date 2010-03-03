#!/usr/bin/env sh

lastversion=`git tag -l | egrep "^v[0-9]+\.[0-9]+\.[0-9]+" | cut -d"-" -f 1 | sed "s/^v//g" | sort | tail -n 1`
if [ -e $lastversion ]
then
 lastversion="0.0.0"
else
    tmpmajor=`git tag -l | egrep "^v[0-9]+\.[0-9]+\.[0-9]+" | sed "s/^v//g" | cut -d"." -f1 | sort -n | tail -n 1`
    tmpminor=`git tag -l | egrep "^v$tmpmajor\.[0-9]+\.[0-9]+" | sed "s/^v//g" | cut -d"." -f2 | sort -n | tail -n 1`
    tmpbuild=`git tag -l | egrep "^v$tmpmajor\.$tmpminor\.[0-9]+" | sed "s/^v//g" | cut -d"." -f3 | sort -n | tail -n 1`
    lastversion="$tmpmajor.$tmpminor.$tmpbuild"

fi

echo "v$lastversion"
