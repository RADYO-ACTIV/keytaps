from playsound3 import playsound
from pynput import keyboard
import time
import json
from pathlib import Path
import sys

def resource_path(relative):
    """For bundled, read-only files (the sounds folder)."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return base / relative

def app_dir():
    """Folder containing the exe (or app.py when running normally)."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

SOUNDS_FILE = app_dir() / "sounds.json"
BASE_DIR = Path(__file__).parent
VALID_EXTENSIONS = {".wav", ".mp3"}
NORMAL_KEYS = str(resource_path("sounds/light.wav"))
SPECIAL_KEYS = str(resource_path("sounds/strong.wav"))

def load_sound():
  try:
    with open(SOUNDS_FILE, "r") as file:
      return json.load(file)
  except Exception:
    return {}

custom_sounds = load_sound()

def parse_key(key):
  """Turn a pynput key into a JSON-safe string ('a', 'space', 'enter'...)."""
  if isinstance(key, keyboard.KeyCode):
      return key.char.lower() if key.char else f"vk_{key.vk}"
  return key.name

def on_press(key):
    sound_path = custom_sounds.get(parse_key(key))
    if sound_path.is_file() and Path(sound_path).suffix.lower() in VALID_EXTENSIONS:
        playsound(sound_path, block=False)
    elif isinstance(key, keyboard.KeyCode):
        playsound(NORMAL_KEYS, block=False)
    else:
        playsound(SPECIAL_KEYS, block=False)


def capture_key():
    """Wait for one keypress and return it."""
    captured = {}
    def on_press(key):
        captured["key"] = key
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    return captured.get("key")

def validate_path(file_path):
  p = Path(file_path.strip().strip('"').strip("'")).expanduser()
  return p.is_file() and p.suffix.lower() in VALID_EXTENSIONS

def update(key, file_path):
  sounds = load_sound()
  sounds[parse_key(key)] = str(Path(file_path.strip().strip('"').strip("'")).expanduser())

  tmp = SOUNDS_FILE.with_suffix(".tmp")
  with open(tmp, "w") as f:
    json.dump(sounds, f, indent=2)
  tmp.replace(SOUNDS_FILE)
  return sounds

intro = (input('keytaps active. press enter to continue or "C" to choose custom sounds: ')).lower()

while intro == 'c' or intro=='y':
  print('''
  HOW TO SET CUSTOM SOUNDS FOR DIFFETENT KEYS
  
  1. WHEN PROMPTED, CLICK ON THE KEY YOU WANT TO ADD THE SOUND TO
  
  2. ONCE THE KEY HAS REGISTERED, PASTE THE COMPLETE/ABSOLUTE FILE PATH OF THE SOUND YOU WISH TO ADD
  
  3. ONCE YOU'RE DONE, CLICK ON ENTER. IF YOU WANT TO CONTINUE ADDING CUSTOM SOUNDS, CLICK 'Y' IF NOT CLICK 'N' AND LET THE PROGRAM CONTINUE RUNNING.
  ''')
  time.sleep(3)
  print('tap on the key you want to customize')
  key = capture_key()
  time.sleep(1)
  file_path = input('paste the file path to your sound: ')
  if not validate_path(file_path):
    print('invalid path. make sure file exists and is in the correct audio format.')
  else:
    custom_sounds = update(key, file_path)
    intro = input('custom sound added, do you want to add another one?(Y or N) ').lower()

with keyboard.Listener(on_press=on_press) as listener:
      playsound(str(resource_path("sounds/7.mp3")), block=True)
      print("Listening for key presses. Press CTRL+C to stop.")
      listener.join()