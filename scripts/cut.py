import subprocess
import os

def cut_video(video_title, segments, output_name):
    """Cuts the specified video file into segments and exports each segment as a separate MP4 file."""
    local_env = os.getenv('LOCALAPPDATA')
    ffmpeg_path = local_env + r"\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-6.0-full_build\bin\\ffmpeg.exe"
    print("Processing:", video_title)
    
    try:
        for i, segment in enumerate(segments):
            start_time, end_time = segment
            with open(os.devnull, 'wb') as quiet:
                    subprocess.run([
                        ffmpeg_path, "-i", video_title,
                        "-ss", str(start_time),
                        "-to", str(end_time),
                        "-c", "copy",
                        f"{output_name}_{i+1:02d}.mp4",
                        "-hide_banner"
                        ])
                    print("Cut", i+1, "done")
        return 1
    except:
        return 0
