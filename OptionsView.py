from tkinter import *
class optionsView():

    def __init__(self, canvas, y, window, type_value, date_information):
        self.registered_validation_entry_amount = window.register(self.validation_entry_amount)
        self.entry = Entry(canvas, font=('Comic Sans MS', 15), width=3, validate='key',
                           validatecommand=(self.registered_validation_entry_amount, '%P'))
        self.entry.place(x=240, y=y)
        self.label = Label(canvas, font=('Comic Sans MS', 15), bg='#9f6fde', fg='#97c6c7', text='amount')
        self.label.place(x=290, y=y)
        self.type_value = type_value
        self.date_information = date_information



    def destroy(self):
        self.entry.destroy()
        self.label.destroy()

    def validation_entry_amount(self, try_number):
        if len(try_number) == 0:
            self.set_value(0)
            self.date_information.print_information()
            return True
        if try_number == '0':
            return False
        if len(try_number) > 2:
            return False
        if try_number.isdigit() == True:
            buf = -1
            if self.type_value == 'numbers':
                buf = self.date_information.amount_numbers
            elif self.type_value == 'letters':
                buf = self.date_information.amount_letters
            elif self.type_value == 'LETTERS':
                buf = self.date_information.amount_LETTERS
            elif self.type_value == 'sympols':
                buf = self.date_information.amount_sympols
            self.set_value(int(try_number))
            if self.date_information.get_sum()<100:
                self.date_information.print_information()
#                self.date_information.delete_error()
                return True
            else:
                if self.type_value == 'numbers':
                    self.date_information.amount_numbers = buf
                elif self.type_value == 'letters':
                    self.date_information.amount_letters = buf
                elif self.type_value == 'LETTERS':
                    self.date_information.amount_LETTERS = buf
                elif self.type_value == 'sympols':
                    self.date_information.amount_sympols = buf

        return False

    def set_value(self, value):
        if self.type_value == 'numbers':
            self.date_information.amount_numbers = value
        elif self.type_value == 'letters':
            self.date_information.amount_letters = value
        elif self.type_value == 'LETTERS':
            self.date_information.amount_LETTERS = value
        elif self.type_value == 'sympols':
            self.date_information.amount_sympols = value

