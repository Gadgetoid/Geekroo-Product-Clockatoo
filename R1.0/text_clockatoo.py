#!/usr/bin/python

from datetime import timedelta

# ===========================================================================
# Clockatoo - Text Example
# ===========================================================================
with open('/proc/uptime', 'r') as f:
	uptime_seconds = float(f.readline().split()[0])
	uptime_string = str(timedelta(seconds = uptime_seconds))

from Raspi_7Segment import SevenSegment
segment = SevenSegment(address=0x70)
segment.writeTextString('hello world',0.2)
segment.writeTextString('uptime ' + uptime_string,0.2)
