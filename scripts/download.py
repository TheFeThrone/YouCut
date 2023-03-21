from pytube import YouTube

def download_video(video_url):
    """Downloads the YouTube video at the specified URL and returns its title and duration."""
  
    print("start")
    yt = YouTube(video_url)
    print(f"yt: {yt}")
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(f"stream: {stream}")
    video_title = stream.default_filename
    print(f"video_title: {video_title}")
    stream.download()
    print("stream.download done")
    video_duration = yt.length
    print(f"video_duration: {video_duration}")
    return video_title, video_duration
