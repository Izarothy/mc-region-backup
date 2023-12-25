from ftplib import FTP
from dotenv import load_dotenv
import os

import tkinter as tk

# env vars 
load_dotenv()
host = os.getenv("FTP_HOST")
login = os.getenv("FTP_LOGIN")
password = os.getenv("FTP_PASSWORD")

# ftp setup
ftp = FTP(host)  
ftp.login(login, password)                     
ftp.cwd('world')               
ftp.retrlines('LIST')           

window = tk.Tk()
window.geometry('500x300')

labelBottomLeft = tk.Label(text="Bottom left corner")
entryBottomLeft = tk.Entry()
labelBottomLeft.pack()
entryBottomLeft.pack()

labelTopRight = tk.Label(text="Top right corner")
entryTopRight = tk.Entry()
labelTopRight.pack()
entryTopRight.pack()


button = tk.Button(text="Do backup", command=doBackup)
button.pack()
window.mainloop()

ftp.quit()
