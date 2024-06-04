#Concept:
The concept for this project is to be able to build a raspberry pi translator that can fit in a pocket. The tool would just be a casing for the pi
with two buttons on it. and with the ablity to connect it to a computer to change the langauges being used. This repository is proof of concept.
The goal is to be able to have two buttons, for two people, and two languges. For example and english speaking person and a spanish speaking person. The 
English person can click the buttonfor talking in english, then the pi will read out the spanish translation, and with simalr results when spanish
person clicks the other button to speak in spanish.

#Technicals:
All AI is being accesed through request API's. This is because the small PI's are very limited in what they can run, they also cannot run Cpython, and just run 
micropython, thankfully request (called Urequest) can be used on the pi.
When a user clicks the button, it records the voice, then uses Meta's wav2vec2 model to translate it. It is supposed to be good enough to translate what 
ever langauge is spoken, however, I am having issues wiht this. Then we convert the wav file to text. This file then is sent to chatgpt with the promt
of converting it to the correct languge. I think ChatGPT give the most natural translations. 
I am actully not a fan of wav2vec2, and thinkg using ChatGPT Wisper might be better option
