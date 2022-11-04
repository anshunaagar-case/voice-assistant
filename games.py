import pyttsx3
import datetime
import speech_recognition as speech
import time
import random
import games

random_number = random.randint(1, 10)

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speakFunc(audio):
    engine.say(audio)
    engine.runAndWait()


def choose_number_game():
    chances_to_play = 10
    speakFunc("You have 10 chances. good luck!")
    get_number_input = int(input("Enter your number : "))
    while True:
        if get_number_input < random_number:
            speakFunc("You choose a wrong number! Try again")
            chances_to_play -= 1
            get_number_input = int(input("Enter your number : "))
        elif get_number_input == random_number:
            speakFunc("You won. Congratulations!")
            break
        elif chances_to_play == 0:
            speakFunc("You lost your chances!")
            break
        elif get_number_input > random_number:
            speakFunc("You choose a wrong number! Try again")
            chances_to_play -= 1
            get_number_input = int(input("Enter your number : "))


def snake_water_gun():
    content_list_snake_water_gun = ["snake", "water", "gun"]
    snake_water_gun_random_number = random.choice(content_list_snake_water_gun).lower()
    print(snake_water_gun_random_number)
    player_input_snake_water_gun = str(input(f"Choose your option {content_list_snake_water_gun} : "))
    speakFunc("You will play against me, Let's play man")
    chances_to_play = 10

    while chances_to_play:
        computer_chance = 0
        player_chance = 0
        if snake_water_gun_random_number == player_input_snake_water_gun:
            player_chance += 1
            print(f"Aya bro, you got {player_chance}")

        else:
            break


if __name__ == "__main__":
    snake_water_gun()
