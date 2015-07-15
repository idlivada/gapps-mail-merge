import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open('/home/pawan/google_auth.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

def get_client():
    return gspread.authorize(credentials)
