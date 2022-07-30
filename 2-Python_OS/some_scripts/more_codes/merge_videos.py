#!/usr/bin/env python3

import sys
from moviepy.editor import *

clip1=VideoFileClip(sys.argv[1])
clip2=VideoFileClip(sys.argv[2])

final_clip= concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("Merged.mp4")
