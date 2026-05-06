# -*- coding:utf-8 -*-

# Interface for zzz using the Waveshare 1.44inch LCD HAT.
# https://www.waveshare.com/wiki/1.44inch_LCD_HAT

import LCD_1in44
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

# 128x128 display with hardware SPI:
disp = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
disp.LCD_Init(Lcd_ScanDir)
disp.LCD_Clear()

# Create blank image for drawing.
image = Image.new('RGB', (disp.width, disp.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, disp.width,disp.height), outline=0, fill=0)
disp.LCD_ShowImage(image, 0, 0)

# launcher_image = Image.open('launcher.bmp')

MAIN_MENU = 0
ZZZ_MODE = 1
mode = MAIN_MENU

TOP_POS = 27
MIDDLE_POS = 57
BOTTOM_POS = 87

print("ZLauncher started.")

try:
    while True:
        # DRAW INTERFACE
        if mode == MAIN_MENU:
            # TODO Draw header or image
            # image = launcher_image
            draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

            # 3 button options
            draw.text((107, TOP_POS), 'zzz ', fill = "BLUE")
            draw.text((85, MIDDLE_POS), '  ', fill = "BLUE")
            draw.text((103, BOTTOM_POS), 'Quit ', fill = "RED")

        elif mode == ZZZ_MODE:
            # zzz header
            draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
            draw.text((10, 10), 'zzz ', fill = "BLUE")

            # exit button
            draw.text((106, BOTTOM_POS), 'Exit ', fill = "PURPLE")


        # HANDLE KEY INPUTS
        # KEY 1
        if disp.digital_read(disp.GPIO_KEY1_PIN) != 0:
            if mode == MAIN_MENU:
              mode = ZZZ_MODE
              print("Entering zzz mode")

              # spin off zzz process
              os.system("nohup /usr/bin/python3 -u /home/pi/zzz/zzz.py >> /home/pi/zzz/sleep.log 2>&1 &")

        # KEY 2
        if disp.digital_read(disp.GPIO_KEY2_PIN) != 0:
            print("Key2")

        # KEY 3
        if disp.digital_read(disp.GPIO_KEY3_PIN) != 0:
            if mode == MAIN_MENU:
              print("Quitting ZLauncher")
              exit()

            if mode == ZZZ_MODE:
              mode = MAIN_MENU
              print("Exiting zzz mode")

              # kill zzz process
              os.system("kill -9 $(pgrep -f \"usr/bin/python3 -u /home/pi/zzz/zzz.py\")")

        # UP
        if disp.digital_read(disp.GPIO_KEY_UP_PIN ) != 0:
            print("Up" )
        # LEFT
        if disp.digital_read(disp.GPIO_KEY_LEFT_PIN) != 0:
            print("Left")
        # RIGHT
        if disp.digital_read(disp.GPIO_KEY_RIGHT_PIN) != 0:
            print("Right")
        # DOWN
        if disp.digital_read(disp.GPIO_KEY_DOWN_PIN) != 0:
            print("Down")
        # CENTER
        if disp.digital_read(disp.GPIO_KEY_PRESS_PIN) != 0:
            print("Center")

        disp.LCD_ShowImage(image, 0, 0)

except:
  print("Exception.")
  disp.LCD_ShowImage(image, 0, 0)

disp.module_exit()
