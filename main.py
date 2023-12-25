from ftplib import FTP
from dotenv import load_dotenv
import os
import tkinter as tk

from lib.getRegionsFromCoordinates import getRegionsFromCoordinates

# env vars 
load_dotenv()
host = os.getenv("FTP_HOST")
login = os.getenv("FTP_LOGIN")
password = os.getenv("FTP_PASSWORD")

# ftp setup
ftp = FTP(host)  
ftp.login(login, password)                     
ftp.cwd('world/DIM100/region')               

def doBackup(cornerOneStr: str, cornerTwoStr: str):
  cornerOne = cornerOneStr.strip().split(',')
  cornerTwo = cornerTwoStr.strip().split(',')

  allRegions = getRegionsFromCoordinates([int(x) for x in cornerOne], [int(x) for x in cornerTwo])
  for region in allRegions:
    with open(region, 'wb') as fp:
      ftp.retrbinary(f"RETR {region}", fp.write)

# gui
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

button = tk.Button(text="Do backup", command=lambda: doBackup(entryBottomLeft.get(), entryTopRight.get()))
button.pack()
window.mainloop()

ftp.quit()
