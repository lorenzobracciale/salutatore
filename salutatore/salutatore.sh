#!/bin/ash

SERVER=10.172.0.13
WGET=/usr/bin/wget
USER_ID=""
BEEP_STOPPER="/tmp/stopthebeep"

nfc_list() {
	#TODO: Call the real nfc_list, perhaps in a while loop?
	echo "garbage"
	echo "garbage"
	echo "       UID (NFCID1): 6d  44  a5  29  "
	echo "garbage"
	echo "garbage"
}

play_beep() {
	# play beep in background if /tmp/stopthebeep is not present
	while [ 1 ]; do
		if [ ! -e $BEEP_STOPPER ]; then
			echo 'madplay beep.mp3'
		fi
		sleep 1;
	done
}

touch $BEEP_STOPPER
play_beep &

while [ 1 ]; do

	IDCARD=""
	i=0
	while [ -z $IDCARD ] && [ $i -lt 3 ]; do
	        IDCARD=$(nfc_list | grep UID | awk -F ":" '{print $2}' | awk '{print $1$2$3$4}')
	        let i=i+1
	done

	if [ ! -z $IDCARD ]; then
		rm -f $BEEP_STOPPER
	        echo $WGET http://$SERVER/salutatore/$IDCARD -O playingnow.wav
	        sleep 3 #XXX: DELETE ME
		touch $BEEP_STOPPER
	        echo madplay playingnow.wav
	fi
	
	sleep 3;

done
 



