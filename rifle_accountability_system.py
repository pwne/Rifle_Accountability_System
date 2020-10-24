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

rifle_accountability_system.py v0.1.0

"""

### NATIVE MODULES ###
import os, time, logging
from datetime import datetime

### 3RD PARTY MODULES ###
from tkinter import *
from tkinter import messagebox

### PROGRAM VARIABLES ###
## TIME OBJECT ##
date=datetime.today()

## PATH VARIABLES ##
projectPath = os.getcwd()
logPath = f"{projectPath}\\logs"

## FILEPATH VARIABLES ##
logFilename = f"RAS_LOG_{date.month}_{date.day}_{date.year}.txt"
logFilepath = f"{logPath}\\{logFilename}"

### HELPER FUNCTIONS ###
def clockOut():
    """ Logs the name of the cadet and the rifle serial NO. he/she drew """
    pass

def clockIn():
    """ Logs the name of the cadet and the rifle serial NO. he/she returned """
    pass

def on_closing(logger, loggerState):
    """ Program exit handler """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        logger.info("EXITING RASv0.9") if loggerState else print("EXITING RASv0.9")
        master.destroy()

def tick(curtime=''):
    """ Acts as a clock, changing the label as time goes up """
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clockLabel.config(text=curtime)
    clockLabel.after(200, tick, curtime)

### MAIN RUNNER ###
if __name__ == "__main__":
    ### TKINTER WINDOW SETUP
    master = Tk()
    #master.state("zoomed")
    master.attributes("-fullscreen", True)
    master.title("RASv0.9")

    ### LOGGING CONFIGURATIONS ###
    try:
        if logFilepath in os.listdir(logPath):
            logging.basicConfig(filename=logFilepath,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='a',
                            level=logging.DEBUG)
        else:
            logging.basicConfig(filename=logFilepath,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='w',
                            level=logging.DEBUG)
        logger = logging.getLogger()
        logger.info("STARTING RASv0.9")
        logger.info("LOGGER CONFIGURATION SUCCESSFULL")
        loggerState = True
    except Exception as err:
        print("STARTING RASv0.9")
        print("LOGGER CONFIGURATION FAILED")
        messagebox.showwarning("LOGGER FAILED", f"The logging system was unable to start due to the following reason(s): \n\n{err}\n\nAny events will not be logged.")
        loggerState = False

        #sys.exit()

    ### GENERAL TKINTER SETTINGS ###
    master.protocol("WM_DELETE_WINDOW", lambda: on_closing(logger, loggerState))
    master.configure(bg="grey80")

    ### IMAGE SETTINGS ###
    pixelVirtual = PhotoImage(width=1, height=1)

    ### MENU SECTION ###
    mainMenu = Menu(master)

    fileMenu = Menu(mainMenu,tearoff=0)
    fileMenu.add_command(label="Exit", command=lambda: on_closing(logger, loggerState))
    mainMenu.add_cascade(label="File", menu=fileMenu)


    ### TOP FRAME ###
    topFrame = Frame(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight()/10)
    topFrame.pack(side=TOP, fill=X, expand=1, anchor=N)
    titleLabel = Label(topFrame, font=('arial', 12, 'bold'), bd=5, anchor=W,
                        text="Rifle Accountability System v0.9")
    titleLabel.pack(side=LEFT)

    ### CLOCK FRAME (WITHIN "TOP FRAME") ###
    clockFrame = Frame(topFrame, width=master.winfo_screenwidth()/10, height=master.winfo_screenheight()/10, bd=4, relief="ridge")
    clockFrame.pack(side=RIGHT)
    clockLabel = Label(clockFrame, font=('arial', 12, 'bold'), bd=5, anchor=E)
    clockLabel.pack()

    ### LEFT FRAME ###
    leftFrame = Frame(master, width=master.winfo_screenwidth()/2, height=master.winfo_screenheight(), bg="grey80")
    leftFrame.pack(side=LEFT, fill=X, expand=1, anchor=W)

    ### RIGHT FRAME ###
    rightFrame = Frame(master, width=master.winfo_screenwidth()/2, height=master.winfo_screenheight(), bg="grey80")
    rightFrame.pack(side=LEFT, fill=X, expand=1, anchor=E)

    buttonWidth = master.winfo_screenwidth()/6
    buttonHeight = (master.winfo_screenwidth()-master.winfo_screenwidth()/10)/8
    font = ('arial', 50, 'bold')
    _1 = Button(rightFrame, text="1", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=0,row=1)
    _2 = Button(rightFrame, text="2", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=1,row=1)
    _3 = Button(rightFrame, text="3", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=2,row=1)
    _4 = Button(rightFrame, text="4", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=0,row=2)
    _5 = Button(rightFrame, text="5", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=1,row=2)
    _6 = Button(rightFrame, text="6", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=2,row=2)
    _7 = Button(rightFrame, text="7", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=0,row=3)
    _8 = Button(rightFrame, text="8", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=1,row=3)
    _9 = Button(rightFrame, text="9", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=2,row=3)
    _0 = Button(rightFrame, text="0", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=font).grid(column=1,row=4)
    _clear = Button(rightFrame, text="CLEAR", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=('arial', 25, 'bold')).grid(column=0,row=4)
    _backspace = Button(rightFrame, text="BACKSPACE", image=pixelVirtual, width=buttonWidth, height=buttonHeight, compound="c", font=('arial', 25, 'bold')).grid(column=2,row=4)

    tick()
    master.configure(menu=mainMenu)
    master.mainloop()
