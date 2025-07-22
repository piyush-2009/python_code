import time
import os
from termcolor import cprint, colored

# Agar termcolor installed nahi hai to ye command chalao:
# pip install termcolor

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def happy_birthday(name):
    messages = [
        "🎉🎉🎉🎉🎉🎉🎉🎉🎉",
        "      HAPPY",
        "     BIRTHDAY",
        f"     {name.upper()}!",
        "🎂🎂🎂🎂🎂🎂🎂🎂🎂"
    ]

    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

    for i in range(3):  # 3 baar repeat hoga
        clear_screen()
        for msg in messages:
            color = colors[i % len(colors)]
            cprint(msg.center(50), color, attrs=['bold'])
            time.sleep(0.5)
        time.sleep(1)

# 👇 Yahan name daalo
your_name = "Piyush"
happy_birthday(your_name)
