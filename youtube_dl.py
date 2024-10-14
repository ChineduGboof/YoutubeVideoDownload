import yt_dlp

# Function to extract audio from a YouTube video
def download_audio(url, output_format='mp3'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Save the file as the video title
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_audio(video_url, 'mp3')  # You can change 'mp3' to 'wav', 'm4a', etc.
