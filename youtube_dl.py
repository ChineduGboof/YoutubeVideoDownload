import yt_dlp

# Function to extract audio from a YouTube video
def download_audio(url, output_format='mp3'):
    # Options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': output_format,  # Desired audio format
            'preferredquality': '192',  # Set audio quality
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title
        'noplaylist': True,  # Download only a single video, not a playlist
    }

    # Create an instance of YoutubeDL with the specified options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Attempt to download the audio
            ydl.download([url])
            print("Download completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    output_format = input("Enter the desired audio format (mp3, wav, m4a, etc.): ") or 'mp3'  # Default to 'mp3' if no input
    download_audio(video_url, output_format)
