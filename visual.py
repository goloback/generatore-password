import time
from tkinter import *
from OptionsView import optionsView
from date_information import Date_information
from main import Generate_password
import pyperclip
from datetime import datetime
numbers_tick = True
letters_tick = True
LETTERS_tick = True
sympols_tick = True

def save_password(event):
    if len(pass_entry.get()) == 0:
        return
    today = datetime.now()
    file_name = f'{today.year} {today.month} {today.day} {today.minute} {today.second}'
    with open(f'{file_name}.txt', 'w') as file:
        file.write(f'{file_name}: {pass_entry.get()}')
    canvas.itemconfigure(save, image=save_click_img)
    canvas.update_idletasks()
    canvas.update()
    time.sleep(0.5)
    canvas.itemconfigure(save, image=saveimg)
def copy_password(event):
    if len(pass_entry.get()) == 0:
        return
    pyperclip.copy(pass_entry.get())
    canvas.itemconfigure(copy, image=copy_click_img)
    canvas.update_idletasks()
    canvas.update()
    time.sleep(0.5)
    canvas.itemconfigure(copy, image=copyimg)

global click_tick, change_tick, click_options, create_options
error_text = None
date_information = Date_information(error_text)

def click_tick(main_canva, tick, value):
    global numbers_tick, letters_tick, LETTERS_tick, sympols_tick
    if value == 1:
        numbers_tick = not numbers_tick
        change_tick(canvas_numbers, tick_number, numbers_tick)
    elif value == 2:
        letters_tick = not letters_tick
        change_tick(canvas_letters, tick_letters, letters_tick)
    elif value == 3:
        LETTERS_tick = not LETTERS_tick
        change_tick(canvas_LETTERS, tick_LETTERS, LETTERS_tick)
    elif value == 4:
        sympols_tick = not sympols_tick
        change_tick(canvas_sympols, tick_sympols, sympols_tick)

def change_tick(main_canva, tick, value):
    if value == True:
        main_canva.itemconfigure(tick, image=tick_green)
        create_options()
    else:
        main_canva.itemconfigure(tick, image=tick_white)
        destroy_option()

def click_options(event):
    global is_options, text_len_pass, len_password_entry
    if is_options == True:
        is_options = False
        canvas.itemconfigure(options, image=plus_image)
        destroy_option()
        text_len_pass = canvas.create_text(10, 220, text='password length', font=('Comic Sans MS', 16), fill='#75c6ba',
                                           anchor=NW)
        len_password_entry = Entry(canvas, font=('Comic Sans MS', 15), width=3, validate='key',
                                   validatecommand=(registered_validation_len_password, '%P'))
        len_password_entry.place(x=180, y=220)
    else:
        canvas.itemconfigure(options, image=minus_image)
        canvas.delete(text_len_pass)
        is_options = True
        create_options()
        len_password_entry.destroy()
        len_password_entry = None

def create_options():
    global plus_number, plus_letters, plus_LETTERS, plus_sympols
    if plus_number is None and numbers_tick == True and is_options == True:
        plus_number = optionsView(canvas, 254, window, 'numbers', date_information)
    if plus_letters is None and letters_tick == True and is_options == True:
        plus_letters = optionsView(canvas, 289, window, 'letters', date_information)
    if plus_LETTERS is None and LETTERS_tick == True and is_options == True:
        plus_LETTERS = optionsView(canvas, 324, window, 'LETTERS', date_information)
    if plus_sympols is None and sympols_tick == True and is_options == True:
        plus_sympols = optionsView(canvas, 359, window, 'sympols', date_information)

def destroy_option():
    global plus_number, plus_letters, plus_LETTERS, plus_sympols
    if plus_number is not None and (is_options == False or numbers_tick == False):
        date_information.amount_numbers = 0
        plus_number.destroy()
        plus_number = None
    if plus_letters is not None and (is_options == False or letters_tick == False):
        plus_letters.destroy()
        date_information.amount_letters = 0
        plus_letters = None
    if plus_LETTERS is not None and (is_options == False or LETTERS_tick == False):
        plus_LETTERS.destroy()
        date_information.amount_LETTERS = 0
        plus_LETTERS = None
    if plus_sympols is not None and (is_options == False or sympols_tick == False):
        plus_sympols.destroy()
        date_information.amount_sympols = 0
        plus_sympols = None

def validation_len_password(try_number):
    global error_text
    if is_options == True and len(try_number) == 0:
        return True
    if is_options == True:
        return False
    if len(try_number)==0:
        return True
    if len(try_number)>2:
        return False
    if try_number == '0':
        return False
    if  try_number.isdigit():
        if error_text is not None:
            error_text.destroy()
            error_text = None
        return True

def validation_entry_password(try_anything):
    return disable
disable = False
correct_form = True
def click_generate_password():
    global correct_form, error_text
    # inert password len is correct
    if is_options == False and len(len_password_entry.get()) == 0:
        correct_form = False
    elif is_options == True and ((plus_number is None or len(plus_number.entry.get()) == 0)
                                 and (plus_letters is None or len(plus_letters.entry.get()) == 0)
                                 and (plus_LETTERS is None or len(plus_LETTERS.entry.get()) == 0)
                                 and (plus_sympols is None or len(plus_sympols.entry.get()) == 0)):
        correct_form = False
    else:
        correct_form = True
    if correct_form == True:
        generate_password()
    else:
        if error_text is None:
            error_text = Label(canvas, text='write correct password length', bg='#9f6fde', fg='red', font=('Comic Sans MS', 15))
            error_text.place(x=400, y=300)
            date_information.error_message = error_text
        else:
            error_text['text']='write correct password length'
            error_text.place(x=400, y=300)

def generate_password():
    global disable
    password = Generate_password()
    if len_password_entry is not None:
        password.pass_len = int(len_password_entry.get())
    password.numbers_amount = 0
    password.letters_amount = 0
    password.LETTERS_amount = 0
    password.sympol_amount = 0
    types = []
    if numbers_tick == True:
        types.append('numbers')
        if plus_number is not None and len(plus_number.entry.get()) > 0:
            password.numbers_amount = int(plus_number.entry.get())
        else:
            password.numbers_amount = 0
    if letters_tick == True:
        types.append('letters')
        if plus_letters is not None and len(plus_letters.entry.get()) > 0:
            password.letters_amount = int(plus_letters.entry.get())
        else:
            password.letters_amount = 0
    if LETTERS_tick == True:
        types.append('LETTERS')
        if plus_LETTERS is not None and len(plus_LETTERS.entry.get()) > 0:
            password.LETTERS_amount = int(plus_LETTERS.entry.get())
        else:
            password.LETTERS_amount = 0
    if sympols_tick == True:
        types.append('sympols')
        if plus_sympols is not None and len(plus_sympols.entry.get()) > 0:
            password.sympol_amount = int(plus_sympols.entry.get())
        else:
            password.sympol_amount = 0
    if is_options == False:
        if len(types) == 1:
            password.generator_only_one_type_password(types[0])
        elif len(types) == 2:
            password.generator_two_types_password(types[0], types[1])
        elif len(types) == 3:
            password.generator_three_types_password(types[0], types[1], types[2])
        elif len(types) == 4:
            password.generator_four_types_password()
    else:
        password.amount_generator()
    disable = True
    pass_entry.delete(0, END)
    pass_entry.insert(0, password.password)
    disable = False

def generate_one_type_password(password, type):
    global disable
    password.generator_only_one_type_password(type)
    disable = True
    pass_entry.delete(0, END)
    pass_entry.insert(0, password.password)
    disable = False



str_title = 'generator'
window = Tk()
window.geometry('700x400+400+200')
window.resizable(0, 0)
window.title(str_title)
registered_validation_len_password = window.register(validation_len_password)
registered_validation_entry_password = window.register(validation_entry_password)
canvas = Canvas(window, width=700, height=400, bg='#9f6fde')
canvas.pack()
copyimg = PhotoImage(file='copy.png')
copy_click_img = PhotoImage(file='click_copy.png')
copy = canvas.create_image(550, 100, anchor=NW, image=copyimg)
saveimg = PhotoImage(file='save.png')
save_click_img = PhotoImage(file='click_save.png')
save = canvas.create_image(120, 100, anchor=NW, image=saveimg)
canvas.tag_bind(copy, '<Button-1>', copy_password)
canvas.tag_bind(save, '<Button-1>', save_password)
# password length
canvas.create_text(250, 20, anchor=NW, text=str_title, font=('Comic Sans MS', 30), fill='#97c6c7')
pass_entry = Entry(canvas, font=('Comic Sans MS', 25), width=18, validate='key',
                   validatecommand=(registered_validation_entry_password, '%P'))
pass_entry.place(x=170, y=100)
generator_button = Button(canvas, font=('Comic Sans MS', 20), bg='#bf7fdf', fg='#97c6c7', text='generate', command=click_generate_password)
generator_button.place(x=270, y=160)
text_len_pass = canvas.create_text(10, 220, text='password length', font=('Comic Sans MS', 16), fill='#75c6ba', anchor=NW)
len_password_entry = Entry(canvas, font=('Comic Sans MS', 15), width=3, validate='key',
                           validatecommand=(registered_validation_len_password, '%P'))
len_password_entry.place(x=180, y=220)
# create tick number
canvas.create_text(10, 255, text='numbers', font=('Comic Sans MS', 16), fill='#75c6ba', anchor=NW)
canvas_numbers = Canvas(canvas, bg='#fff', width=35, height=27)
canvas_numbers.place(x=181, y=255)
tick_white = PhotoImage(file='white.png')
tick_green = PhotoImage(file='green.png')
tick_number = canvas_numbers.create_image(2, 2, image=tick_green, anchor=NW)
# create tick letter
canvas.create_text(10, 290, text='letters', font=('Comic Sans MS', 16), fill='#75c6ba', anchor=NW)
canvas_letters = Canvas(canvas, bg='#fff', width=35, height=27)
canvas_letters.place(x=181, y=290)
tick_letters = canvas_letters.create_image(2, 2, image=tick_green, anchor=NW)
# create tick LETTERS
canvas.create_text(10, 325, text='LETTERS', font=('Comic Sans MS', 16), fill='#75c6ba', anchor=NW)
canvas_LETTERS = Canvas(canvas, bg='#fff', width=35, height=27)
canvas_LETTERS.place(x=181, y=325)
tick_LETTERS = canvas_LETTERS.create_image(2, 2, image=tick_green, anchor=NW)
# create tick sympol
canvas.create_text(10, 360, text='sympols', font=('Comic Sans MS', 16), fill='#75c6ba', anchor=NW)
canvas_sympols = Canvas(canvas, bg='#fff', width=35, height=27)
canvas_sympols.place(x=181, y=360)
tick_sympols = canvas_sympols.create_image(2, 2, image=tick_green, anchor=NW)
# plus minus
plus_image = PhotoImage(file='plus.png')
minus_image = PhotoImage(file='minus.png')
options = canvas.create_image(450, 200, anchor=NW, image=plus_image)
is_options = False
canvas.tag_bind(options, '<Button-1>', click_options)

plus_number = None
plus_letters = None
plus_LETTERS = None
plus_sympols = None
canvas_numbers.tag_bind(tick_number, '<Button-1>', lambda event: click_tick(canvas_numbers, tick_number, 1))
canvas_letters.tag_bind(tick_letters, '<Button-1>', lambda event: click_tick(canvas_letters, tick_letters, 2))
canvas_LETTERS.tag_bind(tick_LETTERS, '<Button-1>', lambda event: click_tick(canvas_LETTERS, tick_LETTERS, 3))
canvas_sympols.tag_bind(tick_sympols, '<Button-1>', lambda event: click_tick(canvas_sympols, tick_sympols, 4))

window.mainloop()