# YouTube Transcript Search

Search the transcripts of any channel on YouTube for keywords or phrases in your terminal with python.

## Built With

- [youtube-channel-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Getting Started

### Clone the Repo

Run the following to clone this repo:

```bash
git clone https://github.com/olincollege/youtube-transcript-search
```

### Install Dependencies

Install the packages used in this project by running the following:

```bash
pip install -r requirements.txt
```

### API Key

 1. Create a free Google Cloud project at [https://console.cloud.google.com/projectcreate]
 2. Enable the YouTube Data API V3 for your project at [https://console.cloud.google.com/apis/library/youtube.googleapis.com]
 3. Create an API key for your project at [https://console.cloud.google.com/apis/credentials]
 4. Copy API key to keyboard
 5. In root directory of repo, add a file named `.env` and add the line: `YOUTUBE_API_KEY=<my-api-key>` replacing `<my-api-key>` with the key that you copied.

## Usage

Navigate to the repository directory in terminal and run
`python run_transcript_search.py` or `python3 run_transcript_search.py`.

The program requires transcript data to be downloaded locally before it can search. Follow the prompts to either search existing channels or download a new one (Note: make sure channel names are spelled *exactly* as they appear on YouTube). Channels with a lot of data may take some time to download for the initial search.

To search, enter comma separated keywords or phrases. These strings (with various versions of capitalization) will be searched for in the transcript data.

Results are scored based on the number of occurrences of all keywords within a video. Only the top 5 videos are displayed by default, however this can be easily modified in the `draw_results` method under the `ViewTerminal` class.

### the transcript_data directory

When a new channel's transcript data is downloaded, a new directory with the channel name is created under `transcript_data`. To delete a channel from local memory, simply delete the channel's directory. Do not delete `transcript_data` itself. 

## Testing

This branch, `testing`, is fully configured to run pytest tests on our program. It is identical to `main` at its core, but comes with a few sets of channel data already downloaded, along with the pytest files themselves. To run the tests, run the following in the root of this branch.

```bash
pytest *.py
```

For the primary release version of the program, please use `main`.

## License

### GNU GPL v3

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)    
