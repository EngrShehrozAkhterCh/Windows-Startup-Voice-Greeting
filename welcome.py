import time
import pyttsx3
from datetime import datetime

# Delay to ensure audio drivers are ready
time.sleep(10)

# Initialize the engine
engine = pyttsx3.init()

# Adjust speaking rate and volume
engine.setProperty("rate", 130)
engine.setProperty("volume", 0.9)

# 🔊 Choose voice (0 = male, 1 = female)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # change 1→0 for male

# Get current date and time
now = datetime.now()
hour = now.hour
weekday = now.strftime("%A")  # e.g., Monday, Tuesday, etc.

# Determine greeting based on time
if 5 <= hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 17:
    greeting = "Good afternoon"
elif 17 <= hour < 21:
    greeting = "Good evening"
else:
    greeting = "Good night"

# Weekend special message
if weekday in ["Saturday", "Sunday"]:
    extra_msg = f"Happy {weekday}, Shehroz! Enjoy your weekend!"
else:
    extra_msg = "Have a nice day!"

# Current time
current_time = now.strftime("%I:%M %p")

# Combine final message
message = f"{greeting}, Shehroz Akhter Chaudhary! It's {current_time}. {extra_msg}"

# Speak the message
engine.say(message)
engine.runAndWait()
