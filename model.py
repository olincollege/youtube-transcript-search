"""
Model for YouTube transcript search.
"""
import os
import json
from youtube_channel_transcript_api import YoutubeChannelTranscripts
from dotenv import load_dotenv

# load the environment variables
load_dotenv()


class Video():
    """
    Data structure that holds the video details and transcript

    Attributes:
        _title: a string representing the title of the video
        vid_id (property): a string representing the video id
        transcript (property): a string representing the full transcript
            of the video
    """

    def __init__(self, title, vid_id, transcript):
        """
        Args:
            title: a string representing the title of the video
            vid_id: a string representing the video id
            transcript: a string representing the full transcript of the video
        """
        self._title = title
        self._vid_id = vid_id
        self._transcript = transcript.lower()

    @property
    def vid_id(self):
        """
        create read-only attribute vid_id
        """
        return self._vid_id

    @property
    def transcript(self):
        """
        create read-only attribute transcript
        """
        return self._transcript

    def __repr__(self):
        """
        Return video title and URL.
        """
        url = f"https://www.youtube.com/watch?v={self._vid_id}"
        return f"{self._title}: {url}"


class Channel():
    """
    Data structure that creates and stores video objects for every video on the
    channel.

    Attributes:
        _channel: a string representing the channel name.
        videos (property): a dictionary representing each video on the channel
            callable by title.
    """

    def __init__(self, channel):
        """
        Args:
            channel: a string representing the channel name.
        """
        self._channel = channel
        self._videos = {}
        self._make_video_objects()

    @property
    def videos(self):
        """
        create read-only attribute videos
        """
        return self._videos

    def _make_video_objects(self):
        """
        Convert each video file to a video object and store in a dictionary.
        """
        # Find list of files in channel folder
        video_files = self.find_files(f"transcript_data/{self._channel}")
        for file in video_files:
            if os.path.isfile(file):  # Only operate on files, not directories
                with open(file, encoding="utf-8") as video_file:
                    # Load data from JSON file
                    video_data = json.load(video_file)

                    # If video file is not empty
                    if video_data is not None:
                        # assign video object attributes
                        vid_id = list(video_data.keys())[0]
                        vid_title = video_data[vid_id]['title']
                        transcript = video_data[vid_id]['captions']
                        # create video object, assign attributes, add to dict
                        self._videos[vid_title] = Video(
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

    Attributes:
        _current_channel_name: string representing the channel to be searched
        _keywords: list of strings representing keywords
        channels (property): dictionary of channel objects that have been loaded
            into program memory.
        results (property): list of tuples with search results
    """

    def __init__(self, current_channel_name, keywords, available_channels):
        """
        Creates new channel object and establishes keywords.

        Args:
            current_channel_name: string representing the channel to be searched
            keywords: list of strings representing keywords
            available_channels: dictionary representing what channels are
                already locally downloaded.
        """
        # set the channel being searched.
        self._current_channel_name = current_channel_name

        # set keywords
        self._keywords = keywords

        # if there is no existing data, create it
        if os.path.isdir('./transcript_data') is False:
            os.mkdir('./transcript_data')

        # if the channel data isn't already in the existing data, download it.
        if self._current_channel_name not in available_channels:
            # make directory for new channel
            os.mkdir(f'./transcript_data/{self._current_channel_name}')
            self._get_channel_video_data()

        # update the dictionary of available channels.
        self._channels = {self._current_channel_name: Channel(
            self._current_channel_name)}

        # search
        self._results = self._search()

    @property
    def results(self):
        """
        create read-only attribute results
        """
        return self._results

    @property
    def channels(self):
        """
        create read-only attribute channels
        """
        return self._channels

    def update_search(self, current_channel_name, keywords, available_channels):
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

        # update the channel being searched.
        self._current_channel_name = current_channel_name
        # if the channel data isn't already downloaded locally, download it.
        if self._current_channel_name not in available_channels:
            os.mkdir(f'./transcript_data/{self._current_channel_name}')
            self._get_channel_video_data()

        # update keywords
        self._keywords = keywords

        # See if the requested channel is already read into memory
        if self._current_channel_name not in self._channels:
            # reads JSONs if they haven't been already
            self._channels[self._current_channel_name] = Channel(
                self._current_channel_name)

        self._results = self._search()

    def _get_channel_video_data(self):
        """
        Fetch and organize relevant metadata for all videos on a youtube
        channel from the API.

        Each JSON contains the data from one video.
        """
        try:
            # call API
            channel_getter = YoutubeChannelTranscripts(
                self._current_channel_name, os.environ['YOUTUBE_API_KEY'])

            # write data to JSONs
            channel_getter.write_transcripts(
                f'./transcript_data/{self._current_channel_name}/',
                just_text=True)
        except IndexError:
            # delete the directory if it was created
            os.rmdir(f'./transcript_data/{self._current_channel_name}/')

    def _search(self):
        """
        Search every video transcript for keywords.

        Returns:
            results: a list of tuples representing YouTube videos with a video
                obj, total count of keywords, and list of keys included in the
                transcript.
        """
        results = []
        for _, vid_obj in \
                self._channels[self._current_channel_name].videos.items():

            key_inclusion = 0  # if a key is included in a video
            score = 0  # total time all keys appear in a video

            for key in self._keywords:
                # convert to lower case
                key_count = vid_obj.transcript.count(key.lower())

                # calculate key_inclusion and score per key, per video
                if key_count > 0:
                    key_inclusion += 1
                    score += key_count

            # if the word appears at least once in a video
            if score > 0:
                results.append((vid_obj, score, key_inclusion,
                                len(self._keywords)))
        # sort list with greatest scores first
        results.sort(key=lambda k: k[1], reverse=True)
        return results
