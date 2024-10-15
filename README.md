# YouTube Audio Downloader

This Python script allows you to download audio from a YouTube video in your preferred audio format (e.g., MP3, WAV, M4A). It uses the `yt-dlp` library for extracting and converting audio from YouTube videos.

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.6 or higher**  
   Download from: https://www.python.org/downloads/

2. **yt-dlp**  
   yt-dlp is a command-line program to download videos from YouTube and other video platforms. Install it via pip:

   ```bash
   pip install yt-dlp
   ```

3. **FFmpeg**  
   FFmpeg is used by `yt-dlp` to handle audio conversion.  
   Follow the installation instructions for your platform:

   - **Windows**:  
     Download the FFmpeg executable from https://ffmpeg.org/download.html and add it to your system’s PATH.
   - **Linux/macOS**:  
     You can install FFmpeg via your package manager. For example:

     ```bash
     sudo apt install ffmpeg   # For Ubuntu/Debian
     brew install ffmpeg       # For macOS
     ```

## How to Use

1. Clone or download this script to your local machine.

2. Run the script using Python:

   ```bash
   python <script_name>.py
   ```

3. You will be prompted to:

   - Enter the URL of the YouTube video.
   - Enter the desired audio format (e.g., mp3, wav, m4a). If no format is provided, the default will be `mp3`.

4. The script will download and extract the audio from the YouTube video, saving it to the current directory with the video title as the filename.

## Example

If you provide the following inputs:

- YouTube URL: `https://www.youtube.com/watch?v=example`
- Desired format: `mp3`

The audio will be downloaded and saved as:

```bash
<Video_Title>.mp3
```

## Error Handling

If any errors occur during the download or extraction process, they will be displayed in the terminal.

## License

This script is free to use and modify.

## Notes

- Only single videos can be downloaded at a time as playlists are disabled in the script.
- Ensure FFmpeg is properly installed and added to your system PATH to avoid conversion errors.
