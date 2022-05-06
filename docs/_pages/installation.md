---
title: Installation
permalink: /installation/
---

## Clone the Repo
Run the following to clone this repo:
```bash
git clone https://github.com/olincollege/youtube-transcript-search
```

## Install Dependencies
Install the packages used in this project by running the following:

```bash
pip install -r requirements.txt
```

## API Key

 1. Create a free Google Cloud project at [https://console.cloud.google.com/projectcreate](https://console.cloud.google.com/projectcreate)
 2. Enable the YouTube Data API V3 for your project at [https://console.cloud.google.com/apis/library/youtube.googleapis.com](https://console.cloud.google.com/apis/library/youtube.googleapis.com)
 3. Create an API key for your project at [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
 4. Copy API key to keyboard
 5. In root directory of repo, add a file named `.env` and add the line: `YOUTUBE_API_KEY=<my-api-key>` replacing `<my-api-key>` with the key that you copied.