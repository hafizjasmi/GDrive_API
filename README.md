# GDrive_API
This is for Google Drive related API which is downloading folder and it's content recursively and also uploading. Basically all interact with the GDrive API


## README
A Python script for downloading all files under a folder in Google Drive.
Downloaded files will be saved at the current working directory.
This script uses the official Google Drive API (https://developers.google.com/drive).
To use this script, you should first follow the instruction 
in Quickstart section in the official doc (https://developers.google.com/drive/api/v3/quickstart/python):
- Enable Google Drive API 
- Download `credential.json` through OAuth 2.0
- Install dependencies (python -m pip install -r requirements.txt --upgrade)
Notes:
- This script will only work on a local environment, 
  i.e. you can't run this on a remote machine
  because of the authentication process of Google.
- This script only downloads binary files, meaning picture, videos, etc etc but not google docs or spreadsheets.



## Notes
Put the credentials.json into the same folder as the script. Then you will need to whitelist port 8080 and hostname is localhost.
run the script by using python command invoke, then it will run and insert the folder id.
