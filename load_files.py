import json

with open('transcript_data/Tapakapa/Cars_Are_Not_the_Problem.json') as video_file:
    video_data = json.load(video_file)
    
    print(video_data)