from tkinter import *
import time
from tkinter import messagebox
from random import *
# Import string and random module
import string
import random

root = Tk()


e = Entry(root)
e.grid(row=0, column=0, columnspan=3)

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))



def start():
    global rondomm_char
    rondomm_char = random_char(10)

    global random_word
    word = 'random_word' in globals()
    if word == True:
        random_word.destroy()

    else:
        pass

    random_word = Label(root, text=rondomm_char)
    random_word.grid(row=1, column=0)


    global start_time
    time_take = "time_taken" in globals()

    if time_take == True:
        time_taken.destroy()
    start_time=time.time()
    

def stop():
    test = e.get()

    if test == rondomm_char:
        pass
    else:
        error = messagebox.askokcancel("Name Error ", "Please Enter The correct word")
    # time.sleep()

    if test == rondomm_char:
        global time_taken
        time_taken = Label(root, text=round(time.time()-start_time))
        time_taken.grid(row=1, column=1)
    else:
        pass


a = Button(root, text="New Word", command=start)
a.grid(row=2, column=0)
b = Button(root, text="Stop", command=stop)
b.grid(row=2, column=1)


root.mainloop()




# def which_button(button_press):
# 	print(button_press)


# b1 = Button(app, text="Apple",
# 			command=lambda m="It is an apple": which_button(m))

