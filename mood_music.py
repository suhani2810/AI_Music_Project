import cv2
import tensorflow as tf
import keras
tf.keras = keras
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from datetime import datetime
import webbrowser, os, time, threading
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from colorama import Fore, init
import matplotlib.pyplot as plt
import pyttsx3

init(autoreset=True)

#Voice
engine = pyttsx3.init()

def speak_async(text):
    def run_speech():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run_speech, daemon=True).start()

#Spotify
SPOTIPY_CLIENT_ID = "daeb14b53cb84861b1fc2f48808cea01"
SPOTIPY_CLIENT_SECRET = "78fcd9c882dd43469987442a05db034e"
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "playlist-read-private"

#API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

MOOD_EMOJIS = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😡",
    "neutral": "😐",
    "surprise": "😲",
    "fear": "😨",
    "disgust": "🤢"
}

#GUI
cap = cv2.VideoCapture(0)
root = tk.Tk()
root.title("AI Mood-Based Music Player")
root.geometry("700x600")

label = tk.Label(root)
label.pack()

status_label = tk.Label(root, text="Press 'Capture' or select a mood!", font=("Arial", 14))
status_label.pack(pady=10)

# Dropdown
selected_mood = tk.StringVar()
mood_dropdown = ttk.Combobox(root, textvariable=selected_mood, font=("Arial", 12))
mood_dropdown['values'] = list(MOOD_EMOJIS.keys())
mood_dropdown.set("Select Mood (Optional)")
mood_dropdown.pack(pady=10)

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    root.after(10, update_frame)

def open_spotify_playlist(url):
    try:
        print("Opening Spotify playlist...")
        webbrowser.open(url, new=2) 
        time.sleep(1)  
        os.system(f'start {url}')    
    except Exception as e:
        print("Error opening Spotify:", e)

def play_music_for_mood(mood):
    emoji = MOOD_EMOJIS.get(mood, "🎵")
    status_label.config(text=f"Mood: {mood.upper()} {emoji} → Playing on Spotify!", fg="magenta")

    speak_async(f"Your mood is {mood}")

    # Save mood history
    pd.DataFrame([[datetime.now(), mood]], columns=["timestamp", "mood"]).to_csv(
        "mood_history.csv", mode='a', header=False, index=False
    )

    #Spotify playlist
    time.sleep(0.5) 
    results = sp.search(q=mood, type="playlist", limit=5)
    playlists = results['playlists']['items']

    if playlists:
        first_playlist_url = playlists[0]['external_urls']['spotify']
        open_spotify_playlist(first_playlist_url)
    else:
        status_label.config(text=f"No playlists found for {mood}", fg="red")

def detect_mood_and_play():
    if selected_mood.get() in MOOD_EMOJIS:
        play_music_for_mood(selected_mood.get())
        return

    # Capture from webcam
    ret, frame = cap.read()
    img_name = "captured_face.jpg"
    cv2.imwrite(img_name, frame)

    status_label.config(text="Analyzing mood...", fg="blue")
    root.update()

    # Detect mood
    result = DeepFace.analyze(img_path=img_name, actions=['emotion'], enforce_detection=False)
    mood = result[0]['dominant_emotion']

    play_music_for_mood(mood)

def show_mood_history():
    try:
        df = pd.read_csv("mood_history.csv", names=["timestamp", "mood"])
        mood_counts = df["mood"].value_counts()

        plt.figure(figsize=(8,5))
        bars = plt.bar(mood_counts.index, mood_counts.values, color="skyblue")
        plt.title("Mood Detection History", fontsize=16)
        plt.xlabel("Moods")
        plt.ylabel("Frequency")

        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                     str(bar.get_height()), ha='center', va='bottom')

        plt.show()
    except FileNotFoundError:
        status_label.config(text="No mood history yet!", fg="red")

#Buttons
capture_btn = tk.Button(root, text="Capture Mood 🎥", font=("Arial", 14), command=detect_mood_and_play)
capture_btn.pack(pady=10)

history_btn = tk.Button(root, text="Show Mood History 📊", font=("Arial", 14), command=show_mood_history)
history_btn.pack(pady=10)

update_frame()
root.mainloop()

cap.release()
cv2.destroyAllWindows()
