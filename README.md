# 🤖 Webex Auto-Joiner Bot

A Python bot that automatically joins your Webex online classes at scheduled times — so you never get barred for missing class again.

---

## ✨ Features

- ⏰ **Scheduled joining** — joins your class automatically based on your timetable
- 🖱️ **Smart button detection** — scans the screen to find and click the green "Join meeting" button
- 💤 **Anti-idle mouse mover** — nudges the mouse every 2–4 minutes to prevent idle disconnection
- 🔇 **Mic & camera off by default** — respects Webex's default muted state, no accidental interruptions
- 📅 **Multi-class support** — handles 5+ classes across different days and times
- 🪟 **Windows native** — built for Windows with the Webex desktop app

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `pyautogui` | Controls mouse/keyboard, reads screen pixels |
| `schedule` | Triggers the bot at the right time |
| `subprocess` | Opens the Webex meeting link |
| `threading` | Runs anti-idle loop alongside the main bot |
| `json` | Reads your class schedule config file |

---

## 📦 Installation

**1. Make sure you have Python installed**

Download from [python.org](https://python.org/downloads) — during install, tick **"Add Python to PATH"**.

**2. Clone this repository**

```bash
git clone https://github.com/YOUR_USERNAME/webex-auto-joiner.git
cd webex-auto-joiner
```

Or just download the ZIP and extract it.

**3. Install dependencies**

Double-click `install.bat`, or run:

```bash
pip install pyautogui schedule pygetwindow keyboard pywin32
```

---

## ⚙️ Configuration

Edit `class_schedule.json` with your real class details:

```json
[
  {
    "name": "Network Security Technology",
    "link": "https://your-university.webex.com/meet/your-link",
    "days": ["Monday", "Wednesday"],
    "start_time": "08:25",
    "duration": 120
  },
  {
    "name": "Another Subject",
    "link": "https://your-university.webex.com/meet/another-link",
    "days": ["Tuesday", "Thursday"],
    "start_time": "10:00",
    "duration": 90
  }
]
```

| Field | Description |
|-------|-------------|
| `name` | Your class name |
| `link` | The Webex meeting URL your lecturer shares |
| `days` | Days of the week (Monday–Sunday) |
| `start_time` | 24-hour format, e.g. `"09:00"` for 9am |
| `duration` | Class duration in minutes |

> The bot joins **2 minutes early** so it's ready by the time class starts.

---

## ▶️ Usage

Double-click `run_bot.bat` or run:

```bash
python webex_bot.py
```

You'll see output like:

```
=======================================================
  Webex Auto-Joiner Bot  v3
=======================================================

Loaded 2 class(es):

  Scheduled: Network Security | Monday @ 08:25 (bot starts @ 08:23)
  Scheduled: Another Subject  | Tuesday @ 10:00 (bot starts @ 09:58)

Bot is running. Press Ctrl+C to stop.
```

Leave the window open. The bot runs silently in the background until class time.

---

## 💡 How It Works

```
1. Reads class_schedule.json
         ↓
2. Waits for scheduled time (triggers 2 min early)
         ↓
3. Opens Webex meeting link via Windows "start" command
         ↓
4. Waits 12 seconds for the pre-join screen to load
         ↓
5. Scans screen pixels to find the green "Join meeting" button
         ↓
6. Clicks it → you're in the meeting
         ↓
7. Anti-idle loop nudges mouse every 2–4 min for the class duration
```

---

## ⚠️ Important Notes

- Your **PC must be on** and **screen unlocked** when class starts
- Set Windows to **never sleep**: Settings → System → Power → Sleep → Never
- Keep the **black terminal window open** — closing it stops the bot
- The bot works with the **Webex desktop app**, not the browser version
- Your lecturer's Webex link is usually on your university portal (e.g. Moodle, Google Classroom)

---

## 🔧 Troubleshooting

| Problem | Fix |
|--------|-----|
| `ModuleNotFoundError` | Run `install.bat` again |
| Bot opens Webex but doesn't click Join | Your screen resolution may differ — try running a test join manually first |
| Wrong class time | Check your Windows clock timezone (should be MYT, UTC+8) |
| Python not found | Reinstall Python and tick "Add Python to PATH" |

---

## 📁 File Structure

```
webex-auto-joiner/
├── webex_bot.py          # Main bot script
├── class_schedule.json   # Your class timetable config
├── install.bat           # One-click dependency installer
├── run_bot.bat           # One-click bot launcher
└── README.md             # This file
```

---

## 📄 License

MIT License — free to use, modify, and share.

---

> Built for students dealing with early morning online classes. Use responsibly.
