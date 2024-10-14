# YoutubeVideoDownload

Code to download youtube video in various formats

To extract audio from a YouTube video on the terminal, you can use the popular tool **youtube-dl** or its modern fork **yt-dlp**. These tools allow you to download videos and extract the audio.

Here’s how to do it:

### Step 1: Install `yt-dlp` (or `youtube-dl`)

First, make sure you have **yt-dlp** installed. If not, you can install it using `pip`.

```bash
pip install yt-dlp
```

Alternatively, if you're using **youtube-dl**:

```bash
pip install youtube-dl
```

### Step 2: Install `ffmpeg`

You will also need **ffmpeg**, a tool for processing multimedia files, to extract the audio from the video.

On Linux:

```bash
sudo apt install ffmpeg
```

On macOS (via Homebrew):

```bash
brew install ffmpeg
```

On Windows:

1. Download FFmpeg from the official site: https://ffmpeg.org/download.html.
2. Add it to your system's PATH.

### Step 3: Extract the audio

Use the following command to extract audio from a YouTube video:

```bash
yt-dlp -x --audio-format mp3 <YouTube_URL>
```

If you are using `youtube-dl` instead of `yt-dlp`, the command will be:

```bash
youtube-dl -x --audio-format mp3 <YouTube_URL>
```

### Explanation:

- `-x`: Extract audio.
- `--audio-format mp3`: Converts the audio to MP3 format. You can change this to other formats like `aac`, `wav`, or `m4a`.

### Example:

```bash
yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=YOUR_VIDEO_ID
```

This will download the video, extract the audio in MP3 format, and save it to the current directory.

Let me know if you need any further assistance!
