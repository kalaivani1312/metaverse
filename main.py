import speech_recognition as sr
import pyttsx3
import datetime



listener = sr.Recognizer()
engine = pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

    except:
        pass
    return command


def run_alexa():
    command = take_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'hello' in command:
        talk('what can i do for you')
    elif 'what is the latest version of app' in command:
        talk('its 2.4')
    elif 'if it have subscription' in command:
        talk('yeah ,its upto 2000 rupees per month ')
    elif 'name' in command:
        talk('i am joy synthetic avater ')
    elif 'what is the renewal date' in command:
        talk('you have  to renewal every three month from your subscription date ')
    elif 'thank you' in command:
        talk('your welcome meet you later ')
    elif 'what is your speciality' in command:
        talk('i am specially design to meet your needs  ')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
