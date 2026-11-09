from playsound import playsound
from pynput import keyboard
import time
import json
import os
import pathlib

with open("sounds.json", "") as file:
  custom_sounds=json.load(file)
  
normal_keys = 'sounds/light.wav'
special_keys = 'sounds/strong.wav'
custom_key = ''

def validate_path():
  pass

def update():
  pass
def on_press(key):
    sound_path = custom_sounds[key]
    try:
      if sound_path:
        playsound(sound_path, block=False)
      else:
        playsound(normal_keys, block=False)
        
    except AttributeError:
      if sound_path:
        playsound(sound_path, block=False)
      else:
        playsound(special_keys, block=False)

def custom(key):
  print(f'You pressed: {key}')
  custom_key = key
  return False

intro = (input('keytaps active. press "S" to start and "C" to choose custom sounds: ')).lower()

while intro == 'c' or intro=='y':
  print('''
  HOW TO SET CUSTOM SOUNDS FOR DIFFETENT KEYS
  
  1. WHEN PROMPTED, CLICK ON THE KEY YOU WANT TO ADD THE SOUND TO
  
  2. ONCE THE KEY HAS REGISTERED, PASTE THE COMPLETE/ABSOLUTE FILE PATH OF THE SOUND YOU WISH TO ADD
  
  3. ONCE YOU'RE DONE, CLICK ON ENTER. IF YOU WANT TO CONTINUE ADDING CUSTOM SOUNDS, CLICK 'Y' IF NOT CLICK 'N' AND LET THE PROGRAM CONTINUE RUNNING.
  ''')
  time.sleep(3)
  with keyboard.Listener(on_press=custom) as customizer:
    print('tap on the key you want to customize')
    customizer.join()

  file_path = input('paste the file path to your sound: ')
  if !validate_path(file_path):
    print('invalid path. make sure file exists and is in the correct audio format.')
  else:
    update()
    intro = input('custom sound added, do you want to add another one?(Y or N) ').lower()

with keyboard.Listener(on_press=on_press) as listener:
      playsound("sounds/7.mp3", block=True)
      print("Listening for key presses. Press CTRL+C to stop.")
      listener.join()