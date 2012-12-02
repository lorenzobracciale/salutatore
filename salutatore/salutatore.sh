#!/bin/ash

SERVER=soci.fusolab.net
WGET=/usr/bin/wget
NFC_LIST=/usr/bin/nfc-list
PLAY=/opt/usr/bin/madplay
USER_ID=""
BEEP_STOPPER="/tmp/stopthebeep"
GREETING_FILE="playingnow.mp3"
PLAYED=""

play_beep_or_greeting() {
	while [ 1 ]; do
		if [ ! -e $GREETING_FILE ]; then
			echo 'madplay beep.mp3'
			$PLAY beep.mp3
		else
		        echo "madplay playingnow.mp3"
		        $PLAY $GREETING_FILE 
		        rm $GREETING_FILE
		        return
		fi
		sleep 3;
	done
}


while [ 1 ]; do

	IDCARD=""
	while [ -z $IDCARD ] ; do
		echo "Try reading card..."
	        IDCARD=$($NFC_LIST | grep UID | awk -F ":" '{print $2}' | awk '{print $1$2$3$4}')
	done
	
	echo "card read: " $IDCARD

	if [ ! -z $IDCARD ]; then
		PLAYED=""
		echo "launching play beep and greets"
		play_beep_or_greeting &
		echo "done"
		#start beeeping
	        echo $WGET http://$SERVER/salutatore/$IDCARD/ -O $GREETING_FILE
	        $WGET http://$SERVER/salutatore/$IDCARD/ -O $GREETING_FILE
	        while [ -e $GREETING_FILE ]; do
	        	sleep 3;
	        done
	fi
		
	sleep 3;

done
 



