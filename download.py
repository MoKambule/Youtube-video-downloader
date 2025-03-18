import yt_dlp
import sys
import argparse
import requests
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


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

def list_video_formats():
    '''list all the available formats'''
    placeholder_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    yt_opts = {'quiet':True,
               'listformats': True,
               'force_generic_extractor': False,} 
    try: 
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.extract_info(placeholder_url, download=False)
    except Exception as e:
        print(f"error:{e}") 
        sys.exit(1)     

def video_downloader():
    args = arg_parser()

    url =url_entry.get()
    if not validate_url(url):
        messagebox.showerror("error, please enter valid url")
        return
     
    format_code = format_entry.get()
    save_path = "C:\\Users\\Mokgethwa\\Downloads"

    yt = {'outtmpl': (f'{save_path}/{args.output}') ,
           'format': format_code,
             'merge_output_format': 'mp4', }  #bestvideo+bestaudio/ is to ensure the best quality
   
    try:
        print(f"Downloading video in format: {format_code}....")
        with yt_dlp.YoutubeDL(yt) as ydl:
            ydl.download([url])
            print("Download completed successfully!")
            messagebox.showinfo("Success", f"Downloaded: {yt.title}")
        print("Downoad completed successfully!")    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download{str(e)}")
        status_label.config(text="Download failed!", fg="red")
        print(f"Error: {e}")



root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")

# Input field
url_label = ttk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text= "Format code (eg 233+136):").pack(pady=10)
format_entry = ttk.Entry(root,width=50)
format_entry.pack(pady=5)

# Download button
download_button = ttk.Button(root, text="Download", command=video_downloader)
download_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

#theme for Combobox
style = ttk.Style()
style.configure("TCombobox", 
                padding=5, 
                relief="flat", 
                background="lightblue", 
                fieldbackground="lightyellow",  
                foreground="blue")

style.map("TCombobox" ,
           fieldbackground= [("!disabled", "lightgreen")],
           foreground = [("focus", "LightSteelBlue"),
                          ("!disabled", "MediumPurple")]
       
 
 )
style.theme_use('clam') 
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"], style = "TCombobox")
combobox.pack(pady=20)

if __name__=='__main__':
    
    list_video_formats()
    video_downloader()  
    # Run the GUI
    root.mainloop()      