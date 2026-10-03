from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os
import sys

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Check if client_secret.json exists
if not os.path.exists("client_secret.json"):
    print("Error: client_secret.json file not found!")
    print("\nTo fix this, you need to:")
    print("1. Go to the Google Cloud Console (https://console.cloud.google.com/)")
    print("2. Create a new project or select an existing one")
    print("3. Enable the YouTube Data API v3")
    print("4. Go to 'Credentials' in the left sidebar")
    print("5. Click 'Create Credentials' > 'OAuth client ID'")
    print("6. Choose 'Desktop application' as the application type")
    print("7. Download the JSON file and rename it to 'client_secret.json'")
    print("8. Place the file in the same directory as this script")
    print(f"\nCurrent directory: {os.getcwd()}")
    sys.exit(1)

try:
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=8080)
    
    with open("youtube_token.pkl", "wb") as token:
        pickle.dump(creds, token)
    
    print("Authentication successful! Token saved to youtube_token.pkl")
    
except Exception as e:
    print(f"An error occurred during authentication: {e}")
    sys.exit(1)
