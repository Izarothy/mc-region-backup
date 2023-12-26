from ftplib import FTP
from dotenv import load_dotenv
import os
import zipfile
from lib.getRegionsFromCoordinates import getRegionsFromCoordinates

# backup folder
if (not os.path.isdir('backups')):
  os.mkdir('backups')

# env vars 
load_dotenv()
host = os.getenv("FTP_HOST")
login = os.getenv("FTP_LOGIN")
password = os.getenv("FTP_PASSWORD")

# ftp setup
ftp = FTP(host)  
ftp.login(login, password)                     

def doBackup(cornerOne: list[int], cornerTwo: list[int], zipFileName: str, ):
  ftp.cwd('world/DIM100/region')        
  allRegions = getRegionsFromCoordinates(cornerOne, cornerTwo)

  if (os.getcwd().find('backups') == -1):
    os.chdir('backups')

  with zipfile.ZipFile(f"{zipFileName.get()}.zip", 'w') as zipFile:
    for region in allRegions:
      with open(region, 'wb') as fp:
        ftp.retrbinary(f"RETR {region}", fp.write)
        fp.close()
        zipFile.write(region)
        os.remove(region)
  
ftp.quit()
