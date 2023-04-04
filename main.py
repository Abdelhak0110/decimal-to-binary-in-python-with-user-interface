import tkinter
from tkinter import (
  Label as label,
  Button as button,
  Entry as entry,
  messagebox as mb
  Tk as tk
)



main = tk()

main.geometry("300x250")

def convert():
  binary = bin(int(decimal.get()))[2:]
  label2.configure(text="the binary number is: " + int(binary))
 
def clear():
  label2.configure(text="")
  mb.showinfo("clear", "the binary number is cleared successfully")

def isTrue():
  check = mb.askyesno("are you sure?", "do you want to exit?")
  if check == True:
    exit()
  else:
    pass

label1 = label(text="welcome to decimal to binary convertor, this script will convert any number that you put in the entry into binary")
label1.pack()

label2 = label(text="")
label2.pack()

decimal = entry(main)
decimal.insert(0, "13")
decimal.pack()

evaluate_button = button(text="convert", command=convert)
evaluate_button.pack()

clear_button = button(text="clear", command=clear)
clear_button.pack()

exit_button = button(text="exit", command=isTrue)
exit_button.pack()
