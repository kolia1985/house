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
lastmajor=`echo $lastversion | cut -d"." -f 1`
lastminor=`echo $lastversion | cut -d"." -f 2`
lastbuild=`echo $lastversion | cut -d"." -f 3`

newmajor=$lastmajor
newminor=$lastminor
newbuild=$lastbuild

case $1 in
    major)
        newmajor=`echo "$lastmajor + 1" | bc`
        newminor="0"
        newbuild="0"
    ;;
    minor)
        newminor=`echo "$lastminor + 1" | bc`
        newbuild="0"
    ;;
    build)
        newbuild=`echo "$lastbuild + 1" | bc`
    ;;
    *)
        echo "Usage: $0 major|minor|build"
        exit 1
    ;;
esac

newversion="v$newmajor.$newminor.$newbuild"
echo "$newversion"

git tag -a -m "auto-tag $newversion" $newversion || exit 1

git push --tags origin $newversion
