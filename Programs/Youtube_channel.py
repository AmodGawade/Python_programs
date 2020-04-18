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
    # print(results)
    # print(type(results))
    # empty list to store video details
    # videos = []

    for result in results:
        '''        videos.append("(% s) (% s) (% s) (% s) (% s) (% s)" % (result["snippet"]["title"],
                                                               result["snippet"]["tags"],
                                                               result['snippet']['description'],
                                                               result["snippet"]["publishedAt"],
                                                               result['contentDetails'],
                                                               result["statistics"]))
        '''
        # print(result)
        print("video id : %s, Title : %s, view count : %s, "
              "likes : %s, dislikes : %s, comments : %s" % (result['id'], result['snippet']['title'],
                                                            result['statistics']['viewCount'],
                                                            result['statistics']['likeCount'],
                                                            result['statistics']['dislikeCount'],
                                                            result['statistics']['commentCount']
                                                            )
              )


def main_by_id():
    video_id_list = []
    num_videos = input("Enter number of videos : ")
    for i in range(int(num_videos)):
        video_id_list.append(input("Enter video id :"))

    for seq in video_id_list:
        video_details(seq)


def main_by_url():
    channel_id_list = []
    num_videos = input("Enter number of videos : ")
    for i in range(int(num_videos)):
        channel_url = input("Enter video URL: ")
        sliced_url = channel_url.split(sep='/', maxsplit=1)[1]
        channel_id_list.append(sliced_url)
        # https://www.youtube.com/watch?v=090n6gzomgM
    #url : https://www.youtube.com/channel/UCoxcjq-8xIDTYp3uz647V5A

    for seq in channel_id_list:
        video_details(seq)


# Boiler Plate
if __name__ == "__main__":
    main_by_id()
    # main_by_url()


