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
LIST = ['baby',
'front',
'statement',
'horrible',
'bedroom']

time_start = 0
time_diff = 0
results = [random.choice(LIST), random.choice(LIST)]

list = [word for word in LIST if word not in results]
CORRECT_ANSWERS = []
end_of_list = 0


def start_timer(event=None):
    global time_start
    time_start = time.time()


def stop_timer(event=None):
    global time_diff
    time_stop = time.time()
    time_diff = time_start - time_stop
    print('tutej')


def game_finish():
    text_area.config(state=NORMAL)
    text_area.delete(1.0, 3.0)
    text_area.insert(INSERT, 'KONIEC')
    text_area.tag_add('current_word', 1.0, 3.0)
    text_area.config(state=DISABLED)

    print('tutejs')

def show_results(results):
    text_area.config(state=NORMAL)
    text_area.delete(1.0, END)
    if len(results) == 3:
        pass
    else:
        results.insert(0, '')
    for words in results:
        text_area.insert(INSERT, words + '\n')

    text_area.config(state=DISABLED)
    text_area.tag_add('side_words', 1.0, 2.0)
    text_area.tag_add('current_word', 2.0, 3.0)
    text_area.tag_add('side_words', 3.0, 4.0)


def check_word():
    word = text_var.get()
    word = word.strip()
    if word == results[0]:
        text_area.tag_add('correct_answer', 1.0, 2.0)
        CORRECT_ANSWERS.append(word)
    else:
        text_area.tag_add('incorrect_answer', 1.0, 2.0)


def key_press(event):
    key = event.char


def erease_text_area(event=None):
    input_area.delete(0, 'end')
    # position = input_area.index(INSERT)
    # input_area.icursor(3)
    # position = input_area.index(INSERT)


def refresh_words(event):
    global end_of_list

    try:
        choice = random.choice(list)
    except IndexError:
        choice = ''

    if len(results) == 3:
        results.remove(results[0])
    results.append(choice)

    show_results(results)
    check_word()
    erease_text_area(event)
    try:
        list.remove(choice)
    except ValueError:
        end_of_list += 1

    if end_of_list == 2:
        stop_timer()
        game_finish()


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

text_area = Text(main_frame, font=('Arial', 14), bg='white', width=20, height=4, padx=10, pady=20, wrap=WORD)
text_area.tag_configure(tagName='current_word', justify='center', font=('Arial', 22))
text_area.tag_configure(tagName='side_words', justify='center', font=('Arial', 12))
text_area.tag_configure(tagName="correct_answer", justify='center', font=('Arial', 12), foreground='green')
text_area.tag_configure(tagName="incorrect_answer", justify='center', font=('Arial', 12), foreground='red')

show_results(results)

text_area.tag_add('side_words', 1.0, 2.0)
text_area.tag_add('current_word', 2.0, 3.0)
text_area.tag_add('side_words', 3.0, 4.0)

text_area.config(state=DISABLED)
text_area.pack(pady=10, anchor='s')

input_area = Entry(main_frame, font=('Arial', 14), width=20, textvariable=text_var, justify=CENTER)
input_area.pack(pady=5)
# input_area.place(width=180, height=60, anchor='center')
run = 10
start = time.time()

input_area.bind('<Return>', refresh_words)
input_area.bind('<space>', refresh_words)
input_area.bind('<FocusIn>', start_timer)

window.mainloop()






