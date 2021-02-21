import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from reportInfo import *
from seminarDate import nextWednesday, str2Date


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
EMAILS_SPREADSHEET_ID = os.environ.get('EMAILS_SPREADSHEET_ID')
EMAILS_SPREADSHEET_RANGE = os.environ.get('EMAILS_SPREADSHEET_RANGE')
INFO_SPREADSHEET_ID = os.environ.get('INFO_SPREADSHEET_ID')
GOOGLE_CLIENT_SECRET_FILE = 'credentials.json'


def get_creds():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GOOGLE_CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def request(spreadsheetId, range):
    service = build('sheets', 'v4', credentials=get_creds())
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheetId,
                                range=range).execute()
    return result.get('values', [])

def get_emails():
    emails = request(EMAILS_SPREADSHEET_ID, EMAILS_SPREADSHEET_RANGE)
    emails = [e[0] for e in emails]
    return list(dict.fromkeys(emails))

def get_report_info():
    DATE_RANGE = 'B2:B'
    dates = request(INFO_SPREADSHEET_ID, DATE_RANGE)
    indices = [i for i, x in enumerate(dates) if str2Date(x[0]) == nextWednesday]
    RANGES = ['A' + str(i+2) + ':I' + str(i+2) for i in indices]
    info = [request(INFO_SPREADSHEET_ID, r) for r in RANGES]
    info = [i[0] for i in info]
    return [ReportInfo(i) for i in info]


if __name__ == '__main__':
    info = get_emails()

    if not info:
        print('No data found.')
    else:
        for row in info:
            print(row)

        print(len(info))
