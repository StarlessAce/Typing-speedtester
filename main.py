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
    for word in range(0, length-2):
        x = random.choice(list)
        while x not in game_list:
            game_list.append(x)


def start_timer(event=None):
    global time_start
    time_start = time.time()


def stop_timer(event=None):
    global time_diff, GAME_STARTED
    time_stop = time.time()
    time_diff = time_stop - time_start
    return time_diff


def update_results(time):
    print(CORRECT_ANSWERS)
    words_count = len(CORRECT_ANSWERS)
    chars_count = sum(len(word) for word in CORRECT_ANSWERS)

    wpm = words_count*60/time
    cpm = chars_count*60/time

    time_result_label.config(text='%.2f' % time + 's')
    wpm_result_label.config(text='%.2f' % wpm)
    cpm_result_label.config(text=str('%.2f' % cpm))


def game_start():
    text_area.config(state=NORMAL)
    text_area.insert(3.0, "PRESS 'START' TO BEGIN")
    text_area.tag_add('current_word', 1.0, 3.0)
    text_area.config(state=DISABLED)


def game_finish():
    text_area.config(state=NORMAL)
    text_area.delete(1.0, 3.0)
    text_area.insert(INSERT, 'FINISH')
    text_area.tag_add('current_word', 1.0, 3.0)
    text_area.config(state=DISABLED)

    input_area.config(state=DISABLED)
    words_number_button.config(state=NORMAL, text='Play again')

    time_result = stop_timer()
    update_results(time_result)
    reset_game()


def reset_game():
    global results, list, game_list, CORRECT_ANSWERS, end_of_list, time_start, time_diff, first_random, second_random

    first_random = random.choice(LIST)
    second_random = random.choice(LIST)
    while first_random == second_random:
        second_random = random.choice(LIST)
    results = [first_random, second_random]
    list = [word for word in LIST if word not in results]
    game_list = []
    CORRECT_ANSWERS = []
    end_of_list = 0
    time_start = 0

def show_words():
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


def erase_text_area(event=None):
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

    show_words()
    check_word()
    erase_text_area(event)

    try:
        game_list.remove(choice)
    except ValueError:
        end_of_list += 1

    if end_of_list == 2:
        game_finish()


window = Tk()

WIDTH = int(window.winfo_screenwidth()/3)
HEIGHT = int(window.winfo_screenheight()/1.5)

window.geometry('%dx%d' % (WIDTH, HEIGHT))
window.config(pady=50)

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

words_number_picker = Scale(settings_frame, variable=words_number, from_=3, to=len(LIST), orient='horizontal', state='normal', length=240)
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

input_area = Entry(game_frame, font=('Arial', 14), width=20, textvariable=text_var, justify=CENTER, state=DISABLED)
input_area.pack(pady=5)

words_number_button = Button(game_frame, text='Start', width=33, height=3, command=lambda: [game_length(), show_words(), input_area.config(state=NORMAL), words_number_button.config(state=DISABLED, text='Play!'), start_timer(), input_area.focus_set()])
words_number_button.pack(pady=(20,20), anchor='center')

results_frame = Frame(game_frame)
results_frame.pack(anchor='w')

time_label = Label(results_frame, text='Your time:')
time_label.grid(row=0, column=0, pady=4, sticky='w')
time_result_label = Label(results_frame, text='')
time_result_label.grid(row=0, column=1, pady=4, sticky='w')

wpm_label = Label(results_frame, text='Your WPM result:')
wpm_label.grid(row=1, column=0, pady=4, sticky='w')
wpm_result_label = Label(results_frame, text='')
wpm_result_label.grid(row=1, column=1, pady=4, sticky='w')

cpm_label = Label(results_frame, text='Your CPM result:')
cpm_label.grid(row=2, column=0, pady=4, sticky='w')
cpm_result_label = Label(results_frame, text='')
cpm_result_label.grid(row=2, column=1, pady=4, sticky='w')

# input_area.place(width=180, height=60, anchor='center')

input_area.bind('<FocusIn>', start_timer)
input_area.bind('<Return>', refresh_words)
input_area.bind('<space>', refresh_words)

window.mainloop()






