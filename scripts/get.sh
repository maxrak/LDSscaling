#!/bin/bash
if test -z "$1" 
then
      CONF="1WPmedium_1DB"
else
      CONF=$1
fi
TARGET="http://193.206.108.215/output/results_Concurrent_User/results_"$CONF"/"
DATA="data/"$CONF"/"
wget -P $DATA $TARGET
cat $DATA/index.html |grep href | awk '{print $5}'|awk -F"\"" '{print $2}' | while read line 
do
  l=${line%/}	
  name=$(sed 's/[-].*//' <<< $line)
  echo $name
  ref=""$TARGET"/"$line"/js/global_stats.json"
  wget -P data $ref
  target="mv data/global_stats.json "$DATA"/stat_"$name
  eval $target
done

#	wget -P data/ http://193.206.108.215/output/results_Concurrent_User/results_1WPmedium_1DB/author0500concurrentusers-20191216163238334/js/global_stats.json
