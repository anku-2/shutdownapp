from tkinter import *
import os
def restart():
    os.system("shutDown /r /t 1")
def restart_time():
    os.system("shutDown /r /t 20")    
def logout():
    os.system("shutDown -1")
def shutDown():
    os.system("shutDown /s /t 1")

root=Tk()
root.title("shutDown App")
root.geometry("500x500")
root.config(bg="red")
r_button = Button(root,text="Restart",font=("Time New Roman",30,"bold"),
                  relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=40,width=200)
ra_button = Button(root,text="Restart Time",font=("Time New Roman",10,"bold"),
                   relief=RAISED,cursor="plus",command=restart_time)
ra_button.place(x=150,y=170,height=50,width=200)
lg_button = Button(root,text="Log-Out",font=("Time New Roman",10,"bold"),
                   relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=40,width=200)
st_button = Button(root,text="ShutDown",font=("Time New Roman",10,"bold"),
                   relief=RAISED,cursor="plus",command=shutDown)
st_button.place(x=150,y=370,height=40,width=200)


root.mainloop()