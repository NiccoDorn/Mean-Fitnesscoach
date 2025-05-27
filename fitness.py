import random
import pyttsx3
import time

eng = pyttsx3.init()

def speak(text):
    eng.say(text)
    eng.runAndWait()
    
def trainierDuPudding(exs):
    for i in range(20):
        if i == 9: speak("10 geschafft.")
        c = random.choice(list(exs.keys())) # kein Auswendiglernen!
        cmd = exs[c]
        output = f"{c}!"
        speak(output)
        time.sleep(2)
    speak("Durchlauf fertig.")

def main():
    cs = ["Rot", "Blau", "Grün", "Gelb"]
    exsl = ["Kniesprung", "Kniebeuge", "Liegestütze", "Links Rechts Sprung"]
    random.shuffle(exsl)
    exs = dict(zip(cs, exsl))
    
    speak("So, das Training beginnt. Abfahrt! Ihr Pudding-Behälter.")
    for c, exercise in exs.items(): # einmalige Ansage, man muss sich das Mapping merken
        speak(f"{c} bedeutet: {exercise}.")
        # print(f"{c} bedeutet: {exercise}.")
        
    # wie Antoine Burz schon sagte: Trrrrainieren!
    speak("In 3 Sekunden geht es los. Nicht einpennen.")
    time.sleep(3)
    trainierDuPudding(exs)
    speak("Macht nicht schlapp ihr faulen Säcke. 10 Sekunden Pause, dann geht es weiter.")
    time.sleep(10)
    speak("Hopp jetzt.")
    trainierDuPudding(exs)
    
    # das nicht nicht das Ende!
    speak("War doch gar nicht so schwer, ihr Waschlappen.")
    speak("Gut gemacht und nicht vergessen: Geschlemmt wird nicht!")
    
if __name__ == '__main__':
    main()
