import requests

import re

from concurrent.futures import ThreadPoolExecutor

import os


#This class only need perma_links of songs ///Last strings of URL

class Song():
	
	def __init__(self , perma_link):
		
		#limit attributes for faster and less memory usage
		__slots__ = ('perma_link' , 'data' , 'key' , 'BASE_URL')
		
		#Base URL for doing api call
		self.BASE_URL = {
			
			"perma_link":"https://www.jiosaavn.com/api.php?__call=webapi.get&token={}&type={}&_format=json&_marker=0",

			"lyrics":"https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&lyrics_id={}&ctx=wap6dot0"
		}
		
		self.perma_link = perma_link
		
		self.data = dict(requests.get(self.BASE_URL["perma_link"].format(self.perma_link , 'song')).json())
		
		self.key = list(self.data.keys())[0]


	def get_data(self): #return song data into dictionery

		return self.data[self.key]

	def get_download_link(self): #return download link of song
		
		download_link = str(self.data[self.key]['media_preview_url'].replace('_96_p.mp4','.mp3'))
		
		download_link = download_link.replace('preview','c' )
		
		return download_link

	def get_lyrics(self): #return lyrics if available else return failure

	  lyric_data = str(requests.get(self.BASE_URL["lyrics"].format(self.key)).content)
	  
	  re_data = re.compile(r"[^\:$\,]+")
	  
	  lyric = re_data.findall(lyric_data)
	  
	  return str(lyric[3]).replace("<br>", "\n")


class Album(object):

	def __init__(self , perma_link):
		self.BASE_URL = "https://www.jiosaavn.com/api.php?__call=webapi.get&token={}&type={}&_format=json&_marker=0"
		self.perma_link = perma_link
		self.data = dict(requests.get(self.BASE_URL.format(self.perma_link , 'album')).json())
	
	#return the json data of songs ,  also can be used as attribute
	@property
	def get_songs(self): 
		return self.data['songs']


	#return list of all download links of songs in album , also can be used as attribute
	@property 
	def get_download_links(self):
		self.download_links = [str(link['media_preview_url']).replace("_96_p.mp4",".mp3") for link in self.data['songs']]
		for i in range(len(self.download_links)):
			self.download_links[i] = self.download_links[i].replace('preview','c')

		return self.download_links

	def write_songs(self , link , title): 
		res = requests.get(link).content
		with open(title+".mp3" , "wb") as f:
			f.write(res)


	#this function download all the songs of using multithreading methode
	#if there any exeception happened during the download the file won't into directory

	def download_all_songs(self , path = os.getcwd()):#pass the desired path to the "path"
		os.chdir(path)
		with ThreadPoolExecutor() as executor:
			executor.map(self.write_songs , self.get_download_links , [song['song'] for song in self.get_songs ])

	
