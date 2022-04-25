"""_summary_
"""

import json

with open('transcript_data/Tapakapa/Cars_Are_Not_the_Problem.json') as video_file:
    video_data = json.load(video_file)

    vid_id = list(video_data.keys())[0]
    print(video_data[vid_id]['title'])
