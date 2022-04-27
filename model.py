"""_summary_
"""

import os
import json
import get_data


class Channel():
    """_summary_
    """

    def __init__(self, channel_name):
        """_summary_

        Args:
            channel_name (_type_): _description_
            videos (dict):
        """
        self.name = channel_name
        self.videos = {}

        for filename in os.listdir(f"transcript_data/{self.name}"):
            file = os.path.join(f"transcript_data/{self.name}", filename)

            if os.path.isfile(file):
                with open(f'transcript_data/{self.name}/{filename}') as \
                        video_file:
                    video_data = json.load(video_file)

                    vid_id = list(video_data.keys())[0]
                    vid_title = video_data[vid_id]['title']
                    transcript = video_data[vid_id]['captions']

                self.videos[vid_title] = Video(vid_title, vid_id, transcript)


class Video():
    """_summary_
    """

    def __init__(self, title, vid_id, transcript):
        """_summary_

        Args:
            title (_type_): _description_
            vid_id (_type_): _description_
            transcript (_type_): _description_
        """

        self.title = title
        self.id = vid_id
        self.transcript = transcript


class YTSearchModel():
    """_summary_
    """

    def __init__(self, channel_name, keywords):
        """_summary_

        Args:
            channel_name (_type_): _description_
            keywords (_type_): _description_
        """

        self.channel_name = channel_name
        self.keywords = keywords
        self.channel = Channel(self.channel_name)

    def update_search(self, channel_name, keywords):
        """_summary_

        Args:
            channel_name (_type_): _description_
            keywords (_type_): _description_
        """

        self.channel_name = channel_name
        self.keywords = keywords
        self.ingest_jsons()

    def ingest_jsons(self):
        """_summary_
        """

        self.channel = Channel(self.channel_name)

    def pull_transcripts(self, channel_name):
        """_summary_

        Args:
            channel_name (_type_): _description_
        """
        pass
