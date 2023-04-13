from tkinter import *
# from tkinter.ttk import *
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
first_random = random.choice(LIST)
second_random = random.choice(LIST)
while first_random == second_random:
    second_random = random.choice(LIST)
results = [first_random, second_random]


list = [word for word in LIST if word not in results]
game_list = []
CORRECT_ANSWERS = []
end_of_list = 0


def game_length():
    length = words_number.get()
    for word in range(0, length-1):
        x = random.choice(list)
        while x not in game_list:
            game_list.append(x)
    print(game_list)


def start_timer(event=None):
    global time_start
    time_start = time.time()


def stop_timer(event=None):
    global time_diff
    time_stop = time.time()
    time_diff = time_start - time_stop


def game_start():
    text_area.config(state=NORMAL)
    text_area.insert(3.0, "PRESS 'START' TO BEGIN")
    text_area.tag_add('current_word', 1.0, 3.0)
    text_area.config(state=DISABLED)


def game_finish():
    text_area.config(state=NORMAL)
    text_area.delete(1.0, 3.0)
    text_area.insert(INSERT, 'KONIEC')
    text_area.tag_add('current_word', 1.0, 3.0)
    text_area.config(state=DISABLED)


def show_results():
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
        choice = random.choice(game_list)
    except IndexError:
        choice = ''

    if len(results) == 3:
        results.remove(results[0])
    results.append(choice)

    show_results()
    check_word()
    erease_text_area(event)
    try:
        game_list.remove(choice)
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
words_number = IntVar()

settings_frame = Frame(window)
settings_frame.pack()

game_frame = Frame(window)
game_frame.pack()


main_title = Label(settings_frame, text='Typing speed test', font=('Arial', 16))
main_title.pack(pady=(50,10))
# time_label = Label(main_frame, text='Time: ')
# time_label.pack(anchor='e', pady=10, padx=5)

words_number_label = Label(settings_frame, text='Choose number of words to type:')
words_number_label.pack(pady=1, anchor='w')

words_number_picker = Scale(settings_frame, variable=words_number, from_=1, to=len(LIST), orient='horizontal', state='normal', length=240)
words_number_picker.pack(pady=1, anchor='center')

text_area = Text(game_frame, font=('Arial', 14), bg='white', width=20, height=4, padx=10, pady=20, wrap=WORD)
text_area.tag_configure(tagName='current_word', justify='center', font=('Arial', 22))
text_area.tag_configure(tagName='side_words', justify='center', font=('Arial', 12))
text_area.tag_configure(tagName="correct_answer", justify='center', font=('Arial', 12), foreground='green')
text_area.tag_configure(tagName="incorrect_answer", justify='center', font=('Arial', 12), foreground='red')

# show_results(results)
game_start()

text_area.tag_add('side_words', 1.0, 2.0)
text_area.tag_add('current_word', 2.0, 3.0)
text_area.tag_add('side_words', 3.0, 4.0)

text_area.config(state=DISABLED)
text_area.pack(pady=10, anchor='s')

entry_label = Label(game_frame, text='Type the words below:')
entry_label.pack(pady=1, anchor='w')

input_area = Entry(game_frame, font=('Arial', 14), width=20, textvariable=text_var, justify=CENTER)
input_area.pack(pady=5)

words_number_button = Button(game_frame, text='Start', width=33, height=3, command=lambda: [game_length(), show_results()])
words_number_button.pack(pady=(20,20), anchor='center')

print(results)

# input_area.place(width=180, height=60, anchor='center')
run = 10
start = time.time()

input_area.bind('<Return>', refresh_words)
input_area.bind('<space>', refresh_words)
input_area.bind('<FocusIn>', start_timer)

window.mainloop()






