#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    blogs = service.blogs()

    # Retrieve the list of Blogs this user has write privileges on
    bloglist = blogs.listByUser(userId='self').execute()

    blog = bloglist['items'][0]

    posts = service.posts()

    r = posts.list(blogId=blog['id'], status='DRAFT').execute()

    body = r['items'][0]

    blogId = body['blog']['id']
    postId = body['id']

    print(blogId,postId)

    # Updated Data
    body['title'] = 'Hello Update'
    body['content'] =  '<h1>Hello Updated World !!</h1>'

    # Update the post for a blog
    r = posts.update(blogId=blogId, postId=postId, body=body)
    r.execute()

    r.close()

if __name__ == '__main__':
    main()
