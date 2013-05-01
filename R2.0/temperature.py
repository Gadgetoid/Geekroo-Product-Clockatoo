#!/usr/bin/python

from datetime import timedelta
from Raspi_7Segment import SevenSegment

# ===========================================================================
# Clockatoo - 1-Wire Temp
# ===========================================================================
seg = SevenSegment(address=0x70)

print "Press CTRL+Z to exit"

while(True):
  with open(filename) as f:
    temp = f.read('/mnt/1wire/28.0139C4030000/temperature').strip()

  seg.writeTextString('room temp is ' + temp,0.2)

  time.sleep(30)
