Windows Startup Voice Greeting (Python + pyttsx3)

A simple and fun Python script that greets you every time you start your computer — with a time-based voice message and your name!
It works offline using the pyttsx3 text-to-speech engine.

✨ Features

🎧 Greets you based on the current time — Good Morning, Good Afternoon, Good Evening, or Good Night

🕒 Announces the current system time

📅 Adds a cheerful weekend message (Happy Sunday, enjoy your weekend!)

👩‍💻 Switch between male or female voice easily

⚙️ Works automatically on Windows startup (via .bat file or Task Scheduler)

🚫 100% offline — no internet required!

🧩 Requirements

Python 3.10 or later

pyttsx3 library

🛠️ Installation

Run this command in Command Prompt (CMD) or PowerShell:

pip install pyttsx3

🚀 Setup (Auto Run on Startup)
Option 1: Using Startup Folder

Create a .bat file (e.g., voice_greet.bat) with the following line:

python "C:\path\to\your\greet_script.py"


Copy the .bat file to:

C:\Users\<YourUser>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup


Restart your PC and enjoy the voice greeting! 🎶

Option 2: Using Task Scheduler

Open Task Scheduler → Create Task

Under Actions, select Start a program → Browse to your .bat file

Under Triggers, choose At startup

Save and restart!

👨‍💻 Author

Muhammad Shehroz Akhter Chaudhary
🎓 Electrical Engineering | UET Lahore
💡 Passionate about AI, Machine Learning, and Embedded Systems

🧠 Fun Ideas

You can customize this script to:

🔊 Speak motivational quotes

🗓️ Read your daily to-do list or schedule

🌦️ Announce weather updates

💻 Read system stats (battery %, CPU temp, etc.)

Just edit the message string in the code to make it your own!
