from tkinter import *
import time
from tkinter import messagebox
from random import *
import string
import random


root = Tk()


e = Entry(root, width=50)
e.grid(row=0, column=0, columnspan=10)

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))


def start():
    global rondomm_char
    rondomm_char = random_char(10)

    global random_word
    word = 'random_word' in globals()
    if word == True:
        random_word.destroy()

    checkbutton = 'custom_stop' in globals()
    if checkbutton == True:
        custom_stop.destroy()

    else:
        pass

    random_word = Label(root, text=rondomm_char)
    random_word.grid(row=1, column=0)


    global start_time
    time_take = "time_taken" in globals()

    if time_take == True:
        time_taken.destroy()
    start_time=time.time()


def custom_start():
       global custom_stop
       custom_stop = Button(root, text="Stop Custom", command=finish_custom)
       custom_stop.grid(row=2, column=2)
       wordd = 'random_word' in globals()
       if wordd == True:
        random_word.destroy()

       else:
        pass

       user_word = Label(root, text=word)
       user_word.grid(row=1, column=0)


       global start_time
       time_take = "time_taken" in globals()

       if time_take == True:
        time_taken.destroy()
       start_time=time.time()


#############################################################################################

def custom():
       global e_custom
       custom_word = Toplevel()
       label_custom = Label(custom_word, text='Enter a word here :- ').grid(row=0, column=0)
       e_custom = Entry(custom_word)
       e_custom.grid(row=0, column=1)
       submit_custom = Button(custom_word, text='Submit', command=custom_word_add)
       submit_custom.grid(row=1, column=1)

def custom_word_add():
       global word
       word = e_custom.get()
       custom_word = Button(root, text=word, command=custom_start)
       custom_word.grid(row=4, column=1)

       
#############################################################################################

    

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

def finish_custom():
    custom_stop.destroy()
    test = e.get()

    if test == word:
        pass
    else:
        error = messagebox.askokcancel("Name Error ", "Please Enter The correct word")
    # time.sleep()

    if test == word:
        global time_taken
        time_taken = Label(root, text=round(time.time()-start_time))
        time_taken.grid(row=1, column=1)
    else:
        pass




a = Button(root, text="Random Word", command=start)
a.grid(row=2, column=0)
b = Button(root, text="Stop", command=stop)
b.grid(row=2, column=2)
c = Button(root, text="Custom Word", command=custom)
c.grid(row=2, column=1)

root.mainloop()
