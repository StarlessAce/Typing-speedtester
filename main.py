from tkinter import *
from tkinter.ttk import *
import time
import random

LIST = ['baby',
'front',
'statement',
'horrible',
'bedroom',
'female',
'alike',
'engine',
'scare',
'bewildered',
'coat',
'defeated',
'birthday',
'natural',
'memorize',
'little',
'shrug',
'sprout',
'exist',
'snail',
'unpack',
'wretched',
'double',
'tested',
'tent',
'wistful',
'sordid',
'happen',
'whine',
'economic',
'vest',
'friend',
'impulse',
'scatter',
'men',
'automatic',
'furniture',
'jar',
'amusement',
'ground']

results = [random.choice(LIST), random.choice(LIST), random.choice(LIST)]

list = [word for word in LIST if word not in results]


def show_results(results):
    text_area.config(state=NORMAL)
    text_area.delete(1.0, END)
    for words in results:
        text_area.insert(INSERT, words + '\n')

    text_area.config(state=DISABLED)
    text_area.tag_add('side_words', 1.0, 2.0)
    text_area.tag_add('current_word', 2.0, 3.0)
    text_area.tag_add('side_words', 3.0, 4.0)


def key_press(event):
    key = event.char


def erease_text_area(event):
    input_area.delete(0, 'end')


def refresh_words(event):
    # print(event)
    choice = random.choice(list)
    if len(results) == 3:
        results.remove(results[0])
    results.append(choice)
    show_results(results)
    list.remove(choice)

    show_results(results)


window = Tk()

WIDTH = int(window.winfo_screenwidth()/2)
HEIGHT = int(window.winfo_screenheight()/2)

window.geometry('%dx%d' % (WIDTH, HEIGHT))

# creating layout
text_var = StringVar()

main_frame = Frame(window)
main_frame.pack()

main_title = Label(main_frame, text='Typing speed test', font=('Arial', 16))
main_title.pack(pady=(50,0))
time_label = Label(main_frame, text='Time: ')
time_label.pack(anchor='e', pady=10, padx=5)

text_area = Text(main_frame, font=('Arial', 14), bg='white', width=20, height=3, padx=10, pady=10, wrap=WORD)
text_area.tag_configure(tagName='current_word', justify='center', font=('Arial', 18))
text_area.tag_configure(tagName='side_words', justify='center', font=('Arial', 12))

show_results(results)

text_area.tag_add('side_words', 1.0, 2.0)
text_area.tag_add('current_word', 2.0, 3.0)
text_area.tag_add('side_words', 3.0, 4.0)

text_area.config(state=DISABLED)
text_area.pack(pady=100, anchor='s')

input_area = Entry(main_frame, font=('Arial', 14), width=61, textvariable=text_var)
input_area.pack(pady=5)
input_area.bind('<space>', refresh_words)


window.mainloop()






