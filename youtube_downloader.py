import os
import json
import sys
from apiclient.discovery import build

class YoutubeDownloader():
	def __init__(self, credentials_file, out_location):
		f = open(credentials_file)
		data = json.load(f)
		self.apikey = data['apikey']
		self.out_location = out_location
		self.api_service_name = 'youtube'
		self.api_version = 'v3'


	def download_song(self,query):
		youtube = build(self.api_service_name, self.api_version, developerKey = self.apikey)
		request = youtube.search().list(q=query,part='snippet')
		response = request.execute()
		if(len(response['items']) > 0 and response['items'][0]['id']['kind'] == "youtube#video"):
			print('Downloading {0} at {1}'.format(query, self.out_location))
			os.system("youtube-dl --extract-audio --audio-format mp3 -o '" + self.out_location+ "/%(title)s.%(ext)s' https://www.youtube.com/watch?v=" + response['items'][0]['id']['videoId'])
		else:
			print('Query failed for {0}'.format(query))

if __name__ == "__main__":
	if(len(sys.argv) != 4):
		print('Improper arguemnts. Format: python youtube_downloader <credentials_file> <query/input file> <out_location>')
		sys.exit(1)
	if(not os.path.isfile(sys.argv[1])):
		print('Credentials file does not exist. Please check the input argument')
		sys.exit(1)
	if(not os.path.isdir(sys.argv[3])):
		print('Out location directory does not exist. Please create it and rerun')
		sys.exit(1)

	yd = YoutubeDownloader(sys.argv[1],sys.argv[3])
	if(os.path.isfile(sys.argv[2])):
		with open(sys.argv[2]) as fp:
			for cnt, line in enumerate(fp):
				yd.download_song(line)
	else:
		yd.download_song(sys.argv[2])