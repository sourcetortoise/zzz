from evdev import InputDevice, ecodes
from pygame import mixer
import time

print("Initializing...")
mixer.init()
sound_dir = '/home/pi/zzz/sound/'
ready_sound   = mixer.Sound(sound_dir + "piano.mp3")
trigger_sound = mixer.Sound(sound_dir + "sonar.mp3")
left_sound    = mixer.Sound(sound_dir + "pop.mp3")
right_sound   = mixer.Sound(sound_dir + "ding.mp3")

mouse = InputDevice('/dev/input/event0') # or event1, etc. if other devices are present

print(formatted_time, "Ready! Listening for input...")
ready_sound.play()

for event in mouse.read_loop():
    if event.type == ecodes.EV_KEY:
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        if event.code == ecodes.BTN_LEFT and event.value == 1:
            trigger_sound.play()
            print(formatted_time, "Trigger clicked!")
        elif event.code == ecodes.BTN_RIGHT and event.value == 1:
            right_sound.play()
            print(formatted_time, "Right button clicked!")
        elif event.code == ecodes.BTN_MIDDLE and event.value == 1:
            left_sound.play()
            print(formatted_time, "Left button clicked!")
