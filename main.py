from pico_i2c_lcd import I2cLcd
from machine import Pin, I2C
import time
import random
#component setup
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
#lcd setup
I2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
lcd = I2cLcd(I2c, 0X27, 2, 16)
while True:
  lcd.clear()
  lcd.putstr("get ready")
  wait_time = random.uniform(0,8)
  time.sleep(wait_time)
  led.value(1)
  start = time.ticks_ms()
  while button.value() == 0:
    pass
  reaction = time.ticks_ms() - start
  led.value(0)
  lcd.clear()
  lcd.putstr("reaction time:")
  lcd.move_to(0,1)
  lcd.putstr(str(reaction)+" ms")
  time.sleep(3)