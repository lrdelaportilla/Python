from tkinter import *
#I want orange juice
#you have to work..... turd

import webbrowser


root = Tk()
root.title("Liam's First Software")
root.geometry("640x480+100+100")

url = "https://scratch.mit.edu/"


url2 = "https://www.facebook.com/"

frame = Frame(root)
frame.grid()

label = Label(frame, text = "This is Liam's First Software")
label.grid()

def OpenUrl():
        webbrowser.open_new(url)

def user_input():
        userinput_get = userinput.get()
        command = Label(text="Hello " + userinput_get).grid()

def endprogram(root):
        root.destory()

button = Button(text='Run', command = user_input, bg='green').grid()
button = Button(root,text='https://scratch.mit.edu/', command = OpenUrl, bg='pink').grid()


button = Button(text='Exit', command = endprogram ,bg='red').grid()


button = Button(root,text='https://www.facebook.com/', command = OpenUrl2, bg='blue').grid()
 

button = Button(text='1', bg='white').grid()

button = Button(text='2', bg='white').grid()

button = Button(text='3', bg='white').grid()

button = Button(text='4', bg='white').grid()

userinput = StringVar()
userdata = Entry(frame, textvariable=userinput, width=50).grid()



root.mainloop()



