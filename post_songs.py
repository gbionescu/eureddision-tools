#!/usr/bin/env python3
import praw
import sys
import time
import argparse
import re
import json
import csv

parser = argparse.ArgumentParser()
USER_AGENT = "Eureddision poster by /u/programatorulupeste"

parser.add_argument("-s", "--source", help="CSV to read", required=True)
parser.add_argument("-d", "--destination", help="Thread where to post", required=True)

args = parser.parse_args()
cfg = json.load(open("config.json", "r"))

f= open(args.source)
csv_list = csv.reader(f)

# Create the reddit instance
reddit = praw.Reddit(
        "ro_moderator_bot",
        user_agent=USER_AGENT,
        username=cfg["user"],
        password=cfg["password"])

dest = praw.models.Submission(reddit, url=args.destination)

for row in csv_list:
    body = "[%s](%s)" % (row[1], row[2])

    print(body)
    dest.reply(body)
    time.sleep(5)
