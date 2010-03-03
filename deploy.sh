#!/bin/sh
proj=$1

INST=/usr/local/lib/staging/roa/roa
SITE=/usr/local/lib/staging/roa/site-packages
DB=roa
DJANGO=roa
BASE=`dirname $INST`

mysqldump $DB | bzip2 > $DB.`date +%F-%R`.sql.bz2

tar xjf $proj.tar.bz2 -C $BASE || (echo Failed to untar; exit $1)

[ -h $INST ] && rm $INST && ln -s $BASE/$proj $INST

cp $INST/$DJANGO/settings_local.py.staging $INST/$DJANGO/settings_local.py
cp $INST/Makefile.def.staging $INST/Makefile.def
