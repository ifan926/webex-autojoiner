====================================================
  WEBEX AUTO-JOINER BOT - Setup Guide
====================================================

REQUIREMENTS
------------
- Windows 10/11
- Python 3.8+ installed (python.org)
- Webex Desktop App installed

QUICK START
-----------
1. Run install.bat  → installs required packages
2. Edit class_schedule.json → add your real class links & times
3. Run run_bot.bat  → starts the bot

HOW TO EDIT YOUR SCHEDULE (class_schedule.json)
------------------------------------------------
Open class_schedule.json in Notepad and fill in:

  "name"       → Your class name (e.g. "Mathematics")
  "link"       → The Webex meeting URL your lecturer shares
  "days"       → Days of the week (e.g. ["Monday","Wednesday"])
  "start_time" → 24hr format (e.g. "09:00" for 9am, "14:30" for 2:30pm)
  "duration"   → How long the class runs in minutes (e.g. 90)

TIP: Use the scheduler UI (open scheduler_ui.html in your browser)
     to fill in your schedule visually and download the JSON file!

WHAT THE BOT DOES
-----------------
- Opens your Webex meeting link at the scheduled time
- Automatically presses Enter to confirm the browser dialog
- Mutes your microphone (Ctrl+M)
- Turns off your camera (Ctrl+Shift+V)
- Nudges the mouse every 2-4 minutes to prevent idle timeout

IMPORTANT NOTES
---------------
- Keep your PC on and don't close the terminal window while bot runs
- Webex desktop app must be installed (not browser version)
- The bot needs your screen to be unlocked when class starts
- You can still use your PC normally while the bot runs

TROUBLESHOOTING
---------------
- "Module not found" → run install.bat again
- Bot joins but mic/cam not muting → try joining manually once first
  so Webex remembers your preferences
- Wrong time → check your Windows clock timezone settings

====================================================
