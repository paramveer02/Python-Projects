import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('How can i help you?')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'siri' in command:
                command=command.replace('siri','')
                print(command)
    except:
        pass
    return command

def run_siri():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing your requested song'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        talk('Current time is '+time)
        print(time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with paramveer')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    # else:
    #     talk('Please repeat the command again')


run_siri()



