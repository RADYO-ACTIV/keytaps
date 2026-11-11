# Keytaps

Keytaps plays a sound every time you press a key on your keyboard. It works in any window, so you can be typing in a browser, a code editor or a game and it'll still make noise.

Normal keys get one sound, special keys (Enter, Space, Shift and so on) get another, and you can give any key a sound of your own.

I built it because I wanted my keyboard to feel a bit more fun to type on.

## What it uses

- Python
- `pynput` to listen for key presses
- `playsound3` to play the audio
- a `sounds.json` file to remember your custom sounds

## What's in the folder

```
keytaps/
├── app.py            the whole app
├── sounds.json       your custom key sounds get saved here
├── requirements.txt
└── sounds/           the audio files
```

The `sounds` folder already has a few sounds you can use or swap out.

## Setting it up

You need Python 3.8 or newer.

1. Download the project and open a terminal inside the folder.
2. Install the packages:

   ```
   pip install -r requirements.txt
   ```

3. Make sure `sounds.json` isn't empty. If it's a fresh install, just put this in it:

   ```
   {}
   ```

4. The app expects a default sound for special keys at `sounds/strong.wav`. If you don't have that file, either add one or change `special_keys` in `app.py` to point at a sound you do have.

## Running it

```
python app.py
```

It'll ask what you want to do. Type `s` and hit Enter to start, or `c` to set up custom sounds first.

Once it's running you'll hear a startup sound, and then every key you press makes a sound. Press `Ctrl + C` in the terminal to stop it.

## Adding your own sounds

1. Run the app and type `c`.
2. Press the key you want to change.
3. Paste the full path to your sound file, like `C:\Users\you\Music\click.wav`.
4. It'll save it and ask if you want to add another one.

It only takes `.wav` and `.mp3` files. If you add a sound to a key that already has one, the old one gets replaced.

To undo everything, open `sounds.json` and change it back to `{}`.

## Things to know

**macOS:** you have to give your terminal Accessibility and Input Monitoring permission (System Settings > Privacy & Security), otherwise it won't pick up any key presses.

**Linux:** `pynput` needs X11, so it probably won't work on Wayland. MP3s might also need GStreamer installed. `.wav` files are safer.

**Privacy:** the app listens to every key you press so it can play sounds, but it doesn't record or save what you type. The only thing it stores is which key has which sound.

## Stuff that doesn't work (yet)

- If you hold a key down, the sound keeps repeating.
- There's no volume control.
- It's terminal only, no window or buttons.
- Custom sounds need the full file path, not a short one.

## Maybe later

- Stop the sound repeating when a key is held
- Volume control
- Different sound packs
- A simple window so you don't need the terminal

## Common problems

**`ModuleNotFoundError: playsound`:** the package is called `playsound3`, so install that and import it with `from playsound3 import playsound`.

**Error when reading `sounds.json`:** the file is broken or empty. Replace what's in it with `{}`.

**Nothing happens when I type (Mac):** it's the permissions thing above. Give your terminal access and restart it.

**"Invalid path":** the file doesn't exist or isn't a `.wav` or `.mp3`. Try pasting the full path again.

## Credits

entavo and mixit. thsts wgete i got most alm 5be sounds used in this project
