from pytube import YouTube
import os

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'\rDownloading: {percentage_of_completion:.2f}%', end='')

def complete_function(stream, file_path):
    print(f'\nDownload complete: {file_path}')

def download_captions(yt, download_folder):
    captions = yt.captions
    if 'en' in captions:
        caption = captions['en']
        caption_file = os.path.join(download_folder, f"{yt.title}_en.srt")
        with open(caption_file, "w", encoding="utf-8") as file:
            file.write(caption.generate_srt_captions())
        print(f"Downloaded English caption to {caption_file}")
    else:
        print("No English captions available for this video.")

def download_youtube_video(video_url):
    try:
        print('Download Started ...')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the download folder relative to the script directory
        download_folder = os.path.join(script_dir, "downloads")
        
        # Ensure the download folder exists
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Create a YouTube object
        yt = YouTube(video_url, on_progress_callback=progress_function, on_complete_callback=complete_function)

        # Get the first audio-only stream available
        stream1 = yt.streams.filter(only_audio=True).first()

        if stream1:
            # Download the audio to the specified folder
            stream1.download(output_path=download_folder)
            print(f"Downloaded: {yt.title} to {os.path.abspath(download_folder)}!")
            
            # Download captions
            download_captions(yt, download_folder)
        else:
            print("No audio stream available for download.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Press Enter Key to Continue ...")
    input()

# Example usage
if __name__ == "__main__":
    print("Enter the URL for Audio:")
    url = input()
    download_youtube_video(url)
