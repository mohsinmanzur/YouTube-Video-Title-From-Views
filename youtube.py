from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import os
import pickle
import logging

## Replacing the below values with your own

vid_id = '246Ud6pI-YU' ## Video must be on your own channel
client_secrets = 'E:\\Python\\YouTube\\client_secrets.json'
credentials_file = 'E:\\Python\\YouTube\\credentials.pkl'
logfile = 'E:\\Python\\YouTube\\Logs.log'

scopes= ['https://www.googleapis.com/auth/youtube.force-ssl']

logging.basicConfig(
    filename = logfile,
    filemode = 'w',
    level = logging.NOTSET,
    format = '%(asctime)s - %(name)s: %(message)s',
    datefmt = '%H:%M:%S %d/%m/%Y'
)

log = logging.getLogger('YouTube')

if os.path.exists(credentials_file):
    log.info('Loading credentials from file...')
    with open(credentials_file, 'rb') as creds:
        credentials = pickle.load(creds)
    
else:
    log.info('Getting login details from browser...')
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets, scopes)
    credentials = flow.run_local_server(port=0)
    
    log.info('Saving credentials to file...')
    with open(credentials_file, 'wb') as creds:
        pickle.dump(credentials, creds)

log.info('Building the YouTube API.')
youtube = build("youtube", "v3", credentials=credentials)

request = youtube.videos().list(
    part="statistics",
    id=vid_id
)

log.info('Executing videos.list() request...')
response = request.execute()
views = response['items'][0]['statistics']['viewCount']
newtitle = f'This video has {views} views.'

updatename = youtube.videos().update(part='snippet', body= {'id': vid_id, 'snippet': {'categoryId': '20', 'title': newtitle}})

log.info('Executing videos.update() request...')
response = updatename.execute()
print(f'New Title: {response['snippet']['title']}')

log.info(f'Successfully updated title to {newtitle}!')