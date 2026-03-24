🎵 AI Mood-Based Music Player
> Detect your mood using AI and automatically play music on Spotify 🎶
> 💡 An intelligent system that bridges human emotions with music using AI.

##📌 Overview

This project is an AI-powered desktop application that detects a user's mood using facial recognition and automatically plays a matching Spotify playlist.
It combines computer vision, deep learning, and music streaming to create an interactive and personalized experience.

##🎬 **Demo Video:**  
[Watch here]([https://drive.google.com/...](https://drive.google.com/file/d/1Quv9Y7HV3oiFpFRAbThO2UhQKg5fnsGu/view?usp=sharing))


##🖼️ Preview
![App Screenshot](https://github.com/user-attachments/assets/bda99070-429e-44e0-aab1-cf3c13ed7243)
> Real-time mood detection using webcam and Spotify integration 🎥🎶

##🚀 Features

- 🎥 Real-time face capture using webcam
- 😊 Mood detection using DeepFace (AI model)
- 🎶 Automatic Spotify playlist recommendation
- 🔊 Voice feedback using text-to-speech
- 📊 Mood history tracking with visualization
- 🖥️ Interactive GUI built with Tkinter
- 🎛️ Manual mood selection option
- 
## 🛠️ Tech Stack

- Python
- OpenCV (Computer Vision)
- TensorFlow / Keras
- DeepFace (Emotion Detection)
- Spotipy (Spotify API)
- Tkinter (GUI)
- Pandas (Data Handling)
- Matplotlib (Visualization)
- pyttsx3 (Text-to-Speech)

## 📂 Project Structure

AI_Music_Project/
│── mood_music.py
│── mood_history.csv
│── captured_face.jpg
│── Project Demo.mp4

##⚙️ Setup Instructions

1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AI_Music_Project.git
cd AI_Music_Project
2️⃣ Install dependencies
pip install opencv-python tensorflow keras deepface spotipy pandas matplotlib pillow pyttsx3 colorama
3️⃣ Set up Spotify API
Go to Spotify Developer Dashboard
Create an app
Replace these in the code:
SPOTIPY_CLIENT_ID = "your_client_id"
SPOTIPY_CLIENT_SECRET = "your_client_secret"
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8888/callback"
4️⃣ Run the application
python mood_music.py

##🧠 How It Works

Webcam captures user's face
DeepFace analyzes facial expression
Dominant emotion is detected (happy, sad, etc.)
Spotify API searches for playlists based on mood
Playlist opens automatically in browser
Mood is stored for future analysis

##📊 Mood History Visualization

Stores moods in mood_history.csv
Displays a bar chart showing mood frequency

##🔊 Voice Feedback

Uses pyttsx3 to announce detected mood

##⚠️ Important Notes

Requires a working webcam
Internet connection needed for Spotify
Spotify login may be required on first run

##🚧 Future Improvements

🎨 Better UI design
🎵 Direct Spotify playback integration
🤖 Improved emotion accuracy
📱 Mobile or web version

##🛠️ Troubleshooting

❌ Error: TensorFlow / Keras Compatibility Issue
ValueError: You have tensorflow 2.21.0 and this requires tf-keras package.
Please run pip install tf-keras or downgrade your tensorflow.
💡 Cause
This happens because newer versions of TensorFlow (2.21+) are not fully compatible with some dependencies used by DeepFace (like RetinaFace).

✅ Solution 1 (Recommended)
Install the required compatibility package:

```bash
pip install tf-keras
✅ Solution 2 (Alternative)

Downgrade TensorFlow to a compatible version:

pip install tensorflow==2.12 keras==2.12

👉 If this happens again, use:
```bash
pip install tensorflow==2.12 --index-url https://pypi.org/simple

##⚠️ Tip

Always use a virtual environment to avoid dependency conflicts:

python -m venv venv
venv\Scripts\activate
❌ Error: Webcam not opening
Make sure no other app is using the camera
Check camera permissions
❌ Error: Spotify not opening
Ensure internet connection is active
Login to Spotify in your browser
Check API credentials
❌ Error: No face detected
Ensure proper lighting
Face should be clearly visible to webcam

OR use Python 3.10 (best compatibility)

##💡 Pro tip

If errors keep coming one by one, fastest way:
pip install -r requirements.txt

## 👩‍💻 Author
 
**Suhani Mahajan**  
[![GitHub](https://github.com/suhani2810)  
[![LinkedIn](https://www.linkedin.com/in/suhani-mahajan-2431b8328/)

⭐ If you like this project

Give it a star on GitHub ⭐
