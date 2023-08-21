#!/bin/python3
import progressbar
import urllib.request
import sys
import os
pbar = None


def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

start=int(sys.argv[1])+789
end=int(sys.argv[2])+790
print(start,' ',end)
for x in range(start,end):
	url='https://saiyanvod.com/media/videos/h264/'+str(x)+'_720p.mp4'
	num=x-789
	print('ep: ',num,' url: ',url)
	try:
		urllib.request.urlretrieve(url, 'ep'+str(num)+'.mp4', show_progress)
	except:
		print("ERROR OCCURED: Failed to download ep",x," Restarting...")
		os.remove('ep'+str(num)+'.mp4')
		x-=1