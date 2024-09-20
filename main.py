import requests
from bs4 import BeautifulSoup
import re

# Function to scrape and download the MP4 file
def download_panopto_video(panopto_url, output_filename="video.mp4"):
    # Get the Panopto page content
    response = requests.get(panopto_url)
    
    if response.status_code != 200:
        print(f"Failed to access Panopto URL. Status code: {response.status_code}")
        return
    
    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Look for the video URL embedded in the script tag (usually contains ".mp4" link)
    scripts = soup.find_all('script')
    
    video_url = None
    for script in scripts:
        if 'mp4' in script.text:
            # Use regex to find the MP4 link in the script tag
            match = re.search(r'(https?://.*\.mp4)', script.text)
            if match:
                video_url = match.group(1)
                break
    
    if not video_url:
        print("Couldn't find an MP4 link on the page.")
        return
    
    print(f"Downloading video from: {video_url}")
    
    # Download the video
    video_response = requests.get(video_url, stream=True)
    total_size = int(video_response.headers.get('content-length', 0))
    chunk_size = 1024
    
    # Write the content to a file
    with open(output_filename, 'wb') as video_file:
        for data in video_response.iter_content(chunk_size=chunk_size):
            video_file.write(data)
    
    print(f"Video downloaded successfully: {output_filename}")

# Example usage
panopto_url = 'https://sandiego.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=adb5a860-41a0-418b-9c99-b1e70127d7f4'
download_panopto_video(panopto_url, 'downloaded_video.mp4')
