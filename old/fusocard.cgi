#!/bin/bash
IDCARDCMD="nfc-list |  awk '/UID/ {print \$3\$4\$5\$6;}'"

IDCARD=""
i=0
while [ -z $IDCARD ] && [ $i -lt 3 ]; do
               IDCARD=$(eval $IDCARDCMD)
               ((i++))
done

echo "Content-type: application/javascript"
echo "Access-Control-Allow-Origin: *"
echo ""
echo "{ \"sn\": \"$IDCARD\" }"
