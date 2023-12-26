from ftplib import FTP
from dotenv import load_dotenv
import os
import zipfile
from datetime import datetime

from lib.getRegionFilesFromCoordinates import getRegionFilesFromCoordinates
from lib.getRegionsFromYaml import getRegionsFromYaml

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
ftp.cwd('world/DIM100/region')        

# date
currentDate = datetime.now()
currentDateStr = currentDate.strftime("%d-%m-%y")

def doBackup(regionName: str, cornerOne: list[int], cornerTwo: list[int], zipFileName: str ):
  allRegionFiles = getRegionFilesFromCoordinates(cornerOne, cornerTwo)

  with zipfile.ZipFile(zipFileName, 'a') as zipFile:
    for regionFile in allRegionFiles:
      with open(regionFile, 'wb') as fp:
        ftp.retrbinary(f"RETR {regionFile}", fp.write)
        zipFile.write(regionFile, f"{regionName}/{regionFile}")
        fp.close()
        os.remove(regionFile)

with open ('regions.yml', 'wb') as localYamlFile:
  ftp.retrbinary("RETR /plugins/WorldGuard/worlds/DIM100/regions.yml", localYamlFile.write)
yamlFile = ftp.retrbinary("RETR plugins/WorldGuard/worlds/DIM100/regions.yml")
allRegions = getRegionsFromYaml('regions.yml')

os.chdir("backups")

zipFileName = f"{currentDateStr}.zip"
zipfile.ZipFile(zipFileName, 'w')

for region in allRegions:
  doBackup(region['name'], region['min'], region['max'], zipFileName)
ftp.quit()
