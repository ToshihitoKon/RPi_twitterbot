#/usr/bin/zsh

export LANG=en_US.UTF-8
dir='~/twitter'
date=`date`
who=`whoami`
cd ${dir}
temp=`./adt7410.py`
ret=`./tweet.py "${date}
現在の気温:${temp}度"` 
echo "${0}:${date}:${who}:${ret}" >> log.txt
