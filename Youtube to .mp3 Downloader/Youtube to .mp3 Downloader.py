from pytube import Playlist
from moviepy.editor import *

# DISLCLAIMER make sure you make a new folder for this program since its final
# step will delete files if chosen to do so.

# Please read the Documentation page.

destination = r"Your File's Location"
my_playlist = Playlist('Your youtube playlist web link')

# Step 1: Download your youtube playlist.

for video in my_playlist.videos:
    try:
        out_file = video.streams.filter(mime_type='video/mp4').first().download(output_path=destination)
    except:
        pass
print('Download Done')

# Step 2: Convert all files in folder(destination), from .mp4 to .mp3.

for root, dirs, files in os.walk(destination):
    for file in files:
        if file.endswith('.mp4'):
            mp4_file = os.path.join(root, file)
            base, ext = os.path.splitext(mp4_file)
            mp3_file = base + '.mp3'

            videoclip = VideoFileClip(mp4_file)
            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3_file)
            audioclip.close()
            videoclip.close()

print('Conversion Done')

# Step 4 Delete all files that end with .mp4 for space management.
confirm = input('Are you sure you want to run this part of the program, it will delete'
                'ALL files that end with .mp4 inside selected folder. Y/N')
confirm = confirm.upper()
if confirm == 'Y' or confirm == 'YES':
    for root, dirs, files in os.walk(destination):
        for file in files:
            if file.endswith('.mp4'):
                mp4_file = os.path.join(root, file)
                os.remove(mp4_file)
    print('Cleanup Done')
else:
    print('Done')