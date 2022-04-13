import moviepy.editor as mp
import os


def video_resizer(input_folder, format, height, width):

    resolution = (width,height)
    output_folder = f'./resized({width}x{height})'

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for clip_name in os.listdir(input_folder):

        if clip_name.endswith(('mkv', 'mp4', 'mov')):
            clip_path = f'{input_folder}/{clip_name}'
            clip = mp.VideoFileClip(clip_path)
            clip_resized = clip.resize(resolution)
            clip_resized.write_videofile(
                f"{output_folder}/{clip_name.split('.')[0]}({width}x{height})(resized).{format}", threads=8)


if __name__ == '__main__':

    # Path to the folder where video files exist
    input_folder = './to_resize'

    # Desired height of the output
    height = 528

    # Desired width of the output
    width = 704

    # Desired format of the output file
    format = 'mp4'

    try:
        video_resizer(input_folder=input_folder, width=width,
                      height=height, format=format)
    except Exception as e:
        print('Error Occured', e)
