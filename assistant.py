import pyttsx3
import datetime
import speech_recognition as speech
import time
import games
import wikipedia
import webbrowser
import os
import random

random_index = random.randint(1, 100)

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speakFunc(audio):
    engine.say(audio)
    engine.runAndWait()


def give_your_command():
    """
        Takes the input from the user device microphone and convert it to a string and perform the
        action according to the user command. Just like a Google voice assistant. The Voice command
        sdk is used from `google voice assistants`.
    """
    recognise = speech.Recognizer()  # Initialize the recognizer

    with speech.Microphone() as source:  # used microphone as the source from the user
        print("Listening...")
        recognise.pause_threshold = 1
        recognise.energy_threshold = 400
        audio_get = recognise.listen(source)
        try:  # Tries to recognise the user input from the microphone
            print("Recognising...")
            query = recognise.recognize_google(audio_get, language="en-in")
            print(f"user said : {query} ")
        except Exception as e:  # If the module can't recognise the user input then this exception run
            print("Say that again!")
            print(e)
            return "none"
        # else: If the user didn't do any input then it will throw the else exception with a mess.
        #     print("Sorry! I didn't get anything")
        return query  # returns the query which was said by user


def wishMe():
    """
       Wishes the user from the current time stamp according to the written given logics.
    """
    current_time = int(datetime.datetime.now().hour)  # converted the date time into integer
    if 0 <= current_time < 12:  # If time is under 12 PM
        speakFunc("Good morning! ")
    elif current_time >= 12 and current_time < 12:  # If time is Over 12 PM and smaller 12 AM ( 12hr Timeframe )
        speakFunc("Good afternoon! ")
    else:  # returns the evening.
        speakFunc("Good evening ")
    speakFunc("I'm friday, ")


def user_to_choice():
    user_wish_statement = str(input("What should i have to do > ")).lower()
    choice_command_string = give_your_command().lower()
    if user_wish_statement == "Close":
        speakFunc("I'm exiting from program good bye")
        time.sleep(5)
        exit()
    elif user_wish_statement == "i love you":
        speakFunc("I love you too! .")
        exit()
    elif user_wish_statement == "load game":
        speakFunc("Which game would you want to play, ")
        choice_to_game_user_to_choice = choice_command_string

        """
            I done changes in this block, if program fails to run then you 
            have to check in this block. because, it could be an error in 
            this block . 
        """

        if "sake water gun" in choice_to_game_user_to_choice:
            games.snake_water_gun()
            speakFunc("I'll loaded up snake water gun game for you. Enjoy boss")
        elif "number game" in choice_to_game_user_to_choice:
            games.choose_number_game()
            speakFunc("I'll loaded up number game for you. Enjoy boss.")

        # games.choose_number_game()
        # time.sleep(2)
        # exit()
    else:
        speakFunc("I didn't recognise anything properly")
        time.sleep(1)
        speakFunc("Bye!")
        exit()


# user_to_choice()

# * give_your_command()

if __name__ == "__main__":
    print(__name__)
    wishMe()
    while True:
        query_string = give_your_command().lower()

        if "wikipedia" in query_string:
            speakFunc("Searching wikipedia...")
            query_str = query_string.replace("wikipedia", "")
            results = wikipedia.summary(query_str, sentences=2)
            speakFunc("According to wikipedia...")
            print(results)
            speakFunc(results)
            break

        elif "open my friend profile" in query_string:
            webbrowser.open_new_tab("https://instagram.com/anshichaudhary80")
            speakFunc("Opening google boss")

        elif "shutdown now" in query_string:
            speakFunc("I'm going to sleep now")
            break

        elif "play music" in query_string:
            music_directory = "O:\\About-me\\musics"
            speakFunc("Playing music.")
            music = os.listdir(music_directory)
            print(music)
            music_name = os.listxattr(music[ranodm_index])
            print(music_name)
            os.startfile(os.path.join(music_directory, music[random_index]))

        elif "music" in query_string:
            music_directory = "O:\\About-me\\musics"
            speakFunc("Playing music.")
            music = os.listdir(music_directory)
            print(music)
            os.startfile(os.path.join(music_directory, music[random_index]))
            # ! print(music[random_index])

        elif "time" in query_string:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            speakFunc(f"Boss, the current time is : {current_time}")

        elif "your god" in query_string:
            speakFunc("My sir is my god who develops me")

        elif "open browser computer":
            speakFunc("Opening browser computer for you boss")
            browser.open_new_tab("https://neverinstall.com")