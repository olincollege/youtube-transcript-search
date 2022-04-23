from keys import *

from youtube_channel_transcript_api import YoutubeChannelTranscripts
# import csv

channel_name = 'Tapakapa'

channel_getter = YoutubeChannelTranscripts(channel_name, youtube_api_key)

# videos_data, videos_errored = channel_getter.get_transcripts()

videos_errored = channel_getter.write_transcripts(f'transcript_data/{channel_name}/', just_text=True)
# videos_errored = channel_getter.write_transcripts(f'transcript_data/{channel_name}/')

