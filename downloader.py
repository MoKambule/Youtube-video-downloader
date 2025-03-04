from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import pytube.request

pytube.request.default_headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

# Define progress callback function
def progress_func(stream,chunk, bytes_remaining):
    total_size = stream.filesize  #gets the total fiesize in btes of the current stream
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print(f"Download progress: {percent:.2f}%")  #.2f - shows percent in 2 decimal point

# Define complete callback function
def complete_func(stream, file_path):
    print(f"Download complete: {file_path}")

def downdload_video():
   
    try:
        yt = YouTube(
        'https://www.youtube.com/watch?v=WOxm19URvtA',
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        # proxies=my_proxies,
        use_oauth=False,
        allow_oauth_cache=True 
        )

        youtube= yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        youtube.download()

    except Exception as e:
        print(f"Error downdloading video: {e}")  

    print("Download complete....")    

if __name__=="__main__":
    downdload_video()




    