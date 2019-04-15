# Eureddision tools
This repository contains tools for managing various types of Eureddision threads, as they are organized on /r/Romania.

### Prerequisites:
- File named `config.json` which contains Reddit credentials. The format is the following:
```
{
    "user": Reddit username to post with,
    "password": Password for the account
}
```

- File named `client_secret.json` which contains YouTube API credentials. This can be obtained through your GCP account.

### Tools:
- `get_songs_from_playlist.py` - Retrieves songs from a YouTube playlist and saves them as CSV
- `get_songs_from_thread.py` - Retrieves YouTube links from a Reddit thread and saves them as CSV.
- `post_songs.py` - Posts songs that are listed in a CSV file to a Reddit thread.
