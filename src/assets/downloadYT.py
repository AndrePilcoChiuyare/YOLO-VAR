from pytube import YouTube

def download_youtube_video(video_url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter YouTube video URL: ")
    output_path = input("Enter the output path (press Enter for the current directory): ")

    if not output_path:
        output_path = '.'

    download_youtube_video(video_url, output_path)