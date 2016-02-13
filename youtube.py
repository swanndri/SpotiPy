#!/usr/bin/python
'''
Example of youtube api result

{
'id': {'kind': 'youtube#video', 'videoId': 'YQHsXMglC9A'},

'snippet': {'
    title': 'Adele - Hello', 'liveBroadcastContent': 'none', 'publishedAt': '2015-10-23T06:54:18.000Z', 
    'thumbnails': {
        'medium': {'url': 'https://i.ytimg.com/vi/YQHsXMglC9A/mqdefault.jpg', 'width': 320, 'height': 180}, 
        'high': {'url': 'https://i.ytimg.com/vi/YQHsXMglC9A/hqdefault.jpg', 'width': 480, 'height': 360}, 
        'default': {'url': 'https://i.ytimg.com/vi/YQHsXMglC9A/default.jpg', 'width': 120, 'height': 90}
    }, 
    'channelId': 'UComP_epzeKzvBX156r6pm1Q', 
    'channelTitle': 'AdeleVEVO', 
    'description': "'Hello' is taken from the new album, 25, out November 20. http://adele.com Available now from iTunes http://smarturl.it/itunes25 Available now from Amazon ..."
    }, 
    
'kind': 'youtube#searchResult', 
'etag': '"DsOZ7qVJA4mxdTxZeNzis6uE6ck/j0uEstXCXOhrDqDegEBmEeHqsBM"'
}
'''

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import youtube_dl


class Youtube_API:
    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
    DEVELOPER_KEY = "AIzaSyAHQx92XArMtbyaupPySzPzbdQt-W3Izrs"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    def youtube_search(self, query_string, max_results=25):
        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
                        developerKey=self.DEVELOPER_KEY)

        search_response = youtube.search().list(
            q=query_string,
            type="video",
            part="id,snippet",
            maxResults=max_results
        ).execute()

        videos = []

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append({'video_title': search_result["snippet"]["title"],
                               'video_id': search_result["id"]["videoId"],
                               'video_url': 'https://www.youtube.com/watch?v=' + search_result["id"]["videoId"]})
        return videos

    def youtube_download(self, id):

        """
        Set up options for youtube-dl.
            - Dir is defd by file name, should allow user to set where they want audio files to dl.
            - Downloading all files as mp3, probz 4 the best.
            - Currently only allow for best quality audio (late game audio quality choice)

        Return \dir\id.tmp as this is the filename
        """
        download_dir = "static\\audio\\"
        file_extension = ".tmp"
        options = {
            'format': 'bestaudio/best',  # choice of quality
            'extractaudio': True,  # only keep the audio
            'audioformat': "mp3",  # convert to mp3
            'outtmpl': download_dir+'%(id)s'+file_extension,  # name the file the ID of the video
            'noplaylist': True,}  # only download single song, not playlist

        ydl = youtube_dl.YoutubeDL(options)
        info = ydl.extract_info(str(id), download=True)

        return (download_dir + str(id) + file_extension).replace('\\','/')



