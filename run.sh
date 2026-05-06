#!/bin/sh
# Runs zzz and starts logging. Ctrl-C to exit.

if [ ! -f /home/pi/zzz/zzz.py ]; then
  echo "Not in default Pi directory. Modify run.sh for development."
else
  nohup /usr/bin/python3 -u /home/pi/zzz/zzz.py > /home/pi/zzz/sleep.log 2>&1 &
fi
