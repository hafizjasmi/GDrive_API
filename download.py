import io
import pickle
import os.path
import datetime as dt
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

'''Configuration'''
# ID of the folder to be downloaded.
# ID can be obtained from the URL of the folder
FOLDER_ID = input('Please Insert Folder ID here : ')


# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
start_time = dt.datetime.now()
proper_start_time = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

DOWNLOAD_FOLDER = input("Please insert your path : ")

def main():
    """Download all files in the specified folder in Google Drive."""
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    

    page_token = None
    while True:
        # Call the Drive v3 API
        results = service.files().list(
                q=f"'{FOLDER_ID}' in parents",
                pageSize=1000, includeItemsFromAllDrives=True, supportsAllDrives=True, fields="files(id, name, size)",
                pageToken=page_token).execute()
        items = results.get('files', [])
        

        if not items:
            print('No files found/No folders found')
        else:
            for item in items:
                start_time1 = dt.datetime.now()
                proper_start_time1 = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                MB_size = format((int(item['size'])/int(1024)/int(1024)), '.2f')
                name = format(item['name'])
                id = format(item['id'])
                print('Timestamp : ' + str(proper_start_time1) + ' | Filename : ' + str(name) + ' | Size : ' + str(MB_size) + ' MB | ID : ' + str(id) + '  ')
                

                file_id = item['id']
                request = service.files().get_media(fileId=file_id)

                folder_path = DOWNLOAD_FOLDER
                with open(folder_path + item['name'], 'wb') as fh:
                
                
                    downloader = MediaIoBaseDownload(fh, request)
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()
                        print("Downloading %d%% " % int(status.progress() * 100))
                    fh.seek(0)
                    end_time1 = dt.datetime.now()
                    finish_time1 = end_time1 - start_time1
                    
                    print("Time taken to finish downloading this files : {} \n\n".format(finish_time1))       
        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break
    end_time = dt.datetime.now()
    proper_end_time = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    finish_time = end_time - start_time
    print("Time Started : " + proper_start_time + "\nTime Finished : " + proper_end_time + "\nTime Taken : " + str(finish_time))    
if __name__ == '__main__':
    main()
