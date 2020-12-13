import speech_recognition as sr
import pyttsx3 as tts

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
    print("going to talk back the command...")
    talk(command)


process_command()



