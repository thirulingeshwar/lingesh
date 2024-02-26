import time
import webbrowser
import pyttsx3
import wikipedia
import pygame
import os
import pandas as pd # Adding pandas for handling CSV files

engine = pyttsx3.init()
pygame.mixer.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond(message):
    print("LVAI :", message)
    time.sleep(0)  # Simulating a delay
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            respond(f"Here is the content of '{filename}':")
            print(content)
            speak(content)
    except FileNotFoundError:
        respond(f"Sorry, I couldn't find the file '{filename}'.")
    except Exception as e:
        respond("An error occurred while opening the file.")

def write_to_file(filename, text_to_write):
    try:
        with open(filename, 'w') as file:
            file.write(text_to_write)
        respond(f"Text written to '{filename}' successfully.")
    except Exception as e:
        respond(f"An error occurred while writing to the file '{filename}'.")

def play_song(song_name):
    song_path = f"songs/{song_name}.mp2"  # Assuming the songs are in a folder named "songs"
    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except FileNotFoundError:
        respond(f"Sorry, I couldn't find the song '{song_name}'.")
    except Exception as e:
        respond("An error occurred while playing the song.")

def open_data(data_filename):
    try:
        data = pd.read_csv(data_filename)  # Assuming CSV format
        respond(f"Successfully opened '{data_filename}'.")
        print(data)
        speak("Data file opened successfully.")
    except FileNotFoundError:
        respond(f"Sorry, I couldn't find the data file '{data_filename}'.")
    except Exception as e:
        respond("An error occurred while opening the data file.")

def open_and_read_file(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Sorry, I couldn't find the file '{filename}'."
    except Exception as e:
        return "An error occurred while opening the file."

def main():
    respond("Hello! I'm your virtual assistant, LVAI APP.")
    speak("Hello! I'm your virtual assistant, LVAI APP.")

    while True:
        user_input = input("You: ").lower()

        if "open" in user_input and "google" in user_input:
            respond("Opening Google...")
            time.sleep(1)
            webbrowser.open("https://www.google.com")
            respond("Google is opened.")
            speak('Google is opened.')

        elif "open" in user_input and "youtube" in user_input:
            respond("Opening YouTube...")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com")
            respond("YouTube is opened.")
            speak('YouTube is opened.')

        elif "open" in user_input and "gpt" in user_input:
            respond("Opening GPT...")
            time.sleep(1)
            webbrowser.open("https://chat.openai.com/")
            respond("GPT is opened.")
            speak('GPT is opened.')

        elif "search" in user_input:
            query = user_input.replace("search wikipedia", "").strip()
            try:
                summary = wikipedia.summary(query, sentences=0)
                respond(f"Here is what I found on Wikipedia: {summary}")
                speak(summary)
            except wikipedia.exceptions.DisambiguationError:
                respond("There are multiple possible articles. Please provide more specific input.")
            except wikipedia.exceptions.PageError:
                respond("Sorry, I couldn't find anything on Wikipedia.")

        elif "open file in read" in user_input:
            filename = user_input.replace("open file", "").strip()
            open_file(filename)

        elif "play song" in user_input:
            song_name = user_input.replace("play song", "").strip()
            play_song(song_name)

        elif "open data" in user_input:
            data_filename = user_input.replace("open data", "").strip()
            open_data(data_filename)

        elif "open and read file" in user_input:
            filename = input("Enter the file address: ")
            file_content = open_and_read_file(filename)

            if isinstance(file_content, bytes):
                print("File content (in bytes):", file_content)
            else:
                print("File content (decoded as text):\n", file_content)
                
        elif "what is your name" in user_input:
            respond('my name is lvai app')
            speak('my name is lvai app')
            
        elif ("000111111111111000000010000001000000000000000000111000000000000010010000001000000000000000000111000000000000010010000001000001000000000000111000000000000010010000001000001000000000000111000000000000010010000001000001000000000000111111110000000010010001001000001000000000")  in user_input:
            respond('it is jarvis cord error, this error is called no net error. net worke is have a problaim so it is the error so soleard is the net not worke.')
            speak('it is jarvis cord error, this error is called no net error. net worke is have a problaim so it is the error so soleard is the net not worke.')

        elif "what is lvai app" in user_input:
            respond('LVAI lingesh voise assistant artificial intelligence app')
            speak('LVAI lingesh voise assistant artificial intelligence app')

        elif "what is leo" in user_input:
            respond('LEO lingesh eagle voise')
            speak('LEO.lingesh eagle voise')

        elif "what is your boss name" in user_input:
            respond('thirulingeshwar')
            speak('thirulingeshwar')
            
        elif"search .sex" in user_input:
            respond('sorry it is 17+ data')
            speak('sorry it is 17+ data')

        elif "goodbye" in user_input or "bye" in user_input:
            respond("Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
            break
        else:
            respond("I'm sorry, I don't have the capability to respond to that command.")

if __name__ == "__main__":
    main()

