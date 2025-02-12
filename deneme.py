from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Yetkilendirme
SCOPES = ['https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
service = build('drive', 'v3', credentials=creds)

# Google Drive'daki tüm dosyaları listele
results = service.files().list(pageSize=10, fields="files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('Hiçbir dosya bulunamadı.')
else:
    print('Google Drive dosyaları:')
    for item in items:
        print(f"Ad: {item['name']}, ID: {item['id']}")
