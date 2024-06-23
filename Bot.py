import speech_recognition as sr
import pyttsx3 
from tkinter import *
from AppOpener import open, close
import tkinter as tk
import pystray
from PIL import Image
import keyboard
import getpass
import os
from pathlib import Path


r = sr.Recognizer() 
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
  
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hamster Bot")
        self.geometry('500x250')
        self.protocol('WM_DELETE_WINDOW', self.minimize_to_tray)
    
    def minimize_to_tray(self):
        self.withdraw()
        image_path = Path(__file__).absolute().parent / "hamster2.png"
        image = Image.open(image_path)
        menu = (pystray.MenuItem('Quit',  self.quit_window), 
                pystray.MenuItem('Listen',self.listen_window),
                pystray.MenuItem('Show',self.show_window),)
        self.icon = pystray.Icon("name", image, "My App", menu)
        self.icon.run()

    def quit_window(self):
        self.icon.stop()
        self.destroy()
    
    def listen_window(self, icon):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                
                print(MyText)

                match MyText:
                    case "open whatsapp":
                        open("whatsapp")
                    case "close whatsapp":
                        close("whatsapp")
                    case "open steam":
                        open("Steam")
                    case "close steam":                                 
                        close("Steam")
                    case "open firefox":
                        open("Firefox")
                    case "close firefox":
                        close("Firefox")
                    case "open notebook":
                        open("Notatnik")
                    case "close notebook":
                        close("Notatnik")
                    case "open discord":
                        open("Discord")
                    case "close discord":
                        close("Discord") 
                    case "quit":
                        icon.stop()
                        self.destroy()
    
                    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
         
        except sr.UnknownValueError:
            print("unknown error occurred")

    def show_window(self):
        self.icon.stop()
        self.after(0,self.deiconify)


def hotkey_pressed(app):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
                
            print(MyText)

            match MyText:
                case "open whatsapp":
                    open("whatsapp")
                case "close whatsapp":
                    close("whatsapp")
                case "open steam":
                    open("Steam")
                case "close steam":                                 
                    close("Steam")
                case "open firefox":
                    open("Firefox")
                case "close firefox":
                    close("Firefox")
                case "open notebook":
                    open("Notatnik")
                case "close notebook":
                    close("Notatnik")
                case "open discord":
                    open("Discord")
                case "close discord":
                    close("Discord")  
                case "quit":
                    app.quit_window()
                    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")

if __name__ == "__main__":
    app = MyApp()
    keyboard.add_hotkey('F8', hotkey_pressed, args=(app,)) 
    app.mainloop()