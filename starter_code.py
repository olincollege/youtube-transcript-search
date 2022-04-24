"""_summary_
"""

from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
import os

# import csv

load_dotenv()

CHANNEL_NAME = 'Tapakapa'

channel_getter = YoutubeChannelTranscripts(CHANNEL_NAME, os.environ['YOUTUBE_API_KEY'])

# videos_data, videos_errored = channel_getter.get_transcripts()

videos_errored = channel_getter.write_transcripts( \
    f'transcript_data/{CHANNEL_NAME}/', just_text=True)
# videos_errored = channel_getter.write_transcripts(f' \
# transcript_data/{CHANNEL_NAME}/')
