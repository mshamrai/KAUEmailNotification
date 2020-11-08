import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from reportInfo import *


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def get_emails():
    SAMPLE_SPREADSHEET_ID = '13vwyvMRlv-hf-glUsIDn2AYGqnWjL2eOwzlxB7rhwvI'
    SAMPLE_RANGE_NAME = 'B2:B'
    service = build('sheets', 'v4', credentials=get_creds())
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    emails = result.get('values', [])
    emails = [e[0] for e in emails]
    return list(dict.fromkeys(emails))

def get_report_info():
    SAMPLE_SPREADSHEET_ID = '1FPnNPFGcli5gaeoMPpGXk4TZJwQCeT42CrinSXsn9YU'
    SAMPLE_RANGE_NAME = 'A11:I11'
    service = build('sheets', 'v4', credentials=get_creds())
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    info = result.get('values', [])
    return [ReportInfo(i) for i in info]

def main():
    info = get_report_info()

    if not info:
        print('No data found.')
    else:
        for row in info:
            print(row)

        print(len(info))

if __name__ == '__main__':
    main()