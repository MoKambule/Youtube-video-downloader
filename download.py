import yt_dlp
import sys
import argparse
import requests

def arg_parser():

    parser = argparse.ArgumentParser(description="youtube downloader in mp4")
    parser.add_argument('--output', default='%(title)s.%(ext)s', help=" file name the video is downloaded to")

    return parser.parse_args()

def validate_url(url):
    '''check if the given url by the user is accessible and valid'''   
    try:
        request = requests.get(url, timeout=5)
        if request.status_code==200:
            return True
        else:
            print("Error finding url")
            return False
    except requests.exceptions.RequestException:
        print("Error: the ule given is invalid / does not exit")        

def list_video_formats(url):
    '''list all the available formats'''
    yt_opts = {'listformats': True,} 
    try: 
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"error:{e}") 
        sys.exit(1)     

def video_downloader():
    args = arg_parser()

    url =input("enter url: ")
    if not validate_url(url):
        sys.exit(1) 
     
    list_video_formats(url)
    format_code = input("enter format you want the video to be downloaded in (audio+vide0): (eg 233+136)  ")    
    yt = {'outtmpl':args.output , 'format': format_code,}  #bestvideo+bestaudio/ isto ensure the best quality
   
    try:
        print(f"Downloading video in format: {format_code}....")
        with yt_dlp.YoutubeDL(yt) as ydl:
            ydl.download([url])
        print("Downoad completed successfully!")    
    except Exception as e:
        print(f"error:{e}") 
        sys.exit(1)    

# def downloads_table(url):
#     download_id = {'video_url':url,
#                    }


if __name__=='__main__':
  
    video_downloader()        