from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
import os


class Channel():

    def __init__(self, channel_name):
        self.name = channel_name

    def pull_transcripts(self):
        load_dotenv()
        self.channel_getter = YoutubeChannelTranscripts(self.name,
            os.environ['YOUTUBE_API_KEY'])
        self.videos_errored = self.channel_getter.write_transcripts(
            f'transcript_data/{self.name}/', just_text=True)
