# YouTube-Archiver
Manage a collection of YouTube video archives

## Dependencies
In order to use Accord's Library - YouTube-Archiver, you will need to download a few executables from other projects:
-  [https://github.com/ytdl-org/youtube-dl/releases](youtube-dl)
-  [https://github.com/wez/atomicparsley/releases](AtomicParser)
-  [https://ffmpeg.org/download.html](FFmpeg)

## Usage
Simply write down video UIDs in the `video-append-uid.txt` file (i.e. dQw4w9WgXcQ). One UID by line, do not include the rest of the URL.
Run `script-list.py`
The output video is located (by default) in `output/[UID]`

## Result
The resulting archive is composed as follows:
- The video, in the highest quality possible for the audio and video (limited to codex compatible with the MP4 container format).
- Highest quality thumbnail, saved as JPG or WebP
- A `.description` file containing the original description of the video
- A `.info.json` file containing most if not all metadata publicly available about the video (duration, uploader, channel_id, tags, available qualities...)
- A `.vtt` file for each subtitle language available.

In addition to the archive, a `collection.csv` is generated. In includes the list of archived videos currently present in the output folder. For each archive, a few information is included: the uploader, the video title, its publication date, its url, and its duration. 
