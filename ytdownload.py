from yt_dlp import YoutubeDL

class ProgressLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

# Hook the Youtube_DL's download progress to output messages
def ProgressHook(d):
    if d['status'] == 'finished':
        print(f'Post-processing "{d['info_dict']['title']}"...')

# Ask the user to input URL's to download from
def AskUser():
    uri = input("Enter Youtube Urls (separate with spaces): ")
    user_option = input("Download as Video(1) or Audio(2): ")
    confirm = input("\nConfirm options(Y/n): ")

    uri_list = uri.split(" ")

    if (confirm.lower() != "y"):
        print("Please enter the options you want")
        return

    ytdl_opts = {
        'logger': ProgressLogger(),
        'progress_hooks': [ProgressHook],
    }

    if (user_option.lower() == "2"):
        ytdl_opts = {
            'logger': ProgressLogger(),
            'progress_hooks': [ProgressHook],
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }

    print("Attempting to download...")
    try:
        with YoutubeDL(ytdl_opts) as ytdl:
            ytdl.download(uri_list)

        print("Finished!")
    except Exception as e:
        print(f"Failed to download: {e}")

    do_exit = input("Do you want to exit? (Y/n): ")
    if (do_exit.lower() == "y"):
        exit()
    else:
        print("\n")

print("<--- ytdownload.py YouTube Downloader --->")
print("<--- https://github.com/TheXJ-Github ---->")

while (True):
    AskUser()
