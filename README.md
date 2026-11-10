# ⌨️ Keytaps

Keytaps is a lightweight Python desktop app that plays a sound every time you press a key. It listens to your keyboard in any window or app, plays a default click for the keys, and lets you set your custom sounds to any individual key.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Custom Sounds](#custom-sounds)
- [How It Works](#how-it-works)
- [Platform Notes](#platform-notes)
- [Troubleshooting](#troubleshooting)
- [Scope and Limitations](#scope-and-limitations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## Features

- **Global key listening:** sounds play no matter which window is focused.
- **Default sounds:** one sound for normal keys (letters, numbers, symbols) and another for special keys (Enter, Space, Shift, and so on).
- **Per-key custom sounds:** set any `.wav` or `.mp3` file to any key.
- **Persistent settings:** custom sounds are saved to `sounds.json` and loaded everytime the app starts.
- **Non-blocking playback:** sounds play in the background so typing never lags behind.
- **Startup sound:** a short sound plays when the listener becomes active.
---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Core language |
| **[pynput](https://pypi.org/project/pynput/)** | Global keyboard listener |
| **[playsound3](https://pypi.org/project/playsound3/)** | Cross-platform audio playback |
| **JSON** | Storing custom key-to-sound mappings |

Standard library modules used: `json`, `pathlib`, `time`.

---

## Project Structure

```
keytaps/
├── app.py              # Main application (listener, playback, custom sound setup)
├── sounds.json         # Saved custom key -> sound mappings
├── requirements.txt    # Python dependencies
├── README.md           # You are here
└── sounds/             # Audio files
    ├── light.wav       # Default sound for normal keys
    ├── strong.wav      # Default sound for special keys
    ├── 7.mp3           # Startup sound
    └── dragon-studio-pop-402324.mp3
```

---

## Getting Started

### Prerequisites

- Python 3.8 or newer
- `pip`
- A keyboard and working audio output

### Installation

1. **Get the project**

   ```bash
   git clone htts://github.com/RADYO-ACTIV/keytaps.git
   cd keytaps
   ```

   Or download and extract the project folder, then open a terminal inside it.

2. **(Recommended) Create a virtual environment**

   ```bash
   python -m venv venv

   # macOS / Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make sure `sounds.json` is valid.** An empty object is enough for initial setup:

   ```json
   {}
   ```

5. **Check the default sound files exist.** The app expects `sounds/light.wav` (normal keys) and a special-key sound (`sounds/strong.wav` by default).

---

## Usage

Start the app from the project folder:

```bash
python app.py
```

You'll see a prompt:

```
keytaps active. press "S" to start and "C" to choose custom sounds:
```

| Input | Result |
|---|---|
| `s` + Enter | Start listening immediately |
| `c` + Enter | Open the custom sound setup first |

Once running, a startup sound plays and the app prints:

```
Listening for key presses. Press CTRL+C to stop.
```

Type anywhere and you'll hear your sounds. Press **Ctrl+C** in the terminal to quit.

---

## Custom Sounds

You can give any key its own sound.

1. Run `python app.py` and enter `c`.
2. When prompted, **press the key** you want to customize.
3. **Paste the full path** to the sound file when asked, e.g.:
   - Windows: `C:\Users\you\Music\click.wav`
   - macOS / Linux: `/home/you/sounds/click.wav`
4. If the file is valid, it's saved and you're asked whether to add another (`Y` or `N`).
5. Enter `n` to finish and start the listener.

**Accepted formats:** `.wav` and `.mp3`.

**Tips:**
- Quotes around the path (for example when you copy it from Windows Explorer) are stripped automatically.
- Re-assigning a key that already has a sound replaces the old sound.

### `sounds.json` format

Custom sounds are stored as a simple key-to-path map:

```json
{
  "a": "/home/you/sounds/click.wav",
  "space": "/home/you/sounds/thud.mp3",
  "enter": "/home/you/sounds/ding.wav"
}
```

- **Normal keys** use the character itself in lowercase (`a`, `7`, `;`).
- **Special keys** use their pynput name (`space`, `enter`, `shift`, `backspace`, `tab`, and so on).
- Keys without a stored sound fall back to the default sound for their type.

You can edit this file by hand, as long as it stays valid JSON.

To reset everything to defaults, replace the contents of `sounds.json` with `{}`.

---

## How It Works

1. On start, `app.py` loads `sounds.json` into memory.
2. If you chose custom setup, a temporary listener captures one keypress, and you provide a sound path. The path is validated (file exists, `.wav` or `.mp3`) and written to `sounds.json`.
3. The main listener starts. On every key press it:
   - converts the key to a string (`a`, `space`, ...),
   - looks it up in the custom sounds,
   - plays the custom sound if there is one, otherwise the normal-key or special-key default.
4. Playback is non-blocking (`block=False`), so rapid typing doesn't queue up or stall.

---

## Platform Notes

| Platform | Notes |
|---|---|
| **Windows** | Works out of the box. |
| **macOS** | Grant your terminal (or IDE) **Accessibility** and **Input Monitoring** permission under *System Settings → Privacy & Security*, otherwise no keys are detected. |
| **Linux** | `pynput` needs an X server. It generally does not work on Wayland-only sessions. MP3 playback may require GStreamer to be installed. |

---

## Troubleshooting

| Problem | Likely cause and fix |
|---|---|
| `ModuleNotFoundError: playsound` | The package is `playsound3`. Install it with `pip install playsound3` and import it as `from playsound3 import playsound`. |
| `json.JSONDecodeError` on start | `sounds.json` is malformed. Replace its contents with `{}`. |
| No sound on keypress (macOS) | Grant Accessibility / Input Monitoring permission to your terminal and restart it. |
| "invalid path" message | The file doesn't exist or isn't `.wav` / `.mp3`. Paste the full absolute path. |
| Sound repeats rapidly when a key is held | Holding a key triggers repeated key events. This is expected with the current version (see Roadmap). |
| MP3s don't play on Linux | Install GStreamer and its Python bindings, or use `.wav` files. |

---

## Scope and Limitations

**In scope**
- Playing sounds in response to keyboard input on desktop systems.
- Per-key customization stored locally.
- Running as a simple terminal application.

**Currently out of scope**
- No graphical interface. Setup and control happen in the terminal.
- No volume control or sound mixing.
- No mouse or gamepad support.
- No mobile support.
- Key-repeat events are not filtered, so holding a key replays its sound.
- Only absolute file paths are supported for custom sounds.

**Privacy note:** Keytaps listens to all keyboard input system-wide in order to trigger sounds. It does not record, store, or transmit what you type. Only the key-to-sound mappings you create are saved, and only in `sounds.json` on your machine. Even so, only run software like this from sources you trust.

---

## Roadmap

Ideas for future improvement:

- [ ] Ignore key-repeat while a key is held down
- [ ] Volume control
- [ ] Sound packs (switch whole themes, for example mechanical, typewriter, bubble pop)
- [ ] Remove or reset a single custom sound from within the app
- [ ] Simple GUI or system-tray icon with a pause and resume toggle
- [ ] Relative paths and drag-and-drop support for sound files
- [ ] Packaging as a standalone executable

---

## Contributing

Contributions are welcome.

Bug reports and feature ideas are welcome as issues.