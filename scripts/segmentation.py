from promptuse import prompt

def segment_video(max_duartion):
    # prompt for segments
    print("function call")
    segments_prompt = f"Enter segment times (in s), separated by commas between 0 and {max_duartion} [ex: 0,1,1,2 for 0-1 and 1-2]:"
    print("prompt coming")
    segments_input = prompt(rf"Segments", segments_prompt, empty=True)
    print("prompt came")
    segments_input = segments_input.split(',')
    print("prompt finished")
    segments = []
    for i in range(len(segments_input)//2):
        start = int(segments_input[i*2])
        end = int(segments_input[i*2+1])
        if start < 0:
            start = 0
        if end > max_duartion:
            end = max_duartion
        segments.append((start, end))
    
    # if no segments specified, set to max video length
    if not segments:
        segments.append((0, max))

    return segments