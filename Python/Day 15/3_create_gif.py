from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * # ImageClip
from PIL import Image
from moviepy.video.fx.all import crop  #crop video


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4') #source video

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)

output_path1 = os.path.join(GIF_DIR, 'sample1.gif')
output_path2 = os.path.join(GIF_DIR, 'sample2.gif')

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10, 20) # time you want 10secs n 20sec
subclip = subclip.resize(width=500) #heifgt=320
# subclip.write_gif(output_path1, fps=fps, program='ffmpeg')

#cropping
w, h = clip.size  #already fps declared line 16
subclip2 = clip.subclip(10, 20)
square_cropped_clip = crop(subclip2, width=320, height=320, x_center=w/2, y_center=h/2)

# square_cropped_clip.write_gif(output_path2, fps=fps, program='ffmpeg')