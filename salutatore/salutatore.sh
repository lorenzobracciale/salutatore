#!/bin/ash

SERVER=soci.fusolab.net
WGET=/usr/bin/wget
NFC_LIST=/usr/bin/nfc-list
PLAY=/usr/bin/madplay
USER_ID=""
GREETING_FILE="/tmp/playingnow.mp3"
DOWNLOAD_IN_PROGRESS="/tmp/stopplay"
BEEP_FILE="/root/beep.mp3"

play_beep_or_greeting() {
	while [ 1 ]; do
		if [ -e $DOWNLOAD_IN_PROGRESS ]; then
			echo 'madplay beep.mp3'
			$PLAY $BEEP_FILE 
		else
		        echo "madplay playingnow.mp3"
		        $PLAY $GREETING_FILE 
		        rm $GREETING_FILE
		        return
		fi
	    sleep 1
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
		touch $DOWNLOAD_IN_PROGRESS
		#start beeeping
		play_beep_or_greeting &
	        echo $WGET http://$SERVER/salutatore/$IDCARD/ -O $GREETING_FILE
	        $WGET http://$SERVER/salutatore/$IDCARD/ -O $GREETING_FILE
	        rm $DOWNLOAD_IN_PROGRESS
	        while [ -e $GREETING_FILE ]; do
	        	sleep 3;
	        done
	fi
		
	sleep 3;

done
 



