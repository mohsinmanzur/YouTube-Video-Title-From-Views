# YouTube-Video-Title-From-Views
This Python script uses the YouTube Data API v3 to update a video's title based on its current view count. It performs authentication using OAuth 2.0 and stores credentials for future use.

## Features
- Authenticates with YouTube API (using OAuth and stored credentials)
- Fetches video statistics (view count)
- Updates the video title dynamically
- Logs all actions for debugging and tracking

## Requirements
- Python 3
- google-auth-oauthlib
- googleapiclient

## Setup
1. Enable the YouTube Data API v3 in the Google Cloud Console.
2. Download client_secrets.json from your Google Developer account.
3. Install dependencies using: ```pip install google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient```
4. Run the script: ```python script.py```

## How It Works
1. Loads credentials from a stored file (credentials.pkl) or authenticates via browser.
2. Fetches the current view count of a specific YouTube video.
3. Updates the video title to include the latest view count.
4. Logs each step for debugging.
