#!/Users/amod/venv/bin/python
# Author name : Amod Gawade

'''
AIzaSyCQ82KVkBNF8TZG4Flq_RRaTc9gwfXFq
'''

# library import
from googleapiclient.discovery import build
import pprint

# arguments to be passed to build function
DEVELOPER_KEY = "AIzaSyCQ82KVkBNF8TZG4Flq_RRaTc9gwfXFq"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object
# for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)


def video_details(video_id):
    # Call the videos.list method
    # to retrieve video info
    list_videos_byid = youtube.videos().list(id=video_id, part="id, snippet, contentDetails, statistics").execute()

    # extracting the results from search response
    results = list_videos_byid.get("items", [])
    print(results)
    print(type(results))
    # empty list to store video details
    videos = []

    for result in results:
        videos.append("(% s) (% s) (% s) (% s) (% s) (% s)" % (result["snippet"]["title"],
                                                               result["snippet"]["tags"],
                                                               result['snippet']['description'],
                                                               result["snippet"]["publishedAt"],
                                                               result['contentDetails'],
                                                               result["statistics"]))

    print("Videos:\n", "\n".join(videos), "\n")

# Boiler Plate
if __name__ == "__main__":
    video_id = input("Enter youtube video id : ")
    video_details(video_id)

