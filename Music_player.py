import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Function to browse and add music to the playlist
def add_music():
    file_paths = filedialog.askopenfilenames(title="Choose Music", filetypes=[("MP3 files", "*.mp3")])
    for file_path in file_paths:
        if file_path.lower().endswith('.mp3'):
            playlist.insert(END, file_path)

# Function to play the selected music
def play_music():
    selected_music = playlist.get(ACTIVE)
    if selected_music:
        mixer.music.load(selected_music)
        mixer.music.play()

# Function to stop the music
def stop_music():
    mixer.music.stop()

# Function to pause/unpause the music
def pause_unpause_music():
    if mixer.music.get_busy():
        if mixer.music.get_pos() > 0:  # Check if music is playing
            if mixer.music.get_pos() < 10:  # A small delay to avoid toggling too fast
                if mixer.music.get_pause() == 0:
                    mixer.music.pause()
                else:
                    mixer.music.unpause()

# Create the main window
root = Tk()
root.title("Music Player")
root.geometry("400x300")

# Initialize the mixer
mixer.init()

# Create the playlist
playlist = Listbox(root, bg="lightgray", selectbackground="orange", selectmode=SINGLE)
playlist.pack(fill=BOTH, expand=True)

# Create buttons
Button(root, text="Add Music", command=add_music).pack(pady=10)
Button(root, text="Play", command=play_music).pack(pady=10)
Button(root, text="Stop", command=stop_music).pack(pady=10)
Button(root, text="Pause/Unpause", command=pause_unpause_music).pack(pady=10)

# Run the main loop
root.mainloop()
