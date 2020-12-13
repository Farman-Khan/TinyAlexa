import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia as wikki

listener = sr.Recognizer()
engine = tts.init()

# setting female voice
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def talk(msg):
    engine.say(msg)
    engine.runAndWait()


def take_user_command():
    try:
        with sr.Microphone() as source:
            print("listening for the input voice...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            if 'alexa' or 'Alexa' in command:
                print(command)

    except:
        print("Got Exception...")
        pass
    return command


def process_command():
    command = take_user_command()

    if 'play' or 'song' in command:
        pywhatkit.playonyt(command)
    elif 'time' or 'Time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk("Current Time is " + time)

    elif 'about' in command:
        info = wikki.summary(command, 1)
        print(info)
        talk(info)


while True:
    process_command()



