from flask import Flask, render_template, request, jsonify
import datetime
import webbrowser
import pyautogui
from time import sleep
import pyttsx3
import PyPDF2
engine = pyttsx3.init()
app = Flask(__name__)
time = datetime.datetime.now().strftime("%H hours %M minutes and %S seconds")
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    greeting += " I am Nexus, how can I help you?"
    return greeting

def speak(text):
    engine.say(text)
def pdf_reader():
    book = open("", "rb")
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    speak(f"total number of pages in this book is {pages}")
    speak("master enter the page i have to read:")
    pg = int(input("page number :"))
    page = pdfReader.pages[pg]
    text = page.extract_text()
    speak(text)
def run_nexus(query: str):
    """Core Nexus logic"""
    query = query.lower()
    response = ""

    if "play" in query:
        webbrowser.open("www.youtube.in")
        pyautogui.moveTo(579, 125, 1)
        sleep(4)
        pyautogui.click()
        sleep(1)
        query = query.replace("open ", '').replace("video", '').replace("jarvis ", '').replace("play", '')
        pyautogui.typewrite(f"{query}")
        pyautogui.hotkey("enter")
        pyautogui.moveTo(361, 386, 1)
        sleep(3)
        pyautogui.click()
    elif "audiobook" in query.lower():
        pdf_reader()
    elif "face recognition" in query.lower():
        import face_recognition

    elif "change" in query:
        pyautogui.moveTo(1184, 135, 1)
        sleep(2)
        pyautogui.click()
        sleep(1)
        pyautogui.moveTo(1179, 135, 1)
        pyautogui.click()
        query = query.replace("change", "").replace("and", "")
        pyautogui.typewrite(f"{query}")
        pyautogui.hotkey("enter")
        pyautogui.moveTo(466, 366, 1)
        sleep(2)
        pyautogui.click()

    elif "whatsapp" in query:
        webbrowser.open("web.whatsapp.com")

    elif "instagram" in query:
        webbrowser.open("https://www.instagram.com/")

    elif "introduce" in query:
        if "team" in query:
            response = (
                "Ok master, the name of the team is Tech Titans. "
                "Now introducing the members: Ritiwaesh Bhardwaj, the team leader, "
                "Goon Single, Neha Singh, and Maanyaa Jain."
            )
        else:
            response = (
                "Best AI Assistant powered by GPT. Nexus, your AI copilot, "
                "seamlessly integrates with your web browser and OS "
                "to boost productivity with rich features including AI chat, "
                "suggestions, translation, rewriting, and more."
            )
        speak(response)
    elif "information" in query:
        query = query.replace("get", "")
        webbrowser.open("https://chatgpt.com/")
        sleep(4)
        pyautogui.moveTo(803, 504)
        pyautogui.typewrite(f"{query}")
        pyautogui.hotkey("enter")

    elif "close it" in query:
        pyautogui.hotkey("alt", "F4")
    elif "close" in query.lower():

        from apps import closeappweb
        closeappweb(query)

    elif "wish" in query:
        if time >= "19 hours 45 minutes and 00 seconds":
            tric = "night"
        elif time >= "16 hours 00 minutes and 00 seconds":
            tric = "evening"
        elif time >= "12 hours 00 minutes and 00 seconds":
            tric = "afternoon"
        else:
            tric = "morning"

        query = query.replace("wish", "")
        response = f"Hey {query}, a very warm and good {tric} from my team and me."
        speak(response)

    elif "feelings" in query:
        webbrowser.open("https://www.youtube.com/shorts/bPkuVwHVQlU")

    elif "dance" in query:
        response = "That's a nice idea master, I am initiating a pixel dance."

        pyautogui.hotkey("win", "r")
        sleep(1)
        pyautogui.hotkey("enter")
        sleep(3)
        pyautogui.typewrite("cd/")
        pyautogui.hotkey("enter")
        sleep(0.6)
        pyautogui.typewrite("cd\\Windows\\System32")
        pyautogui.hotkey("enter")
        pyautogui.typewrite("curl ascii.live/rick")
        pyautogui.hotkey("enter")
        speak(response)

    elif "want" in query:
        response = "Master really, this was in my mind since months."
        speak(response)
        webbrowser.open("https://www.deviantart.com/antmanai/art/Female-Jarvis-967108805")

    elif "shameless" in query:
        webbrowser.open("https://www.youtube.com/shorts/phC1CeSCDv8")

    elif "click" in query:
        pyautogui.click()

    elif "generate" in query:
        webbrowser.open("https://firefly.adobe.com/generate/image")
        pyautogui.moveTo(599, 953)
        sleep(10)
        pyautogui.click()
        query = query.replace("generate", "")
        pyautogui.typewrite(f"{query}")
        sleep(2)
        pyautogui.hotkey("enter")

    elif "command prompt" in query:
        pyautogui.hotkey("win", "r")
        sleep(1)
        pyautogui.hotkey("enter")
        sleep(3)
        pyautogui.typewrite("cd/")
        pyautogui.hotkey("enter")
        sleep(0.6)
        pyautogui.typewrite("cd\\Windows\\System32")
        pyautogui.hotkey("enter")

    elif "poem" in query:
        webbrowser.open("https://thesonofthedragon.tumblr.com/image/118684971049")
        response = (
            "Death must be so beautiful. "
            "To lie in the soft brown earth with the grasses waving above one's head "
            "and listen to silence. To have no yesterday and no tomorrow. "
            "To forget time, to forgive life, to be at peace."
        )
        speak(response)
    elif "can" in query or "do you" in query:
        query = query.replace("you", '')
        response = f"Yes, I can {query}"
        speak(response)


    elif "are you" in query or "r u" in query:
        response = "Yes master, I am fine and what about you?"
        speak(response)
    elif "type" in query.lower():
        if "dance" in query:
            pyautogui.typewrite("rick")
            sleep(1)
            pyautogui.hotkey("enter")
        elif "run" in query:
            pyautogui.typewrite("forrest")
            sleep(1)
            pyautogui.hotkey("enter")
        elif "network sharing" in query:
            pyautogui.typewrite("netsh wlan show profiles name="" key=clear")
        elif "star wars" in query.lower():
            pyautogui.typewrite("telnet towel.blinkenlights.nl")
            sleep(1)
            pyautogui.hotkey("enter")
        elif "sky" in query.lower():
            pyautogui.typewrite(f'curl ascii.live/')
        elif "show" in query.lower():
            query = query.replace("type", '')
            pyautogui.typewrite(f"netsh wlan{query}")
            sleep(1)
            pyautogui.hotkey("enter")
        elif "system info" in query.lower():
            pyautogui.typewrite("systeminfo")
            sleep(2)
            pyautogui.hotkey("enter")
        else:
            query = query.replace("type", "")
            query=query.replace(".","")
            pyautogui.typewrite(f"{query.lower()}")
            pyautogui.hotkey("enter")
    elif "planetspark" in query.lower():
        webbrowser.open("https://www.planetspark.in/employees/combat_leads/unassigned")
        sleep(3)
        response=("your respective CRM is being opened master")
        response=("this is your respective updation master")
        pyautogui.moveTo(135,433)

    else:
        response = "Sorry master, can you repeat it?"
    return response
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/launch")
def launch():
    greeting = wish_me()
    return render_template("launch.html", message=greeting)
@app.route("/process_command", methods=["POST"])
def process_command():
    data = request.json
    command = data.get("command", "")
    response = run_nexus(command)
    return jsonify({"response": response})
if __name__ == "__main__":
    app.run(debug=True)

