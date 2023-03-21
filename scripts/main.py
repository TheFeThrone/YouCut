import os
import re
from promptuse import prompt, info, alert
from download import download_video
from segmentation import segment_video
from cut import cut_video
import pytube

def main():
    # define YouTube video URL
    buffer_space = r'                                            '

    video_url = prompt("Video URL", f"{buffer_space}Enter the YouTube URL:{buffer_space}", empty=False)
    if video_url is None:
        alert("Error", "Video URL is empty or you cancelled. Program will exit.", "error")
        quit()

    # define directory
    dirresult = ""
    while dirresult == "":
        try:
            work_dir = prompt("File Path", f"{buffer_space}Enter the download path:{buffer_space}", empty=False)
            dirresult = os.chdir(work_dir)
        except:
            if work_dir is None: 
                alert("Error", "The Path is empty or you cancelled. Program will exit.", "error")
                quit()
            else: alert("Error","The Path does not Exist. Try again", "warning")

    # define output name
    try:
        output_name = prompt("Output Name", 'Enter the name you want to set for the cuts (no \\ / : * ? \" < > | ):', empty=True)
        output_name = re.sub(r'[\\/:*?"<>|]', '', output_name)
    except:
        alert("Error","You pressed cancel", "error")

    # download video and get duration
    print("download "+video_url + " in " + work_dir + "\\"+output_name)
    video_title, max = download_video(video_url)
    print(video_title + " downloaded")

    # prompt for segments & cut video into segments
    segresult = 0
    while segresult == 0:
        try:
            segments = segment_video(max)
            print("FIRST")
            segresult = cut_video(video_title, segments, output_name)
            print("END")
        except:
            alert("Error","There was a problem while cutting. Try to segment it again", "error")

    info("Finished","The video has been successfully cut")

    return

if __name__ == '__main__':
    main()