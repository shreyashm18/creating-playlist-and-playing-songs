from pygame import mixer
import os
import re
mixer.init()
song_playlist=[]
folder=input('enter path of folder where you want to search your songs\n')
song=input("enter song name\n")
while song:
	song_containing_name=[]
	song_ext=song+'.mp3'
	def pathFinder():
		found=False
		for (root,dirs,files) in os.walk(folder,topdown=True):
			#print(root)
			#print(dirs)
			#print(files)
			#print('------------')
			for f in files:
				if re.findall(song,f):
					if os.path.splitext(f)[1]=='.mp3':
						print('index = ',files.index(f))
						print(f'root = {root}')
						song_path=root+'\\'+f
						song_containing_name.append(song_path)
			'''if song in files:
				found=True
				print('index = ',files.index(song))
				print(f'root = {root}')
				#print(f'dirs = {dirs}')
				song_path=root+'\\'+song
				return song_path,found'''
		if len(song_containing_name)>1:
			print(f'we have found these songs which contains {song} word in name, which song u want just enter its position or 0 if song is not in list')
			print(song_containing_name)
			while True:
				pos=int(input('enter valid position\n'))
				if pos!=0 and (pos-1)<len(song_containing_name):
					found=True
					song_path=song_containing_name[pos-1]
					return song_path,found
				elif (pos-1)>len(song_containing_name):
					print('Wrong Input\n')
		elif len(song_containing_name)==1:
			found=True
			return song_containing_name[0],found
		return 'song not found',found
	song_path,found=pathFinder()
	if found:
		if song_path not in song_playlist:
			song_playlist.append(song_path)
		else:
			print(f'{song} already present in playlist at {(song_playlist.index(song_path)+1)} position')
	else:
		print(f'{song} {song_path}')
	song=input("enter next song name\n")
playlist_len=len(song_playlist)
print(f'Your playlist is {song_playlist}\n')
if playlist_len>0:
	i=0
	print(song_path)
	mixer.music.load(song_playlist[i])
	mixer.music.set_volume(25)
	mixer.music.play()
	print('song is playing')
	print('press p to pause the song, r for resuming, n for next song, b for previous song and e to stop')
	print('you can also give number of the song to jump to that song directly')
	while True:
		inp=input('>>>')
		inp=''.join(inp.split())
		try:
			if int(inp):
				inp=int(inp)
		except:
			pass
		if inp=='p':
			mixer.music.pause()
			print('song paused')
		elif inp=='r':
			mixer.music.unpause()
			print('song resumes')
		elif inp=='n':
			if not i==(playlist_len-1):
				i+=1
				print(i)
				print(song_playlist[i])
				mixer.music.load(song_playlist[i])
				mixer.music.play()
				print(f'playing {os.path.split(song_playlist[i])[-1]}')
			else:
				print('This is the last song in playlist')
		elif inp=='b':
			if not i==0:
				i-=1
				print(i)
				print(song_playlist[i])
				mixer.music.load(song_playlist[i])
				mixer.music.play()
				print(f'playing {os.path.split(song_playlist[i])[-1]}')
			else:
				print('This is the first song in playlist')		
		elif isinstance(inp,int):
			if (inp-1)==i:
				print('same song is playing')
			elif(inp-1)<0 or (inp-1)>(playlist_len-1):
				print('wrong input')
			else:
				i=inp-1
				mixer.music.load(song_playlist[inp-1])
				mixer.music.play()
				print(f'playing {os.path.split(song_playlist[inp-1])[-1]}')
		#elif inp=='0':
		#	print('wrong input')
		elif inp=='e':
			mixer.music.stop()
			print('song stops')
			break
		else:
			print('wrong input')
else:
	print(song_path)