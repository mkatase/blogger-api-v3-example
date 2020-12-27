#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/blogger']

def main():
    """Shows basic usage of the Google Blogger API.
    Prints the start and draft content on the user's blogger.
    """
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
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('blogger', 'v3', credentials=creds)

    # Call the Blogger API
    users = service.users()

    # Retrieve this user's profile infomation
    thisuser = users.get(userId='self').execute()
    print('This user\'s display name is: %s' % thisuser['displayName'])

    blogs = service.blogs()

    # Retrieve the list of Blogs this user has write privileges on
    bloglist = blogs.listByUser(userId='self').execute()

    blog = bloglist['items'][0]
    print(blog['id'])

    # Insert the post for a blog this user has
    posts = service.posts()

    # Set Data
    body = {
        'title'   : 'Hello Test',
        'content' : '<h1>Hello World !!</h1>',
        'labels'  : ['Test', 'Misc'],
    }

    r = posts.insert(blogId=blog['id'], body=body, isDraft=True)
    r.execute()

    r.close()

if __name__ == '__main__':
    main()
