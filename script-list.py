import csv
import os
import sys
import json

def getTitle(uid):
    fileList = os.listdir('output/' + uid)
    fileList.remove('meta')
    return fileList[0][:-4]

def getMeta(uid):
    fileList = os.listdir('output/' + uid + '/meta')
    jsonFile = [e for e in fileList if '.json' in e][0]
    with open('output/' + uid + '/meta/' + jsonFile) as f:
        return json.load(f)

def secondsToStr(duration):
    hours = duration // 3600
    minutes = duration // 60 % 60
    seconds = duration % 60
    return str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)

def youtubeDL(uid):
    print('Downloading', uid)
    os.system('.\youtube-dl.exe "https://www.youtube.com/watch?v=' + uid + '" -o ".\output\%(id)s\%(title)s.%(ext)s" -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --all-subs --embed-subs --embed-thumbnail --add-metadata --cookies cookies.txt --no-overwrites')
    os.system('.\youtube-dl.exe "https://www.youtube.com/watch?v=' + uid + '" -o ".\output\%(id)s\meta\%(title)s.%(ext)s" --all-subs --write-sub --skip-download --add-metadata --write-thumbnail --write-info-json --write-description --write-annotations --cookies cookies.txt --no-overwrites')
        
def repairCurrentArchives():
    # Verify if some archive are incomplete
    for uid in os.listdir('output/'):
        layer1Content = os.listdir('output/' + uid)

        if not layer1Content:
            print(uid, 'is empty!')

        if 'meta' not in layer1Content:
            print(uid, 'is missing the meta folder')
        else:
            layer2Content = os.listdir('output/' + uid + '/meta/')
            description = [e for e in layer2Content if e[-11:] == 'description']
            json = [e for e in layer2Content if e[-4:] == 'json']
            thumb = [e for e in layer2Content if e[-4:] == 'webp' or e[-3:] == 'jpg']
            
            if len(description) != 1: print(uid, 'is missing its description file')
            if len(json) != 1: print(uid, 'is missing its json file')
            if len(thumb) != 1: print(uid, 'is missing its thumb file')

        mp4 = [e for e in layer1Content if e[-3:] == 'mp4']
        if not mp4:
            print(uid, 'is missing its mp4 file')
            youtubeDL(uid)
        
        elif len(layer1Content) > 2:
            print(uid, 'got temporary file still present')
            
            
            
            
            


repairCurrentArchives()

# Retrieve the list of video UID that we want to append
videosUID = set()
with open('video-append-uid.txt') as file:
    for line in file.readlines():
        videosUID.add(line.replace('\n', ''))
        
downloadedUID = set()
for uid in videosUID:
    if uid not in os.listdir('output/'):
        youtubeDL(uid)
        downloadedUID.add(uid)
    else:
        print('Already downloaded', uid)

# Empty input file
with open('video-append-uid.txt', 'w'): pass

with open('collection.csv', mode ='w', encoding='utf-8', newline='') as file:
  csvFile = csv.writer(file, delimiter='\t')
  csvFile.writerow(['status', 'uploader', 'title', 'date', 'url', 'duration', 'browse'])
  for uid in os.listdir('output/'):
    meta = getMeta(uid)
    status = '🟢'
    title = meta['title']
    url = 'https://youtu.be/' + uid
    duration = secondsToStr(meta['duration'])
    date = meta['upload_date']
    date = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
    uploader = meta['channel']
    csvFile.writerow([status, uploader, title, date, url, duration, 'Private'])
    
