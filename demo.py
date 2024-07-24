import speech_recognition as sr
import pyttsx3 
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.") 
        speak("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, I could not process the request. Try again later.")
        speak("Sorry, I could not process the request. Try again later.")

def main():
    while True:
        command = listen()
        if not command:
            continue

        if "hello" in command:
            speak("Hey there! How can I assist you?")
        elif "how are you" in command:
            speak("I'm just a computer program, but thank you for asking. If I can help with anything, just ask.")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}.")
            print("Time:", current_time)
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"The date is {current_date}.")
            print("Date:", current_date)
        elif "open youtube" in command:
            speak("Ok! Opening YouTube.")
            print("Open YouTube")
            webbrowser.open("https://youtube.com")
        elif "open google" in command:
            speak("Ok! Opening Google.")
            print("Open Google")
            webbrowser.open("https://google.com")
        elif "play music" in command:
            speak("Here you go! Opening Spotify.")
            print("Play music")
            webbrowser.open("https://spotify.com")
        elif "search" in command:
            query = command.split("search", 1)[1].strip()
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}.")
            webbrowser.open(url)
        elif "exit" in command:
            speak("Goodbye! Have a great day!")
            print("Exit")
            break
        else:
            speak("Sorry, I didn't catch that. Can you please repeat?")

if __name__ == "__main__":
    main()





    