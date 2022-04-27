from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
import os
import json
import get_data


class Channel():

    def __init__(self, channel_name):
        self.name = channel_name
        self.videos = {}

        for filename in os.listdir(f"transcript_data/{self.name}"):
            f = os.path.join(f"transcript_data/{self.name}", filename)

            if os.path.isfile(f):
                with open(f'transcript_data/{self.name}/{filename}') as video_file:
                    video_data = json.load(video_file)

                    vid_id = list(video_data.keys())[0]
                    vid_title = video_data[vid_id]['title']
                    transcript = video_data[vid_id]['captions']

                self.videos[vid_title] = Video(vid_title, vid_id, transcript)


class Video():

    def __init__(self, title, vid_id, transcript):
        self.title = title
        self.id = vid_id
        self.transcript = transcript


class YTSearchModel():

    def __init__(self, channel_name, keywords):
        self.update_search(channel_name, keywords)

    def update_search(self, channel_name, keywords):
        self.channel_name = channel_name
        self.keywords = keywords
        self.ingest_jsons()

    def ingest_jsons(self):
        self.channel = Channel(self.channel_name)

    def pull_transcripts(self, channel_name):
        get_data.videos_from_channel(channel_name)
