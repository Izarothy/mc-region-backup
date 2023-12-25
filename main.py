from ftplib import FTP
from dotenv import load_dotenv
import os
load_dotenv()

# env vars 
host = os.getenv("FTP_HOST")
login = os.getenv("FTP_LOGIN")
password = os.getenv("FTP_PASSWORD")

ftp = FTP(host)  
ftp.login(login, password)                     
ftp.cwd('world')               
ftp.retrlines('LIST')           

ftp.quit()
