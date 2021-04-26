""" Pull All Youtube Videos from a Playlist """

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from pytube import YouTube
import yaml
import re

DEVELOPER_KEY = "AIzaSyDh2GQjM4XAsVpmeCNkkcotsEPvwjK_TZ4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def fetch_all_youtube_videos(playlistId):
    """
    Fetches a playlist of videos from youtube
    We splice the results together in no particular order

    Parameters:
        parm1 - (string) playlistId
    Returns:
        playListItem Dict
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    res = youtube.playlistItems().list(
    part="snippet",
    playlistId=playlistId,
    maxResults="50"
    ).execute()

    nextPageToken = res.get('nextPageToken')
    while ('nextPageToken' in res):
 
        nextPage = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults="50",
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']
        if 'nextPageToken' not in nextPage:
            res.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']
        
    return res

if __name__ == '__main__':
  #entering the playlist id
  #https://www.youtube.com/playlist?list=PLwGdqUZWnOp00IbeN0OtL9dmnasipZ9x8
  playlist_id=input("Enter the link")
  url="https://www.youtube.com/playlist?list=PLwGdqUZWnOp00IbeN0OtL9dmnasipZ9x8"
  regex=r"/(?:(?:\?|&)list=)((?!videoseries)[a-zA-Z0-9_]*)/g"
  str=re.findall(regex,url)
  print(str)
  #videos = fetch_all_youtube_videos("PLwGdqUZWnOp00IbeN0OtL9dmnasipZ9x8")

  i=0;
  r=[]
  
  #appending videoIds in a list
  '''while(i<86):
      r.append(yaml.dump(videos["items"][i]["snippet"]["resourceId"]["videoId"]))
      i=i+1

  #iterating over the list and generating links, later downloading those links one after the other to a specified location.
  for links in r:
      link="https://www.youtube.com/watch?v="+links[0:-5]+"&list=PLwGdqUZWnOp00IbeN0OtL9dmnasipZ9x8" 
      yt = YouTube(link)
      ys = yt.streams.get_highest_resolution()
      print("Downloading...")
      ys.download(r"C:\Users\ASUS\Desktop\Downloads")
  #print(link)'''