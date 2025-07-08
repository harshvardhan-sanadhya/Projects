import webbrowser
import time
import math
import requests
import re
import music_lib

# Initialize TTS and recognizer

# Speak

# Prime check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Table printer
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Math solver
def solve_math(cmd):
    try:
        if "table of" in cmd:
            number = int(cmd.split("of")[1].strip())
            print(f"Table of {number}")
            print_table(number)

        elif "square root of" in cmd:
            number = int(cmd.split("of")[1].strip())
            result = number ** 0.5
            print(f"Square root of {number} is {result}")

        elif "divide" in cmd and "by" in cmd:
            words = cmd.split()
            index = words.index("by")
            num1 = int(words[index - 1])
            num2 = int(words[index + 1])
            result = num1 / num2
            print(f"{num1} divided by {num2} is {result}")

        elif "to the power" in cmd:
            base = int(cmd.split("to the power")[0].strip())
            exponent = int(cmd.split("to the power")[1].strip())
            result = base ** exponent
            print(f"{base} to the power {exponent} is {result}")

        elif "factorial of" in cmd:
            number = int(cmd.split("of")[1].strip())
            result = math.factorial(number)
            print(f"Factorial of {number} is {result}")

        elif "percent of" in cmd:
            percent = float(cmd.split("percent of")[0].strip())
            total = float(cmd.split("percent of")[1].strip())
            result = (percent / 100) * total
            print(f"{percent} percent of {total} is {result}")

        elif "is" in cmd and "prime" in cmd:
            number = int(cmd.split("is")[1].split("prime")[0].strip())
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")

        elif "even" in cmd or "odd" in cmd:
            number = int([word for word in cmd.split() if word.isdigit()][0])
            if number % 2 == 0:
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")

        elif "area of circle with radius" in cmd:
            radius = float(cmd.split("radius")[1].strip())
            area = math.pi * radius ** 2
            print(f"Area of circle with radius {radius} is {area:.2f}")

        else:
            # Fallback to eval for expressions like 5 + 2 * 3
            result = eval(cmd)
            print(f"The answer is {result}")

    except Exception as e:
        print("Sorry, I couldn't understand that math.")
        print("Error:", e)

def news():
    print("In news function")
    api_key="23a56b7c2264b60b37243b7d223e5ee4"
    country="in"
    r=requests.get(f"https://gnews.io/api/v4/top-headlines?country={country}&lang=en&max=5&apikey={api_key}")
    if r.status_code==200:
        data=r.json()
        articles=data.get('articles',[])
        for article in articles:
            print(article['title'])

def songs(cmd):
    if cmd.lower()=="stealth":
        song=cmd.lower()
        link=music_lib.music[song]
        webbrowser.open(link)
    elif cmd.lower()=="sunny":
        song=cmd.lower()
        link=music_lib.music[song]
        webbrowser.open(link)
    elif cmd.lower()=="island":
        song=cmd.lower()
        link=music_lib.music[song]
        webbrowser.open(link)
    else:
        print("Not Found")

# Process command
def process(cmd):
    cmd = cmd.lower().strip()

    if "open google" in cmd:
            webbrowser.open("https://google.com")
    elif "open youtube" in cmd:
            webbrowser.open("https://youtube.com")
    elif "open facebook" in cmd:
            webbrowser.open("https://facebook.com")
    elif "open instagram" in cmd:
            webbrowser.open("https://instagram.com")
    elif "open linkedin" in cmd:
            webbrowser.open("https://linkedin.com")
    else:
            print("Sorry, I didn't recognize that command.")

# Startup guide

# Main loop
print("Jarvis is now online.")
print("Activate Me By saying JARVIS")
print("Select A Mode")
print("News")
print("Songs")
print("Command")
print("Calculation")

while True:
    try:
            
      word=input("enter the name 1 :")
      if "jarvis" in word.lower():
       print("✅ Wake word detected.")
       command=input("Enter the command :")

       print(f"🗣️ You said: {command}")
       if "news" in command.lower():
           print("News Mode ON")
           news()
       elif "songs" in command.lower():
                print("Songs Mode On")
                cmd=input("Enter the song name :")
                songs(cmd)
       elif "command" in command.lower():
            print("Command mode on")
            command=input("Enter the command name :")
            process(command)
       elif "calculation" in command.lower():
            print("Calculation mode on")
            command=input("Enter the Expression :")
            solve_math(command)
       else:
            print("Invalid Command")

    except Exception as e:
        print("⚠️ Error:", e)

