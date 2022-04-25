from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
import os
import json


class Channel():

    def __init__(self, channel_name):
        self.name = channel_name
        self.videos = {}

        for filename in os.listdir(f"transcript_data/{self.name}"):
            f = os.path.join(f"transcript_data/{self.name}", filename)

            if os.path.isfile(f):
                with open('transcript_data/Tapakapa/Cars_Are_Not_the_Problem.json') as video_file:
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

    def __init__(self):
        pass

    def ingest_jsons(self):
        pass

    def pull_transcripts(self):
        pass
