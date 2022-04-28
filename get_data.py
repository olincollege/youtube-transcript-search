from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
import os

# import csv
def videos_from_channel (channel):
    """
    fetch and organize relevant metadata for all videos on a youtube channel
    Each JSON contains the data from one video.

    Args:
        channel: a string representing the Youtube Channel name
    """
    load_dotenv()
    channel_getter = YoutubeChannelTranscripts(channel, os.environ['YOUTUBE_API_KEY'])

    # write data to JSONs
    channel_getter.write_transcripts(\
        f'transcript_data/{channel}/', just_text=True)

    # Remove slashes from folder/filenames to delete subfolders

    # errors = os.listdir('My_directory')

    #todo
    # for subfolder in os.listdir(f"transcript_data/{channel}"):
    #     # for each subfolder
    #     if os.path.isdir(subfolder):
    #         # get the file inside
    #         file = os.listdir(subfolder)[0]
    #         # add the folder name to the beginning
    #         # take the file inside and add the folder name to the beginning


    #for each directory in the channel directory, take take the file
    #inside and add the folder name (without the slash) to the beginning of the
    #video file name, then add the video file to the main directory and delete
    #the old subdirectory

    # todo account for




