#!/bin/tcsh

set table = SNFAKE
set schema      = marcelle
set fakeversion = KBOMAG20NGC1433
set idoffset    = 10000000

awk '($1>0)&&($1<360){printf "%s,-1,-20,%s,20,0,%s,%s,0,NULL,0\n","'${idoffset}'"+NR,"'${fakeversion}'",$1,$2}' mag20.radec > mag20.csv

set ctl = mag20.ctl
echo "load data" > $ctl
echo "  infile mag20.csv" >> $ctl
echo "  append" >> $ctl
echo "  into table "${schema}"."${table} >> $ctl
echo "  fields terminated by ',' " >> $ctl
echo "  (ID,SNANAID,GALID,VERSION,INDNONIA,Z,RA,DEC,PEAKMJD,FIELD,HOST_ANGSEP)" >> $ctl

sqlldr marcelle/mar70chips@leovip148.ncsa.uiuc.edu/destest control='mag20.ctl' discard=0 skip=0 log='mag20.log'
