INST=/usr/local/lib/staging/roa/roa/roa
SITE=/usr/local/lib/staging/roa/roa/lib
SITEPACK=/usr/local/lib/staging/roa/site-packages

export PYTHONPATH=$INST:$SITE:$SITEPACK

log=""
child="minspare=1 maxspare=2 maxchildren=3"
params="protocol=fcgi umask=002 maxrequests=1000 $child $log --settings=settings"

sock=/tmp/roa.sock  # I don't feel this is correct location
pid=/tmp/roa.pid
PID1=`cat $pid`
kill $PID1
python $INST/manage.py runfcgi socket=$sock pidfile=$pid $params \
  && chmod go+w $sock
