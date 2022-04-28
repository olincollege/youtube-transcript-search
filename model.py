"""_summary_
"""
import os
from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
import json
load_dotenv()

class Video():
    """
    Data structure that holds the video details and transcript
    """
    def __init__(self, title, vid_id, transcript):
        """
        Args:
            title: a string representing the title of the video
            vid_id: a string representing the video id
            transcript: a string representing the full transcript of the video
        """
        self.title = title
        self.id = vid_id
        self.transcript = transcript

    def __repr__(self):
        url = f"https://www.youtube.com/watch?v={self.id}"
        return f"{self.title}: {url}"


class Channel():
    """
    Data structure that creates and stores video objects for every video on the
    channel.
    """
    def __init__(self, channel):
        """
        Args:
            channel: a string representing the channel name.
            videos: a dictionary representing each video on the channel
            callable by title.
        """
        self.channel = channel
        self.videos = {}
        self.make_video_objects()

    def make_video_objects(self):
        """
        Convert each video file to a video object and store in a dictionary.
        """
        video_files = self.find_files(f"transcript_data/{self.channel}")
        for file in video_files:
            if os.path.isfile(file):
                with open(file) as video_file:
                    video_data = json.load(video_file)
                    if video_data is not None:
                        # assign video object attributes
                        vid_id = list(video_data.keys())[0]
                        vid_title = video_data[vid_id]['title']
                        transcript = video_data[vid_id]['captions']

                        self.videos[vid_title] = Video(vid_title, vid_id, transcript)

    def find_files(self, directory):
        """
        Get all files in a directory tree.

        Args:
            directory: A string representing the directory

        Returns:
            A list of all files in the directory tree.
        """
        # create a list of files and subdirectories in the given directory
        files = os.listdir(directory)
        video_files = list()
        # Iterate over all the entries
        for entry in files:
            # Create full path
            fullPath = os.path.join(directory, entry)
            # If entry is a directory then get the list of files in directory
            if os.path.isdir(fullPath):
                video_files = video_files + self.find_files(fullPath)
            else:
                video_files.append(fullPath)

        return video_files


class YTSearchModel():
    """_summary_
    """
    def __init__(self, current_channel_name, keywords):
        """
        Creates new channel object and establishes keywords.

        Args:
            current_channel_name (_type_): _description_
            keywords (_type_): _description_
        """
        self.current_channel_name = current_channel_name
        self.keywords = keywords
        self.channels = {self.current_channel_name: Channel(self.current_channel_name)}
        # search
        self.results = self.search()

    def update_search(self, current_channel_name, keywords):
        """
        Update channel name and keywords for new search and channel. A new
        channel object is created if it hasn't been already.

        Args:
            current_channel_name (_type_): _description_
            keywords (_type_): _description_
        """
        self.current_channel_name = current_channel_name
        self.keywords = keywords

        # See if requested channel already read into memory
        if self.current_channel_name not in self.channels.keys():
            # reads JSONs if they haven't been already
            self.channels[self.current_channel_name] = Channel(self.current_channel_name)

        self.results = self.search()

    def get_channel_video_data(self, channel):
        """
        fetch and organize relevant metadata for all videos on a youtube channel
        Each JSON contains the data from one video.

        Args:
            channel: a string representing the Youtube Channel name
        """
        channel_getter = YoutubeChannelTranscripts(channel, os.environ['YOUTUBE_API_KEY'])

        # write data to JSONs
        channel_getter.write_transcripts(\
            f'transcript_data/{channel}/', just_text=True)

    def search(self):
        results = []
        for vid_title, vid_obj in self.channels[self.current_channel_name].videos.items():
            score = vid_obj.transcript.count(self.keywords[0])
            if score > 0:
                results.append((vid_title, score))
        results.sort(key=lambda k: k[1], reverse=True)
        return results
