import my_audio
import my_text_convert
import my_translator

langauge1 = "Chinese"
langauge2 = "Korean"

print(f"Default language is {langauge1} and {langauge2}. Click 1 to change, else click 0")
if input() == "1":
    langauge1 = input("Enter the first language: ")
    langauge2 = input("Enter the second language: ")

print(f"Instructions:\n(1) Click '1' to speak in {langauge1} and click '2' to speak in {langauge2}.")
print("(2) When finished peaking, hit control c")
print("(3) Repeat as many times as needed")

while True:
    translate_to = langauge2
    user_input = input()
    if user_input == "2":
        translate_to = langauge1

    # Start recording
    my_audio.record()
                       
    # Read the recorded file and return the text
    text = my_text_convert.converter()

    # Translate text
    my_translator.get_translation(text,translate_to)
