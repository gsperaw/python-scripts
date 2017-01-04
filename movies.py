import fnmatch
import os
import shutil

rootPath = '/Volumes/Multimedia/video/Movies/'
destDir = rootPath

matches = []
for root, dirnames, files in os.walk(rootPath):
    for filename in files:
        if filename.endswith(('.mp4', '.m4v', '.avi', '.mkv')) and not filename.startswith(('._')) and (root is not '/Volumes/Multimedia/video/Movies/'):
          matches.append(os.path.join(root, filename))
          print(os.path.join(root, filename))
          shutil.move(os.path.join(root, filename), os.path.join(destDir, filename))

print len(matches)
