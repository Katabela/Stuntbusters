from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Define the Gmail scope (full access to send/read emails)
SCOPES = ['https://mail.google.com/']

# Start the OAuth flow
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES
)
creds = flow.run_local_server(port=0)

# Print your tokens
print("\n✅ ACCESS TOKEN:")
print(creds.token)
print("\n🔁 REFRESH TOKEN:")
print(creds.refresh_token)

