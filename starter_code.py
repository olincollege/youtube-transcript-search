"""_summary_
"""

from youtube_channel_transcript_api import YoutubeChannelTranscripts
from keys import youtube_api_key

# import csv

CHANNEL_NAME = 'Tapakapa'

channel_getter = YoutubeChannelTranscripts(CHANNEL_NAME, youtube_api_key)

# videos_data, videos_errored = channel_getter.get_transcripts()

videos_errored = channel_getter.write_transcripts( \
    f'transcript_data/{CHANNEL_NAME}/', just_text=True)
# videos_errored = channel_getter.write_transcripts(f' \
# transcript_data/{CHANNEL_NAME}/')
