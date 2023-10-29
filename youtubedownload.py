from pytube import YouTube
import moviepy.editor as mp 

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  youtubeObject.download()
 
def Download_audio(link):
    print(link)
    youtubeObject = YouTube(link)
    print('baixando....')
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    titulo = youtubeObject.title.title()
    print(titulo)

    youtubeObject.download()
    clip = mp.VideoFileClip(titulo+".mp4") 
    clip.audio.write_audiofile(titulo+".mp3")
link = input("Coloque o link aqui: ")
try:
  Download_audio(link)
  print("Download completo")
except:
  print('Erro no download')