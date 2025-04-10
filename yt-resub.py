import csv
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import re

def get_youtube_service(api_key):
    """Build and return a YouTube API service object."""
    return googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

def extract_channel_id_from_url(url):
    """Extracts the channel ID from a YouTube channel URL."""
    match = re.search(r"channel/([A-Za-z0-9_-]+)", url)
    if match:
        return match.group(1)
    else:
        return None

def load_subscriptions_from_takeout_csv(csv_path):
    """Load subscription data from Google Takeout CSV file, using Channel URL."""
    subscriptions = []
    try:
        with open(csv_path, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader) #skip header row
            for row in reader:
                try:
                    channel_url = row[1]  # Channel URL is in column B (index 1)
                    channel_id = extract_channel_id_from_url(channel_url)
                    if channel_id:
                        subscriptions.append({"resourceId": channel_id})
                    else:
                        print(f"Warning: Could not extract channel ID from URL: {channel_url}")
                except IndexError:
                    print(f"Warning: malformed row {row}")
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
        return None
    return subscriptions

def subscribe_to_channel(youtube, channel_id):
    """Subscribe to a YouTube channel."""
    try:
        request = youtube.subscriptions().insert(
            part="snippet",
            body={
                "snippet": {
                    "resourceId": {
                        "channelId": channel_id
                    }
                }
            }
        )
        response = request.execute()
        return response
    except HttpError as e:
        print(f"Error subscribing to channel {channel_id}: {e}")
        return None

def main():
    """Main function to handle subscription restoration."""
    api_key = input("Enter your YouTube Data API v3 key: ")
    csv_path = input("Enter the path to your Google Takeout YouTube subscriptions CSV file: ")

    youtube = get_youtube_service(api_key)
    subscriptions = load_subscriptions_from_takeout_csv(csv_path)

    if subscriptions is None:
        return

    print(f"Found {len(subscriptions)} channels in your CSV.")

    for sub in subscriptions:
        print(f"Subscribing to channel ID: {sub['resourceId']}...")
        response = subscribe_to_channel(youtube, sub["resourceId"])
        if response:
            print(f"Subscribed to channel ID: {sub['resourceId']} successfully.")
        else:
            print(f"Failed to subscribe to channel ID: {sub['resourceId']}.")

if __name__ == "__main__":
    main()