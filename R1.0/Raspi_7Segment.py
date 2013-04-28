#!/usr/bin/python

import time
import datetime
from Raspi_LED import LED

# ===========================================================================
# 7-Segment Display
# ===========================================================================

class SevenSegment:
  disp = None

  # Hexadecimal character lookup table (row 1 = 0..9, row 2 = A..F)
  digits = [ 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, \
             0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71 ]

  # Basic text lookup table ( a-z, -, _ space, 0-9 ), lowercase only
  letters = { 'a':0x77, 'b':0x7c, 'c':0x39, 'd':0x5e, 'e':0x79, 'f':0x71, \
              'g':0x3d, 'h':0x74, 'i':0x06, 'j':0x1e, 'k':0x76, 'l':0x38, \
              'm':0x15, 'n':0x54, 'o':0x5c, 'p':0x73, 'q':0x67, 'r':0x31, \
              's':0x6d, 't':0x78, 'u':0x3e, 'v':0x1c, 'w':0x2a, 'x':0x76, \
              'y':0x66, 'z':0x5b, '0':0x3f, '1':0x30, '2':0x5b, '3':0x4f, \
              '4':0x66, '5':0x6d, '6':0x7d, '7':0x07, '8':0x7f, '9':0x6f, \
              ' ':0x00, '-':0x40, '_':0x08 }

  # Constructor
  def __init__(self, address=0x70, debug=False):
    if (debug):
      print "Initializing a new instance of LED at 0x%02X" % address
    self.disp = LED(address=address, debug=debug)

  def writeTextString(self, string, speed=0.5):
    string = '    ' + string.lower() + '    '
    buf = []
    disp = []
    for c in string:
      if c in self.letters:
        buf.append(self.letters[c])
      else:
        continue

      if(len(buf) > 3):
        disp = buf[-4:]     

      if (len(disp) > 0):
        self.writeDigitRaw(0,disp[0])
      if (len(disp) > 1):
        self.writeDigitRaw(1,disp[1])
      if (len(disp) > 2):
        self.writeDigitRaw(3,disp[2])
      if (len(disp) > 3):
        self.writeDigitRaw(4,disp[3])
      time.sleep(speed)

  def writeDigitRaw(self, charNumber, value):
    "Sets a digit using the raw 16-bit value"
    if (charNumber > 7):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, value)

  def writeDigit(self, charNumber, value, dot=False):
    "Sets a single decimal or hexademical value (0..9 and A..F)"
    if (charNumber > 7):
      return
    if (value > 0xF):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, self.digits[value] | (dot << 7))

  def setColon(self, state=True):
    "Enables or disables the colon character"
    # Warning: This function assumes that the colon is character '2',
    # which is the case on 4 char displays, but may need to be modified
    # if another display type is used
    if (state):
      self.disp.setBufferRow(2, 0xFFFF)
    else:
      self.disp.setBufferRow(2, 0)

