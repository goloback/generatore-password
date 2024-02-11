class Date_information():
    def __init__(self, error_message):
        self.amount_numbers = 0
        self.amount_letters = 0
        self.amount_LETTERS = 0
        self.amount_sympols = 0
        #self.error_message = error_message
    def print_information(self):
        print(self.amount_numbers, self.amount_letters, self.amount_LETTERS, self.amount_sympols)
    def get_sum(self):
        return self.amount_numbers + self.amount_letters + self.amount_LETTERS + self.amount_sympols

   # def delete_error(self):
       # if self.error_message is not None:
           # self.error_message.destroy()
          #  self.error_message = None
