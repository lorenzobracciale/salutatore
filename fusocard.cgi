#!/bin/bash
IDCARDCMD="nfc-list |  awk '/UID/ {print \$3\$4\$5\$6;}'"
IDCARD=$(eval $IDCARDCMD)
echo "Content-type: application/javascript"
echo "Access-Control-Allow-Origin: *"
echo ""
echo "{ \"sn\": \"$IDCARD\" }"
