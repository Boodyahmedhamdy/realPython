from pytube import YouTube
# from pytube.cli import on_progress
from colorama import Fore, init
from win10toast import ToastNotifier
import os

# NAME OF THE PROJECT
projectName = 'python downloader'

# ALL FUNCTIONS IN THE PROGRAM
# -----------------------------
# # PROGRESS FUNCTION
#
# def progress_function(self, stream, chunk, file_handle, bytes_remainig):
#     size = stream.filesize
#     p = 0
#     while p <= 100:
#         progress = p
#         print(str(p), '%')
#         p = percent(bytes_remainig, size)
#
#
# def percent(self, tem, total):
#     perc = (float(tem) / float(total) * float(100))
#     return perc

# notifications functions

def start_downloading_notification(paragraph, heading = projectName):
    box = ToastNotifier()
    box.show_toast(heading, paragraph, icon_path="down-arrow.ico")


def finish_downloading_notification(paragraph, heading=projectName):
    box = ToastNotifier()
    box.show_toast(heading, paragraph, icon_path="checked.ico")


def error_notification(paragraph, heading=projectName):
    box = ToastNotifier()
    box.show_toast(heading, paragraph, icon_path="warning.ico")


# FOR COLORAMA AUTO RESET
init(autoreset=True)


# coloring functions

def mk_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'


def mk_red(thing):
    return f'{Fore.RED + str(thing) + Fore.RESET}'


def mk_blue(thing):
    return f'{Fore.BLUE + str(thing) + Fore.RESET}'


# start the main program
# -----------------------
def mainFunc():

    # CHOOSE YOUR WAY
    audioOrVideo = input("do you want to download audio only or video (A/V): ").strip().upper()

    # IN CASE OF VIDEO
    if audioOrVideo == "V":

        # TAKE THE LINK
        link = input("enter video link you want to download : ")

        video = YouTube(link)

        print(mk_blue("NOTE: this will download highest available resolution for this video"))

        # DOWNLOAD THE HIGHEST RESOLUTION -->> 720P
        finalVideo = video.streams.get_highest_resolution()

        print(mk_green("start downloading "), video.title)

        # NOTIFY USER BY START DOWNLOADING AND FINISHING
        start_downloading_notification(f'start downloading {video.title} in {os.getcwd()}')
        finalVideo.download()
        finish_downloading_notification(f'download has finished successfully')

        # ITS DONE WITH VIDEO

    # IN CASE OF AUDIO
    elif audioOrVideo == "A":
        # TAKE LINK OF THE VIDEO
        link = input("enter link of video to download its audio : ")

        audios = YouTube(link)

        # CHOOSE AUTOMATICALLY FIRST AUDIO IN STREAMS
        finalAudio = audios.streams.filter(only_audio=True).first()
        # print(finalAudio)

        # NOTIFY USER BY START DOWNLOADING
        print(mk_blue('NOTE : downloading audio file'))
        start_downloading_notification(f'start downloading {finalAudio.title}')

        # DOWNLOAD AND ASSIGN THE FINAL VALUE TO ANOTHER VARIABLE TO CONVERT THE TYPE LATER
        outFile = finalAudio.download()

        # CONVERT THE TYPE FROM MP4 TO MP3
        base, ext = os.path.splitext(outFile)  # THIS WILL SPLIT THE FINAL NAME TO 2 PARTS
        new_file = base + '.mp3'  # CHANG EXETENTION TO MP3
        os.rename(outFile, new_file)  # RENAME THE FINAL FILE

        # NOTIFY USER TO END DOWNLOADING
        finish_downloading_notification("downloading has finished")

    # IF USER MADE A MISTAKE
    else:
        print(mk_blue("please enter A for audio or V for video"))
        error_notification("please enter A or V")


anotherDownload = 'y'
while anotherDownload == "y" or anotherDownload == 'Y':
    mainFunc()
    anotherDownload = input("do you want to do another download : ")
    print("-----------------")

