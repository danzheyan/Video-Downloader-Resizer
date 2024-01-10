import tkinter
import customtkinter
from pytube import YouTube

# Download
def start_download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finish_download.configure(text="")

        video.download(output_path="VideoCollect")
        finish_download.configure(text="Downloaded!", text_color="green")
    except:
        finish_download.configure(text="Youtube link is invalid", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_done = bytes_downloaded / total_size * 100
    per = str(int(percent_done))
    percentage.configure(text=f"{per}%")
    bar.set(float(percent_done) / 100)

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# app frame 
app = customtkinter.CTk()
app.geometry("720x360")
app.title("Youtube Downloader")

# UI 
title = customtkinter.CTkLabel(app, text="Enter a YouTube link")
title.pack(padx=10, pady=10)

# Input link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, corner_radius=10, textvariable=url_var)
link.pack()

# Download button 
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(pady=20)

# Progress %
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

# Progress bar
bar =  customtkinter.CTkProgressBar(app, width=400)
bar.set(0)
bar.pack(pady=40)

# Finished Download
finish_download = customtkinter.CTkLabel(app, text="")
finish_download.pack()

# Run app
app.mainloop()