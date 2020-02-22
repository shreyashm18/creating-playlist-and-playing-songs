from pygame import mixer
import os
mixer.init()
song_playlist=[]
song=input("enter song name")
while song:
	song=song+'.mp3'
	def pathFinder():
		found=False
		for (root,dirs,files) in os.walk('E:\\',topdown=True):
			print(root)
			print(dirs)
			print(files)
			print('------------')
			if song in files:
				found=True
				print('index = ',files.index(song))
				print(f'root = {root}')
				#print(f'dirs = {dirs}')
				song_path=root+'\\'+song
				return song_path,found
			'''else:
				song_path=root'''
		return 'song not found',found
	song_path,found=pathFinder()
	if found:
		song_playlist.append(song_path)
	else:
		print(f'{song} {song_path}')
	song=input("enter next song name")
playlist_len=len(song_playlist)
print(f'Your playlist is {song_playlist}')
if playlist_len>0:
	i=0
	print(song_path)
	mixer.music.load(song_playlist[i])
	mixer.music.set_volume(25)
	mixer.music.play()
	print('song is playing')
	print('press p to pause the song, r for resuming, n for next song, b for previous song and e to stop')
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
		elif inp=='0':
			print('wrong input')
		elif inp=='e':
			mixer.music.stop()
			print('song stops')
			break
else:
	print(song_path)