# read_playlist.py
# Reads all items from the DynamoDB Playlist table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key 

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Playlist"


def get_table():
    """Return a reference to the DynamoDB Playlist table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_songs_in_playlist(playlist):
    title = playlist.get("Title", "Unknown Title")
    artist = playlist.get("Artist", "Unknown Artist")
    album = playlist.get("Album", "No ratings")


    print(f"  Title  : {title}")
    print(f"  Artist   : {artist}")
    print(f"  Album : {album}")
    print()

def print_playlist():
    """Scan the entire Playlist table and print each item (song)."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found in playlist. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} song(s):\n")
    for playlist in items:
        print_songs_in_playlist(playlist)


    

    

def main():
    print("===== Reading from DynamoDB =====\n")
    print_playlist()
  


if __name__ == "__main__":
    main()