#!/bin/bash
if test -z "$1" 
then
      CONF="1WPmedium_1DB"
else
      CONF=$1
fi
for profile in author editor shopmanager userreader
do
	for cuser in 0020 0040 0060 0080 0100 0120 0140 0160 0180 0200 0220 0240 0260 0280 0300 0320 0340 0360 0380 0400 0420 0440 0460  0480 0500
	do
		filename="data/"$CONF"/stat_"$profile""$cuser"concurrentusers"
		if [ -f $filename ]; then
			ratecmd="jp -f \"data/\"$CONF\"/stat_\"$profile\"\"$cuser\"concurrentusers\" meanNumberOfRequestsPerSecond.total" 
			RTcmd="jp -f \"data/\"$CONF\"/stat_\"$profile\"\"$cuser\"concurrentusers\" meanResponseTime.ok" 
			Nrcmd="jp -f \"data/\"$CONF\"/stat_\"$profile\"\"$cuser\"concurrentusers\" numberOfRequests.total"
			KOcmd="jp -f \"data/\"$CONF\"/stat_\"$profile\"\"$cuser\"concurrentusers\" numberOfRequests.ko"
			StdDevcmd="jp -f \"data/\"$CONF\"/stat_\"$profile\"\"$cuser\"concurrentusers\" standardDeviation.ok"
			rate=$(eval $ratecmd)
			RT=$(eval $RTcmd)
			Nr=$(eval $Nrcmd)
			KO=$(eval $KOcmd)
			Percmd="bc -l <<< \"100*$KO/$Nr\" "
			Per=$(eval $Percmd)
			StdDev=$(eval $StdDevcmd)
			OUTcmd="echo $CONF , $profile , $cuser , $rate , $RT , $KO , $Nr , $Per , $StdDev >>data/stats.csv"
			eval $OUTcmd
		else 
			echo "Missing file "$filename
		fi
	done
done
