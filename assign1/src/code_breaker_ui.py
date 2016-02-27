from tkinter import *
from code_breaker import CodeBreaker, Color, Response
from functools import partial


class CodeBreakerApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, width=1100, height=625)
        self.base = CodeBreaker()
        self.base.random_colors_selection()
        self.selected_colors = [None]*5
        variable = StringVar()
        self.evaluate_button = Button(self, bg='grey', text="Evaluate Selected Colors", 
            command=self.OnEvaluationButtonClick, padx=50, pady=50, state = DISABLED)
        self.evaluate_button.place(x=482, y=247)        
        self.grid()
        self.create_color_pool_frame()
        self.create_response_frame()
        self.create_user_input_buttons()

    def create_color_pool_frame(self):
        self.color_buttons = [[None]*2 for _ in range(5)]
        for i in range(5):
            for j in range(2):
                self.color_buttons[i][j] = self.base.color_pool[i + j*5]
                self.color_buttons[i][j] = Button(self, bg=self.base.color_pool[i +j*5].value, 
                    state=DISABLED, padx=50, pady=50, 
                    command = partial(self.OnColorPoolButtonClick, color = self.base.color_pool[i +j*5]),
                    highlightthickness = 2)
                self.color_buttons[i][j].place(x=j*110, y=125*i)
                self.color_buttons[i][j].bind("<Enter>", self.mouse_enter)
                self.color_buttons[i][j].bind("<Leave>", self.mouse_leave)

    def create_response_frame(self):
        self.response_frame = [None]*5
        for i in range(5):
            self.response_frame[i] = Label(self, bg="red", padx=50, pady=50)
            self.response_frame[i].place(x=330 + i*120, y=125)

    def create_user_input_buttons(self):
        self.input_buttons = [None]*5
        for i in range(5):
            self.input_buttons[i] = Button(self, bg="black", padx=50, pady=50,
                command = partial(self.OnInputButtonClick, index = i), highlightthickness = 5)
            self.input_buttons[i].place(x= 330 + 120*i, y=375)

    def OnInputButtonClick(self, index = None):
        for i in range(5):
            for j in range(2):
                self.color_buttons[i][j].config(state = 'normal',
                    highlightbackground = "black")
        for button in self.input_buttons:
            button.config(highlightbackground = self["bg"])
        self.input_buttons[index].config(highlightbackground = "yellow")
        self.chosen_input_button_index = index

    def OnColorPoolButtonClick(self, color = None):
        self.input_buttons[self.chosen_input_button_index].config(bg = color.value,
            highlightbackground = self.cget("bg"))
        self.selected_colors[self.chosen_input_button_index] = color
        if None not in self.selected_colors:
            self.evaluate_button.config(state = 'normal', text = "Evaluate Selected Colors")
        for i in range(5):
            for j in range(2):
                self.color_buttons[i][j].config(state = 'disabled', 
                    highlightbackground = self.cget("bg"))

    def OnEvaluationButtonClick(self):
        responses = []
        responses = self.base.guess_colors(self.selected_colors)
        for i in range(5):
            if responses[i] == Response.MATCH_POSITION:
                color = Color.black
            elif responses[i] == Response.MATCH:
                color = Color.silver
            else:
                color = Color.white
            self.response_frame[i].config(bg = color.value)
        if self.base.game_won:
            self.evaluate_button.config(text = 'You Won')
            self.evaluate_button.config(command = self.quit)
        else:
            self.evaluate_button["text"] = "Chances left: {}".format(20 - self.base.number_of_guess_made)
        if self.base.number_of_guess_made >= 20:
            self.evaluate_button.config(command = self.quit)

    def mouse_enter(self, event):
        if event.widget['state'] != 'disabled':
            event.widget.config(highlightbackground = "blue")

    def mouse_leave(self, event):
        if event.widget['state'] != 'disabled':
            event.widget.config(highlightbackground = "black")

if __name__ == '__main__':
    top = Tk()
    top.resizable(width=FALSE, height=FALSE)
    app = CodeBreakerApplication(top)
    app.master.title("Color Game")
    top.mainloop()
