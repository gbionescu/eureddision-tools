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

def get_yt_titles(playlist, pageToken=None):
    results = youtube.playlistItems().list(
        part='snippet',
        maxResults=50,
        pageToken=pageToken,
        playlistId=playlist
        ).execute()

    return results

parser.add_argument("-p", "--playlist", help="Playlist to fetch", required=True)
parser.add_argument("-o", "--output", help="File to store the data", required=True)

args = parser.parse_args()

data = []
nextPage = None

while True:
    result = get_yt_titles(args.playlist, nextPage)

    for item in result["items"]:
        id = item["snippet"]["resourceId"]["videoId"]
        title = item["snippet"]["title"]
        data.append([id, title, "https://youtu.be/" + id])

    if "nextPageToken" not in result:
        break

    nextPage = result["nextPageToken"]

csv_out = open(args.output, "w")
csv.writer(csv_out).writerows(data)
