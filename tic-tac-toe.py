from tkinter import *
import tkinter.messagebox


def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      
      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
           
      else :
            player = "X"
            button["bg"] = "lightgreen"
      check()
      
      
window = Tk()
player = "X"
list = []
wincase = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 3, 6, 1, 4, 7, 2, 5, 8, 0, 4, 8, 2, 4, 6]  

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)
      


def check() :
      j=0
      while j < 22 :
            if list[wincase[j]]["text"] == list[wincase[j+1]]["text"] == list[wincase[j+2]]["text"] == "X" :
                  tkinter.messagebox.showinfo("60132301이석준", "X is winner")
                  quit()
            elif list[wincase[j]]["text"] == list[wincase[j+1]]["text"] == list[wincase[j+2]]["text"] == "O":
                  tkinter.messagebox.showinfo("60132301이석준", "O is winner")
                  quit()
            j = j+3;
            
                  
window.mainloop()


