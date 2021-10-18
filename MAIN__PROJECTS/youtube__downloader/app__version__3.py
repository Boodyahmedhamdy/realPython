from pytube import YouTube, Playlist  # THE MAIN MODULE
from colorama import Fore, init  # COLORING TEXT IN PYTHON CONSOLE
from win10toast import ToastNotifier  # FOR MAKING NOTIFICATIONS
import os  # FOR MAKING DIRECTORIES IN PLAYLIST DOWNLOAD
from tqdm import tqdm  # TO MAKE A PROGRESS BAR IN PLAYLIST DOWNLOAD
from typing import Any  # for type hinting
import time  # for dealing with time
# from shutil import rmtree  # TO REMOVE NONE EMPTY FOLDER

# MAIN INFORMATION
# --------------------
# NAME OF THE PROJECT
projectName = 'python downloader'
# MAIN PATH OF THE PROGRAM
mainPath = os.getcwd()
# DOWNLOADS PATH
mainDownloadPath = mainPath + '/' + "downloads"

# ALL FUNCTIONS IN THE PROGRAM
# -----------------------------
# notifications functions


def start_downloading_notification(paragraph, heading=projectName):

    """
    :param paragraph: words in the message box 'notification'
    :param heading: default  the name of the project
    :return: have no return but produce a notification using
             ToastNotifier() form win10toast
    """

    box = ToastNotifier()
    box.show_toast(heading, paragraph, icon_path="images__and__icons/down-arrow.ico")


def finish_downloading_notification(paragraph, heading=projectName):

    """
    :param paragraph: words in the message box 'notification'
    :param heading: default  the name of the project
    :return: have no return but produce a notification using
             ToastNotifier() form win10toast
    """

    box = ToastNotifier()
    box.show_toast(heading, paragraph, icon_path="images__and__icons/checked.ico")


def error_notification(paragraph, heading=projectName):
    """
    :param paragraph: words in the message box 'notification'
    :param heading: default  the name of the project
    :return: have no return but produce a notification using
             ToastNotifier() form win10toast
    """

    box = ToastNotifier()
    box.show_toast(heading, paragraph, icon_path="images__and__icons/warning.ico")


# FOR COLORAMA AUTO RESET
init(autoreset=True)


# coloring functions

def mk_green(thing: Any) -> str:

    """
    :param thing: any text
    :return: thing in the color of the function
            USING COLORAMA MODULE
    """
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'


def mk_red(thing: Any) -> str:

    """
    :param thing: any text
    :return: thing in the color of the function
            USING COLORAMA MODULE
    """
    return f'{Fore.RED + str(thing) + Fore.RESET}'


def mk_blue(thing: Any) -> str:

    """
    :param thing: any text
    :return: thing in the color of the function
            USING COLORAMA MODULE
    """
    return f'{Fore.BLUE + str(thing) + Fore.RESET}'


# downloading functions
# =========================
# PLAY LIST DOWNLOAD
def download_playlist() -> None:

    """
    :param: takes no parameters
    called by the main function
        it detectes if you want to download the play list as audio or video

        NOTE: if you choosed audio this will download all the play list as audio
        the same thing with video

        FEATURES: have a progress bar
        USING PYTUBE MODULE .. PLAYLIST
    :return:
    """
    # FIRST .. TAKE THE LINK
    linkOfPlaylist = input("enter url of the playlist : ")

    # CREATE A PLAYLIST OBJECT
    playlist = Playlist(linkOfPlaylist)

    # ONCE PLAYLIST IS CREATED THOSE INFORMATION SHOULD COME TO LIFE
    # ---------------------------------------------------------------
    # PLAYLIST NAME THAT WE ARE GOING TO DEAL WITH INSIDE THIS FUNCTION
    playlistName = playlist.title

    # NUMBER OF VIDEOS --> IF NEEDED TO IT
    numberOfObjects = playlist.length

    # DEALING WITH PATH OF DOWNLOAD AND MAIN PATH
    mainPath = os.getcwd()
    mainDownloadPath = mainPath + '/' + "downloads"

    # THE CHOICE BETWEEN PLAYLIST OF SONGS OR VIDEOS
    audioOrVideo = input("do you like to download it a audios or videos (a/v): ").lower()

    # IN CASE OF AUDIO
    if audioOrVideo == 'a':

        # if user will download audio then save it in audio folder
        # ONCE YOU CHOOSE AUDIO .. LET THE DOWNLOAD PATH INSIDE AUDIO
        mainDownloadPath = mainDownloadPath + '/' + "audio" + '/' + playlistName

        # MAKE FOLDER TO SAVE THE PLAYLIST INSIDE IT
        os.makedirs(mainDownloadPath)
        print(mk_green('folder created successfully 😊'))

        # DOWNLOADING NOTIFICATION
        print(mk_green(f'start downloading {mk_blue(numberOfObjects)} audios'))
        start_downloading_notification(f"start downloading {playlistName}")

        # time for whole playlist
        allStartTime = time.time()

        # DOWNLOADING PROCESS
        for audio in tqdm(playlist.videos, desc=f'downloading {mk_blue(playlistName)}'):
            singleStartTime = time.time()
            finalAudio = audio.streams.filter(only_audio=True).first().download(output_path=mainDownloadPath)
            convert_to_mp3(finalAudio)
            singleDownloadingTime = time.time() - singleStartTime

            print(f"downloaded {audio.title} in {singleDownloadingTime / 60} minutes")

        # time for the whole playlist
        allDownloadingTime = time.time() - allStartTime

        # finishing notification
        finish_downloading_notification(f'download has finished in {allDownloadingTime / 60} minutes .. thank you')

    elif audioOrVideo == "v":
        mainDownloadPath = mainDownloadPath + '/' + "video" + '/' + playlistName

        # for n, video in enumerate(playlist.videos):
        #     print(n+1, '-', mk_blue(video.title))

        # MAKE FOLDER TO SAVE THE PLAYLIST INSIDE IT
        os.makedirs(mainDownloadPath)
        print(mk_green('folder created successfully 😊'))

        # DOWNLOADING NOTIFICATION
        print(mk_green(f'start downloading {mk_blue(numberOfObjects)} videos'))
        start_downloading_notification(f"start downloading {playlistName}")

        # to calculate time for the whole playlist
        allStartTime = time.time()

        for video in tqdm(playlist.videos):
            singleStartTime = time.time()
            video.streams.get_highest_resolution().download(output_path=mainDownloadPath)
            singleDownloadingTime = time.time() - singleStartTime

            print(f"downloaded {video.title} in {singleDownloadingTime / 60} minutes")

        # time for the play list
        allDownloadingTime = time.time() - allStartTime

        finish_downloading_notification(f'download has finished in {allDownloadingTime /60} minutes .. thank you')

    else:
        print(mk_red('invalid input .. please enter a or v next time'))
        error_notification('invalid input')

# SINGLE VIDEO DOWNLOAD
def download_single_video() -> None:

    """
    takes no parameters
    called by the main function
    detect audio or video and start downloading it in the highest available resolution

    :return: nothing but it downloads the object that you choose from the main function

    USING PYTUBE MODULE .. YOUTUBE
    """

    # taking the link from the user
    link = input('please enter link of the video : ')

    # create an object to deal with the video
    video = YouTube(link)

    # let user choose whether he wants to download it ad mp3 or mp4
    audioOrVideo = input('do you want to download audio or video (a/v) : ')

    # in case of audio
    if audioOrVideo == 'a':
        # setting download path
        mainDownloadPath = mainPath + '/' + "downloads"

        mainDownloadPath = mainDownloadPath + '/' + 'audio'

        # start downloading notification
        print(f'start downloading {mk_green(video.title)}')
        start_downloading_notification("downloading has started")

        # downloading process
        singleStartTime = time.time()

        finalAudio = video.streams.filter(only_audio=True).first().download(output_path=mainDownloadPath)
        # converting the .mp4 to .mp3 to be used as audio
        convert_to_mp3(finalAudio)

        singleDownloadingTime = time.time() - singleStartTime

        print(f"{video.title} downloaded in {singleDownloadingTime/ 60} minutes")

        # finishing notification
        finish_downloading_notification(f'downloading has finished in {singleDownloadingTime/60} minutes .. thank you')

    # in case of video
    elif audioOrVideo == 'v':
        # setting downloading path
        mainDownloadPath = mainPath + '/' + "downloads"

        mainDownloadPath = mainDownloadPath + '/' + 'video'

        # start downloading notification
        print(f'start downloading {mk_green(video.title)}')
        start_downloading_notification("downloading has started")

        singleStratTime = time.time()

        # ONLY HIGHEST RESOLUTION WILL BE DOWNLOADED
        video.streams.get_highest_resolution().download(output_path=mainDownloadPath)

        singleDownloadingTime = time.time() - singleStratTime

        print(f"{video.title} downloaded in {singleDownloadingTime /60} minutes")

        # finishing download notification
        finish_downloading_notification('downloading has finished .. thank you')

    # in case of wrong input
    else:
        print(mk_red('invaled input'))
        error_notification('invaled input')


# FOR THE .MP3 FILES
def convert_to_mp3(audio) -> None:
    """
    :JOB: converts .mp4 file exetention to .mp3 exetention
    :WHY: to be used as a mp3 file .. set as ringtone for example
    :param audio: the audio object after downloading in using one of breaviouse functions
    :return: nothing

    """
    base, ext = os.path.splitext(audio)
    new_file = base + '.mp3'
    os.rename(audio, new_file)


# start the main program
# -----------------------
def mainFunc() -> None:

    """
    :JOB: the main function for the program and call the other functions on need
    :return: nothing
    """
    # CHOOSE THE WAY WHETHER PLAYLIST OR A SINGLE VIDEO
    videoOrPlaylist = input('do you like to download playlist or single video (v/p) : ')

    if videoOrPlaylist == 'v':
        download_single_video()

    elif videoOrPlaylist == 'p':
        download_playlist()

    else:
        print(mk_blue("please enter A for audio or V for video"))
        error_notification("please enter p or v")


anotherDownload = 'y'
print("wellcome to py downloader 😍")
while anotherDownload == "y":
    mainFunc()
    anotherDownload = input("do you want to do another download (y/n) : ").lower()
    print("-----------------")

