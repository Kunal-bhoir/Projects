import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

client = wolframalpha.Client("K52833-GP4TQHL8YT")
engine = pyttsx3.init()
engine.setProperty('rate', 140)

sg.theme('DarkPurple')	
layout = [   [sg.Text('Ask something: '), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Virtual Assist', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    res = client.query(values[0])
    wolfram_res = next(res.results).text
    Wiki_res = wikipedia.summary(values[0], sentences=1)           
    sg.PopupNonBlocking("wolfram_res: "+ wolfram_res,"Wiki_res: "+Wiki_res)
    engine.say(wolfram_res)
    engine.say(Wiki_res)
    engine.runAndWait()

window.close()