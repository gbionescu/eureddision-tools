#!/usr/bin/env python3
import praw
import sys
import time
import argparse
import re
import csv
import json
from youtube_api import get_authenticated_service

youtube = get_authenticated_service()

parser = argparse.ArgumentParser()
USER_AGENT = "YouTube scraper by /u/programatorulupeste"

def get_yt_title(yt_id):
    if "watch?v=" in yt_id:
        yt_id = yt_id.split('=')[-1]

    if "youtu.be" in yt_id:
        yt_id = yt_id.split("/")[-1]

    if "?t=" in yt_id:
        yt_id = yt_id.split("?t=")[0]

    print("Looking up " + yt_id)
    results = youtube.videos().list(
        part='snippet',
        id=yt_id).execute()

    try:
        return results['items'][0]['snippet']['title'], yt_id
    except:
        import traceback; traceback.print_exc()
        return None, None


parser.add_argument("-s", "--source", help="Thread to scrape", required=True)
parser.add_argument("-o", "--output", help="File to store the data", required=True)

args = parser.parse_args()

cfg = json.load(open("config.json", "r"))

# Create the reddit instance
reddit = praw.Reddit(
        "ro_moderator_bot",
        user_agent=USER_AGENT,
        username=cfg["user"],
        password=cfg["password"])

# Create source submission instance
source = praw.models.Submission(reddit, url=args.source)

# Get the comments by new and get the reversed list
source.comment_sort = "new"
src_comments = reversed(source.comments.list())

# Create link regex
link = re.compile(r'(https?:\/\/)(\s)?(www\.)?(\s?)(\w+\.)*([\w\-\s]+\/)*(([\w]+)|([\?\=_\-])|(_))*\b')

data = []
# Parse comments
for comm in src_comments:
    # For each parent comment, post in the destination thread
    if comm.is_root and comm.author:
        print("*******\n" + comm.author.name)
        for i in re.finditer(link, comm.body):
            print(i.group())
            title, id = get_yt_title(i.group())

            data.append([id, title, "https://youtu.be/" + id])

csv_out = open(args.output, "w")
csv.writer(csv_out).writerows(data)
