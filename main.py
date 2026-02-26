import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclist
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="enter your api key"
    )

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()



def processcommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")

    elif "open github" in c:
        webbrowser.open("https://github.com/yuvraj-singh-027")
        speak("Opening GitHub")

    elif "open amazon" in c:
        webbrowser.open("https://www.amazon.in/s?k=join+amazon+prime&adgrpid=1327112148528381&hvadid=82944775541359&hvbmt=bb&hvdev=c&hvlocphy=254568&hvnetw=o&hvqmt=b&hvtargid=kwd-82945393014646%3Aloc-90&hydadcr=5626_2377281&mcid=3861a9d242543041b997efa1f39279d3&msclkid=6238e7df0e2f113bcbe28e40f378d7b5&tag=msndeskstdin-21&ref=pd_sl_9ntprzamt3_b")
        speak("opening amazon")

    elif "open flipkart" in c:
        webbrowser.open("https://www.flipkart.com/")
        speak("Opening flipkart")

    elif "open microsoft" in c:
        webbrowser.open("https://www.microsoft.com/en-in/?msockid=03b017bf36ba647a074a012e37bc657e")
        speak("Opening microsoft")

    elif "open spotify" in c:
        webbrowser.open("https://open.spotify.com/")
        speak("Opening spotify")

    elif "open quiz" in c:
        webbrowser.open("https://abesquiz.netlify.app/#/access-quiz?req_id=MjAyNi0wMi0yNiNfMjAyNUIxNTMzMDAwMSNfQzNFOSNfMjcxMg%3D%3D")
        speak("Opening quiz")

    elif c.startswith("play"):
        song = c.replace("play", "").strip()

        if song in musiclist.music:
            link = musiclist.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found")

    else:
        # Gemini fallback
        response = llm.invoke(c)
        speak(response)
        print("AI:", response)

print("Initializing Joy")
speak("Initializing Joy")

activated = False

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1,)

    while True:
        try:
            print("Listening...")
            audio = recognizer.listen(source,timeout=2,phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "joy" in word.lower():
                activated = True
                speak("Yes Boss")
                continue


            if activated:
                processcommand(word)
                activated = False

        except Exception as e:
            print("Error:", e)