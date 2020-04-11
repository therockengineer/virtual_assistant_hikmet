# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:54:54 2020

@author: Ahmet
"""

import wolframalpha
client = wolframalpha.Client("hikmetindensualolunmaz")

import wikipedia

import pyttsx3
engine = pyttsx3.init()

import PySimpleGUI as psg
psg.theme('Green')
layout =[[psg.Text('Ask me, Majesty!'), psg.InputText()],[psg.Button('Ok'), psg.Button('Cancel')]]
window = psg.Window('PyDa', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        psg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        psg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        psg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        psg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])

window.close()