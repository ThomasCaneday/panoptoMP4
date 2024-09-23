# panoptoMP4

This Python script allows you to download MP4 videos hosted on Panopto. It scrapes the Panopto page for the embedded video link and downloads the video file directly.

## Features

- Scrapes Panopto web pages using BeautifulSoup.
- Extracts the MP4 video URL using regex.
- Downloads the video in chunks, allowing for large file downloads without memory overload.

## Prerequisites

Before running the script, make sure you have Python installed along with the following libraries:

- `requests`: For sending HTTP requests to the Panopto page and downloading the video.
- `beautifulsoup4`: For parsing the HTML content of the page.
- `re`: For extracting the MP4 URL via regular expressions.

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Set the `panopto_url` variable to the Panopto page URL that contains the video you want to download.
2. Call the `download_panopto_video()` function, passing in the Panopto URL and an optional filename for the downloaded video.

Example:

```python
panopto_url = 'https://your_panopto_video_link_here'
download_panopto_video(panopto_url, 'output_video.mp4')
```

### Arguments:
- `panopto_url` (str): The URL of the Panopto video page.
- `output_filename` (str): (Optional) The name of the file to save the video. Default is `video.mp4`.

## Example

```python
panopto_url = 'https://sandiego.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=adb5a860-41a0-418b-9c99-b1e70127d7f4'
download_panopto_video(panopto_url, 'downloaded_video.mp4')
```

## Notes

- This script assumes that the Panopto video link is embedded in the HTML content in a script tag. If Panopto changes its page structure, the script may need adjustments.
- Make sure you have proper access rights to the Panopto video. Videos might be protected by authentication.
