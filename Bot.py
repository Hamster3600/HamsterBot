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
        icon = pystray.Icon("name", image, "My App", menu)
        icon.run()

    def quit_window(self, icon):
        icon.stop()
        self.destroy()
    
    def listen_window(self, icon):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                
                print(MyText)

                if MyText == ("open whatsapp"):
                    open("whatsapp")
                elif MyText == ("close whatsapp"):
                    close("whatsapp")

                elif MyText == ("open steam"):
                    open("Steam")
                elif MyText == ("close steam"):
                    close("Steam")

                elif MyText == ("open firefox"):
                    open("Firefox")
                elif MyText == ("close firefox"):
                    close("Firefox")

                elif MyText == ("open notebook"):
                    open("Notatnik")
                elif MyText == ("close notebook"):
                    close("Notatnik")
                     
                elif MyText == ("open discord"):
                    open("Discord")
                elif MyText == ("close discord"):
                    close("Discord") 

                    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
         
        except sr.UnknownValueError:
            print("unknown error occurred")

    def hotkey_pressed():
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                    
                print(MyText)

                if MyText == ("open whatsapp"):
                    open("whatsapp")
                elif MyText == ("close whatsapp"):
                    close("whatsapp")

                elif MyText == ("open steam"):
                    open("Steam")
                elif MyText == ("close steam"):
                    close("Steam")

                elif MyText == ("open firefox"):
                    open("Firefox")
                elif MyText == ("close firefox"):
                    close("Firefox")

                elif MyText == ("open notebook"):
                    open("Notatnik")
                elif MyText == ("close notebook"):
                    close("Notatnik")         
                        
                elif MyText == ("open discord"):
                    open("Discord")
                elif MyText == ("close discord"):
                    close("Discord") 

                        
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")

    keyboard.add_hotkey('F8', hotkey_pressed) 
            

    def show_window(self, icon):
        icon.stop()
        self.after(0,self.deiconify)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()