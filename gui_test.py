import os, logging, datetime
from tkinter import *

### LOGGING CONFIGURATIONS ###
date=datetime.datetime.today()
filename=f"{date.month}_{date.today().day}_{date.year}.txt"
if filename in os.listdir():
    logging.basicConfig(filename=filename,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a',
                    level=logging.DEBUG)
else:
    logging.basicConfig(filename=filename,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w',
                    level=logging.DEBUG)
logger = logging.getLogger()
logger.info("STARTING RASv0.9")

### Tkinter CONFIGURATIONS ###
root = Tk()
#root.attributes("-fullscreen", True)   ### UNCOMMENT FOR PRODUCTION

# BUTTON FUNCTIONS #
def clockOut():
    """ Logs the name of the cadet and the rifle serial NO. he/she drew """
    logger.info(f"{nameEntry.get()} clocked out rifle: {serialNOEntry.get()}")

def clockIn():
    """ Logs the name of the cadet and the rifle serial NO. he/she returned """
    logger.info(f"{nameEntry.get()} clocked in rifle: {serialNOEntry.get()}")

## START GENERAL CONFIGS ###
try:
    # TITTLE LABEL #
    """
    title = Label(root, text="RIFLE ACCOUNTABILIITY SYSTEM v0.9", font=("Helvetica", 30))
    title.pack(side=TOP)
    """

    # LABELS #
    nameLabel = Label(root, text="Name:").grid(sticky=E)
    serialNOLabel = Label(root, text="Serial NO:").grid(sticky=E)

    # ENTRIES #
    nameEntry = Entry(root)
    nameEntry.grid(row=0, column=1)
    serialNOEntry = Entry(root)
    serialNOEntry.grid(row=1, column=1)

    # BUTTONS #
    exitButton = Button(root, text="EXIT", command=lambda:[logger.info("EXITING"), root.destroy()]).grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
    clockOutButton = Button(root, text="Clock Out", command=clockOut).grid(row=2,column=3)
    clockInButton = Button(root, text="Clock In", command=clockIn).grid(row=2,column=4)

    # NUMBERPAD #
    """
    _1 = Button(root, text="1").grid(column=0,row=1)
    _2 = Button(root, text="2").grid(column=1,row=1)
    _3 = Button(root, text="3").grid(column=2,row=1)
    _4 = Button(root, text="4").grid(column=0,row=2)
    _5 = Button(root, text="5").grid(column=1,row=2)
    _6 = Button(root, text="6").grid(column=2,row=2)
    _7 = Button(root, text="7").grid(column=0,row=3)
    _8 = Button(root, text="8").grid(column=1,row=3)
    _9 = Button(root, text="9").grid(column=2,row=3)
    _0 = Button(root, text="0").grid(column=1,row=4)
    """
    root.mainloop()

except TclError as err:
    logger.critical(err)
