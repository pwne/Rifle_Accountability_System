"""
Copyright 2020 Francisco Adrian Rodriguez Vara

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
--------------------------------------------------------------------------------

rifle_accountability_system.py v0.1.5
    + replaced 'warning' icon with 'error' icon

"""

### NATIVE MODULES ###
import os, time, logging
from datetime import datetime

### 3RD PARTY MODULES ###
from tkinter import *
from tkinter import messagebox

### PROGRAM VARIABLES ###
## PROGRAM VERSION ##
version = "v0.1.5"

## TIME OBJECT ##
date=datetime.today()

## PATH VARIABLES ##
projectPath = os.getcwd()
logPath = f"{projectPath}\\logs"

## FILEPATH VARIABLES ##
logFilename = f"RAS_LOG_{date.month}_{date.day}_{date.year}.txt"
logFilepath = f"{logPath}\\{logFilename}"

### PROGRAM FUNCTIONS ###
def clockOut():
    """ Logs the name of the cadet and the rifle serial NO. he/she drew """
    pass

def clockIn():
    """ Logs the name of the cadet and the rifle serial NO. he/she returned """
    pass

def on_closing(loggerState):
    """ Program exit handler """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        logger.info(f"EXITING RAS{version}") if loggerState else sys.exit(f"EXITING RAS{version}")
        master.destroy()

def tick(curtime=''):
    """ Acts as a clock, changing the label as time goes up """
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clockLabel.config(text=curtime)
    clockLabel.after(200, tick, curtime)

def input_number(number):
    """ Access the global expression variables """
    global text
    text += str(number)
    serialNOIn.set(text)

def delete_previous_number():
    """ Delete the last enterd number """
    global text
    text = text[:-1]
    serialNOIn.set(text)

def clear_input_field():
    """ Clear the input field """
    global text
    text = ""
    serialNOIn.set("")

### MAIN RUNNER ###
if __name__ == "__main__":
    ### TKINTER WINDOW SETUP
    master = Tk()
    master.state("zoomed")                      # Use for development ONLY
    #master.attributes("-fullscreen", True)     # Uncomment for production
    master.title(f"RAS{version}")
    master.configure(bg="grey80")

    ## VARIABLE CLASS INSTANTIATION ##
    serialNOIn = StringVar()
    text = ""

    ### LOGGING CONFIGURATIONS ###
    try:
        # FILE SEARCH
        if logFilename in os.listdir(logPath):
            # CONFIGURE LOGGER (append to file if file is found)
            logging.basicConfig(filename=logFilepath,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='a',
                            level=logging.DEBUG)
        else:
            # CONFIGURE LOGGER (create new file if file not found)
            logging.basicConfig(filename=logFilepath,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='w',
                            level=logging.DEBUG)
        logger = logging.getLogger()    # Create a logger object
        logger.info(f"STARTING RAS{version}")
        logger.info("LOGGER CONFIGURATION SUCCESSFULL")
        loggerState = True

    # HANDLE ANY ERRORS ABOUT THE LOGGER CONFIGURATION PROCESS
    except Exception as err:
        print(f"STARTING RAS{version}")
        print("LOGGER CONFIGURATION FAILED")
        # CONTINUE PROGRAM FOLLOWING LOGGER CONFIGURATION FALIUE
        msgBox = messagebox.askquestion("LOGGER FAILED", f"The logging system was unable to start due to the following reason(s): \n\n{err}\n\nAny events will not be logged.\n\nWould you like to continue?", icon="error")
        if msgBox == 'yes':
            loggerState = False
        else:
            sys.exit(f"EXITING RAS{version}")

    try:
        ### TKINTER PROTOCOL SETTINGS ###
        master.protocol("WM_DELETE_WINDOW", lambda: on_closing(loggerState))

        ### IMAGE SETTINGS ###
        pixelVirtual = PhotoImage(width=1, height=1)

        ### MENU SECTION ###
        mainMenu = Menu(master)

        fileMenu = Menu(mainMenu,tearoff=0)
        fileMenu.add_command(label="Exit", command=lambda: on_closing(loggerState))
        mainMenu.add_cascade(label="File", menu=fileMenu)


        ### TOP FRAME ###
        topFrame = Frame(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight()/10)
        topFrame.pack(side=TOP, fill=X, expand=1, anchor=N)
        titleLabel = Label(topFrame, font=('arial', 12, 'bold'), bd=5, anchor=W,
                            text=f"Rifle Accountability System {version}")
        titleLabel.pack(side=LEFT)

        ### CLOCK FRAME (WITHIN "TOP FRAME") ###
        clockFrame = Frame(topFrame, width=master.winfo_screenwidth()/10, height=master.winfo_screenheight()/10, bd=4, relief="ridge")
        clockFrame.pack(side=RIGHT)
        clockLabel = Label(clockFrame, font=('arial', 12, 'bold'), bd=5, anchor=E)
        clockLabel.pack()

        ### LEFT FRAME ###
        leftFrame = Frame(master, width=master.winfo_screenwidth()/2, height=master.winfo_screenheight(), bg="grey80")
        leftFrame.pack(side=LEFT, fill=X, expand=1, anchor=W)

        ## LABELS ##
        nameLabel = Label(leftFrame, text="Name:", font=('arial', 25, 'bold'), bg="grey80").grid(sticky=W)
        serialNOLabel = Label(leftFrame, text="Serial NO:", font=('arial', 25, 'bold'), bg="grey80").grid(sticky=W)

        ## ENTRIES ##
        nameEntry = Entry(leftFrame)
        nameEntry.grid(row=0, column=1)
        serialNOEntry = Entry(leftFrame, textvar=serialNOIn)
        serialNOEntry.grid(row=1, column=1)

        ### RIGHT FRAME ###
        rightFrame = Frame(master, width=master.winfo_screenwidth()/2, height=master.winfo_screenheight(), bg="grey80")
        rightFrame.pack(side=LEFT, fill=X, expand=1, anchor=E)

        buttonWidth = master.winfo_screenwidth()/6
        buttonHeight = (master.winfo_screenwidth()-master.winfo_screenwidth()/10)/8
        font1 = ('arial', 50, 'bold')
        font2 = ('arial', 25, 'bold')
        _1 = Button(rightFrame, text="1", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(1)).grid(column=0,row=1)
        _2 = Button(rightFrame, text="2", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(2)).grid(column=1,row=1)
        _3 = Button(rightFrame, text="3", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(3)).grid(column=2,row=1)
        _4 = Button(rightFrame, text="4", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(4)).grid(column=0,row=2)
        _5 = Button(rightFrame, text="5", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(5)).grid(column=1,row=2)
        _6 = Button(rightFrame, text="6", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(6)).grid(column=2,row=2)
        _7 = Button(rightFrame, text="7", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(7)).grid(column=0,row=3)
        _8 = Button(rightFrame, text="8", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(8)).grid(column=1,row=3)
        _9 = Button(rightFrame, text="9", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(9)).grid(column=2,row=3)
        _0 = Button(rightFrame, text="0", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font1, command=lambda: input_number(0)).grid(column=1,row=4)
        _clear = Button(rightFrame, text="CLEAR", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font2, command=lambda: clear_input_field()).grid(column=0,row=4)
        _backspace = Button(rightFrame, text="BACKSPACE", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font2, command=lambda: delete_previous_number()).grid(column=2,row=4)

        tick()
        master.configure(menu=mainMenu)
        master.mainloop()

    except Exception as err:
        logger.critical(err)
        sys.exit(f"CRITICAL ERROR ENCOUNTERED:\n\n{err}\n\nEXITING RAS{version}")
