from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * # ImageClip
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-half-second")
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')


this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]

# filepaths = []
# for fname in this_dir:
#     if fname.endswith("jpg"):
#         path = os.path.join(thumbnail_dir, fname)
#         filepaths.append(path)
# 1st method
# print(filepaths)
# clip = ImageSequenceClip(filepaths, fps=1)
# clip.write_videofile(output_video)   # output them to videoa

# 2nd method Walk
directory = {}

for root, dirs, files in os.walk(thumbnail_per_frame_dir): # walk thro all dir
    for fname in files:
        filepath = os.path.join(root, fname) # give filename for @file
        try:
            key = float(fname.replace(".jpg", "")) #coz its a jpg image
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):  # name of file in dir in order
    filepath = directory[k]
    new_paths.append(filepath)

# clip = ImageSequenceClip(new_paths, fps=10)
# clip.write_videofile(output_video)

my_clips = [] #Imageclip
for path in list(new_paths):
    frame = ImageClip(path)
    # print(frame.img) # numpy array
    my_clips.append(frame.img)


clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_video)