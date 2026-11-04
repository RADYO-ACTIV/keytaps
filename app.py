from playsound import playsound
from pynput import keyboard
import json

with open("sounds.json", "") as file:
  custom_sounds=json.load(file)
  
normal_keys = 'sounds/light.wav'
special_keys = 'sounds/'

def on_press(key):
    sound_path = custom_sounds[key]
    try:
      print(f"Alphanumeric key pressed: {key.char}")
      if sound_path:
        playsound(sound_path, block=False)
      else:
        playsound(normal_keys, block=False)
        
    except AttributeError:
      print(f"Special key pressed: {key}")
      if sound_path:
        playsound(sound_path, block=False)
      else:
        playsound(, block=False)

intro = (input('keytaps started. press "S" to start and "C" to choose custom sounds: ')).lower()

if intro == 's':
  with keyboard.Listener(on_press=on_press) as listener:
      playsound("sounds/7.mp3", block=True)
      print("Listening for key presses. Press CTRL+C to stop.")
      listener.join()

elif intro == 'c':
  print('''
  HOW TO SET CUSTOM SOUNDS FOR DIFFETENT KEYS
  
  1. WHEN PROMPTED, CLICK ON THE KEY YOU WANT TO ADD THE SOUND TO
  
  2. ONCE THE KEY HAS REGISTERED, PASTE THE COMPLETE/ABSOLUTE FILE PATH OF THE SOUND YOU WISH TO ADD
  
  3. ONCE YOU'RE DONE, CLICK ON ENTER. IF YOU WANT TO CONTINUE ADDING CUSTOM SOUNDS, CLICK 'Y' IF NOT CLICK 'N' AND LET THE PROGRAM CONTINUE RUNNING.
  ''')
  pass