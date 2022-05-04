# Usage

## How to use

Navigate to the repository directory in terminal and run
`python run_transcript_search.py` or `python3 run_transcript_search.py`.

The program requires transcript data to be downloaded locally before it can search. Follow the prompts to either search existing channels or download a new one (Note: make sure channel names are spelled *exactly* as they appear on YouTube). Channels with a lot of data may take some time to download for the initial search.

To search, enter comma separated keywords or phrases. These strings (with various versions of capitalization) will be searched for in the transcript data.

Results are scored based on the number of occurrences of all keywords within a video. Only the top 5 videos are displayed by default, however this can be easily modified in the `draw_results` method under the `ViewTerminal` class.

### the transcript_data directory
When a new channel's transcript data is downloaded, a new directory with the channel name is created under `transcript_data`. To delete a channel from local memory, simply delete the channel's directory. Do not delete `transcript_data` itself. 

## License: GNU GPL V3
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)    
<!-- `[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)` -->