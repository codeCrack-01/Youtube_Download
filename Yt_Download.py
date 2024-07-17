from pytube import YouTube
import os

def complete_function(stream, file_path):
    print(f'\nDownload complete: {file_path}')

def download_youtube_video(video_url, res):
    try:
        print('Download Started ...')
        # Get the path to the user's home directory
        home_dir = os.path.expanduser('~')

        # Define the Downloads folder path
        download_folder = os.path.join(home_dir, 'Downloads')
        
        # Ensure the download folder exists
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Create a YouTube object
        yt = YouTube(video_url, on_complete_callback=complete_function)

        # Get the highest resolution video stream available
        stream = yt.streams.get_by_resolution(res)

        if stream:
            # Download the video to the specified folder
            stream.download(output_path=download_folder)
            print(f"\nDownloaded: {yt.title} to {os.path.abspath(download_folder)}")
        else:
            print("No video stream available for download.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Press Enter Key to Continue ...")
    input()

# Example Usage

if __name__ == "__main__":
    print("Enter the URL:")
    url = input().strip()
    print("\nEnter The Resolution ['720p', '480p', '360p', '240p' or '144p']")
    res = input()
    download_youtube_video(url, res)
    