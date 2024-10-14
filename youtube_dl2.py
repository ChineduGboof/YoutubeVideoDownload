import yt_dlp

# Function to list available audio formats for a YouTube video
def list_formats_and_download(url):
    with yt_dlp.YoutubeDL() as ydl:
        # Extract the video information without downloading
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        
        # Filter for audio formats and print them
        audio_formats = [f for f in formats if f['acodec'] != 'none']  # Keep only audio formats
        print("Available audio formats:")
        for i, f in enumerate(audio_formats):
            print(f"{i}: {f['format_id']} - {f['ext']} - {f['abr']} kbps")

        # Allow user to select a format
        selected_index = int(input("Enter the index of the desired audio format: "))
        selected_format = audio_formats[selected_index]['ext']  # Get the selected format's extension
        
        # Download the selected format
        ydl_opts = {
            'format': f'bestaudio[ext={selected_format}]',  # Use the selected audio format
            'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title
            'noplaylist': True,  # Download only a single video, not a playlist
        }

        # Downloading the selected format
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                print("Download completed successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    list_formats_and_download(video_url)
