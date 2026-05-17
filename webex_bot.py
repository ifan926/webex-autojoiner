"""
Webex Class Auto-Joiner Bot
Requirements: pip install pyautogui schedule pygetwindow keyboard pywin32
"""

import time
import schedule
import subprocess
import pyautogui
import threading
import random
import sys
import json
import os
from datetime import datetime

pyautogui.FAILSAFE = False

CONFIG_FILE = "class_schedule.json"

def load_schedule():
    if not os.path.exists(CONFIG_FILE):
        print(f"[ERROR] Schedule file '{CONFIG_FILE}' not found.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def click_join_button():
    """Scan screen for Webex green Join button by colour, fallback to Tab+Enter."""
    print("  Looking for Join Meeting button...")
    screen_w, screen_h = pyautogui.size()
    target_r, target_g, target_b = 45, 184, 75
    tolerance = 40
    found = None
    for y in range(int(screen_h * 0.3), int(screen_h * 0.9), 4):
        for x in range(int(screen_w * 0.5), screen_w - 20, 4):
            try:
                r, g, b = pyautogui.pixel(x, y)
                if (abs(r - target_r) < tolerance and
                    abs(g - target_g) < tolerance and
                    abs(b - target_b) < tolerance):
                    found = (x, y)
                    break
            except Exception:
                pass
        if found:
            break
    if found:
        print(f"  Found Join button at {found}, clicking...")
        pyautogui.click(found[0], found[1])
        return True
    print("  Green button not found — trying Tab+Enter fallback...")
    for _ in range(8):
        pyautogui.press("tab")
        time.sleep(0.3)
    pyautogui.press("enter")
    return False

def join_meeting(link, class_name):
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Joining: {class_name}")
    print(f"  Link: {link}")

    subprocess.Popen(["cmd", "/c", "start", "", link], shell=False)
    print("  Waiting for pre-join screen to load (12s)...")
    time.sleep(12)

    # Click Join Meeting — mic and camera are already off by default
    click_join_button()
    print("  Waiting for meeting to connect (8s)...")
    time.sleep(8)

    print(f"  Joined '{class_name}'. Anti-idle active.")

def anti_idle_loop(duration_minutes):
    end_time = time.time() + (duration_minutes * 60)
    print(f"  Anti-idle running for {duration_minutes} minutes...")
    while time.time() < end_time:
        sleep_for = random.randint(120, 240)
        time.sleep(sleep_for)
        if time.time() >= end_time:
            break
        x, y = pyautogui.position()
        pyautogui.moveTo(x + random.randint(-5, 5), y + random.randint(-5, 5), duration=0.5)
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] Anti-idle: mouse nudged.")

def setup_schedule(classes):
    day_map = {
        "Monday": "monday", "Tuesday": "tuesday", "Wednesday": "wednesday",
        "Thursday": "thursday", "Friday": "friday",
        "Saturday": "saturday", "Sunday": "sunday",
    }
    for cls in classes:
        name     = cls["name"]
        link     = cls["link"]
        days     = cls["days"]
        raw_time = cls["start_time"]
        h, m = map(int, raw_time.split(":"))
        m -= 2
        if m < 0:
            m += 60
            h -= 1
        early_time = f"{h:02d}:{m:02d}"
        duration = cls.get("duration", 60)

        def make_job(l=link, n=name, d=duration):
            def job():
                join_meeting(l, n)
                t = threading.Thread(target=anti_idle_loop, args=(d,), daemon=True)
                t.start()
            return job

        for day in days:
            day_key = day_map.get(day)
            if day_key:
                getattr(schedule.every(), day_key).at(early_time).do(make_job())
                print(f"  Scheduled: {name} | {day} @ {raw_time} (bot starts @ {early_time})")

def main():
    print("=" * 55)
    print("  Webex Auto-Joiner Bot  v3")
    print("=" * 55)
    classes = load_schedule()
    print(f"\nLoaded {len(classes)} class(es):\n")
    setup_schedule(classes)
    print("\nBot is running. Press Ctrl+C to stop.\n")
    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
