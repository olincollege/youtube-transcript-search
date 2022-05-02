"""
Model for YouTube transcript search.
"""
import os
import json
from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv
# load the API environment
load_dotenv()

class Video():
    """
    Data structure that holds the video details and transcript
    """

    def __init__(self, title, vid_id, transcript):
        """
        Args:
            title: a string representing the title of the video
            _vid_id: a string representing the video id
            transcript: a string representing the full transcript of the video
        """
        self.title = title
        self._vid_id = vid_id
        self.transcript = transcript

    @property
    def vid_id(self):
        """
        create read-only attribute vid_id
        """
        return self._vid_id

    def __repr__(self):
        """
        Return video title and URL.
        """
        url = f"https://www.youtube.com/watch?v={self.vid_id}"
        return f"{self.title}: {url}"


class Channel():
    """
    Data structure that creates and stores video objects for every video on the
    channel.
    """

    def __init__(self, channel):
        """
        Attributes:
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
                with open(file, encoding="utf-8") as video_file:
                    video_data = json.load(video_file)
                    if video_data is not None:
                        # assign video object attributes
                        vid_id = list(video_data.keys())[0]
                        vid_title = video_data[vid_id]['title']
                        transcript = video_data[vid_id]['captions']
                        # create video object, assign attributes, add to dict
                        self.videos[vid_title] = Video(
                            vid_title, vid_id, transcript)

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
        video_files = []
        # Iterate over all the entries
        for entry in files:
            # Create full path
            full_path = os.path.join(directory, entry)
            # If entry is a directory then get the list of files in directory
            if os.path.isdir(full_path):
                video_files = video_files + self.find_files(full_path)
            else:
                video_files.append(full_path)

        return video_files


class YTSearchModel():
    """
    Searches YouTube channel transcripts for keywords.
    """

    def __init__(self, current_channel_name, keywords):
        """
        Creates new channel object and establishes keywords.

        Args:
            current_channel_name: string representing the channel to be searched
            keywords: list of strings representing keywords
        """
        # set the channel being searched.
        self.current_channel_name = current_channel_name
        # set keywords
        self.keywords = keywords

        # if there is no existing data, create it
        if os.path.isfile('./transcript_data') is False\
        or len(os.listdir('./transcript_data')) == 0:
            os.makedirs(f'./transcript_data/{self.current_channel_name}/')
            self.get_channel_video_data()
            # update the dictionary of available channels.
            self.channels = {self.current_channel_name: Channel(self.\
                current_channel_name)}

        # if the channel data isn't already in the existing data, download it.
        elif self.current_channel_name not in self.available_channels:
            # make directory for new channel
            os.mkdir(f'./transcript_data/{self.current_channel_name}')
            self.get_channel_video_data()

            # update the dictionary of available channels.
            self.channels = {self.current_channel_name: Channel(
                self.current_channel_name)}

        # search
        self.results = self.search()

    def update_search(self, current_channel_name, keywords):
        """
        Update channel name and keywords for new search and channel. A new
        channel object is created if it hasn't been already.

        Args:
            current_channel_name: string representing the channel to be
            searched.
            keywords: list of strings representing search terms.
            available_channels: dictionary representing what channels are
            already locally downloaded.
        """
        self.update_available_channels()

        # update the channel being searched.
        self.current_channel_name = current_channel_name
        # if the channel data isn't already downloaded locally, download it.
        if self.current_channel_name not in self.available_channels:
            os.mkdir(f'./transcript_data/{self.current_channel_name}')
            self.get_channel_video_data()

        # update keywords
        self.keywords = keywords

        # See if the requested channel is already read into memory
        if self.current_channel_name not in self.channels:
            # reads JSONs if they haven't been already
            self.channels[self.current_channel_name] = Channel(
                self.current_channel_name)

        self.results = self.search()

    def update_available_channels(self):
        """
        Update record of channels stored locally by the user.
        """
        # list of channels already downloaded
        self.available_channels = next(os.walk('./transcript_data'))[1]

    def get_channel_video_data(self):
        """
        Fetch and organize relevant metadata for all videos on a youtube
        channel from the API.

        Each JSON contains the data from one video.
        """
        # call API
        channel_getter = YoutubeChannelTranscripts(
            self.current_channel_name, os.environ['YOUTUBE_API_KEY'])

        # write data to JSONs
        channel_getter.write_transcripts(
            f'transcript_data/{self.current_channel_name}/', just_text=True)

    def search(self):
        """
        Search every video transcript for keywords.

        Returns:
            results: a list of YouTube videos in order of relevance.
        """
        results = []
        for _, vid_obj in \
                self.channels[self.current_channel_name].videos.items():
            score = vid_obj.transcript.count(self.keywords[0])
            if score > 0:
                results.append((vid_obj, score))
        # sort list with greatest scores first
        results.sort(key=lambda k: k[1], reverse=True)
        return results
