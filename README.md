# YouTube-Archiver
Manage a collection of YouTube video archives

## Dependencies
In order to use Accord's Library - YouTube-Archiver, you will need to download a few executables from other projects:
-  [https://github.com/ytdl-org/youtube-dl/releases](youtube-dl)
-  [https://github.com/wez/atomicparsley/releases](AtomicParser)
-  [https://ffmpeg.org/download.html](FFmpeg)

You'll also need to create a `cookies.txt` file that will provide credentials for youtube-dl to use. This is optional, but it is the only way to archive aged-restricted videos. To generate this `cookies.txt` file, you can use the extension called [https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid](Get cookies.txt) by Rahul Shaw. Simply log in YouTube and click on the extension icon to extract the cookies.

All the executables and the cookies.txt file needs to be included at the root of the repository.

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
