# Binet's Calculator

from tkinter import *
import math

def click():
    error = "PLEASE ENTER AN INTEGER"
    fib = fib_input.get()
    fib_result.delete(0.0, END)
    if (fib.isnumeric() == False):
        fib_result.insert(1.0, error, "center")
        return
    else:
        fib = int(fib, base=10)
        fib_answer = math.floor((1/(5 **(1/2))*(((1+(5**(1/2)))/2)**fib-((1-(5**(1/2)))/2)**fib)))
        fib_result.insert(1.0, fib_answer, "center")

### MAIN ###
window = Tk()
window.title("Bidet's Calculator")
window.configure(background="pink")
window.resizable(width=False, height=False)


### DECLARATIONS ###
fib_label1 = Label(window, text="The ", bg="pink", fg="blue", font="none 12 bold")
fib_label2 = Label(window, text=" (st/nd/rd/th) number ", bg="pink", fg="blue", font="none 12 bold")
fib_label3 = Label(window, text="  in the fibonacci sequence is: ", bg="pink", fg="blue", font="none 12 bold")
fib_input = Entry(window, width=5, bg="white", fg="blue", font="none 12 bold", justify="center")
fib_result = Text(window, width=40, height=5, wrap=WORD, background="white", fg="blue", font="none 12 bold")
submit_button = Button(window, text="SUBMIT", width=6, command=click)


### APPLICATION TO GRID
fib_label1.grid(row=0, column=0)
fib_input.grid(row=1, column=0)
fib_label2.grid(row=2, column=0)
fib_label3.grid(row=3, column=0)
fib_result.grid(row=4, column=0)
submit_button.grid(row=5, column=0)


window.mainloop()


