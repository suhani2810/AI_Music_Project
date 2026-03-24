🎵 AI Mood-Based Music Player
📌 Overview
This project is an AI-powered desktop application that detects a user's mood using facial recognition and automatically plays a matching Spotify playlist.
It combines computer vision, deep learning, and music streaming to create an interactive and personalized experience.

🚀 Features
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

📂 Project Structure

AI_Music_Project/
│── mood_music.py # Main application
│── mood_history.csv # Stores mood logs
│── captured_face.jpg # Captured image
│── Project Demo.mp4 # Demo video (optional)

⚙️ Setup Instructions

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

🧠 How It Works
Webcam captures user's face
DeepFace analyzes facial expression
Dominant emotion is detected (happy, sad, etc.)
Spotify API searches for playlists based on mood
Playlist opens automatically in browser
Mood is stored for future analysis

📊 Mood History Visualization
Stores moods in mood_history.csv
Displays a bar chart showing mood frequency

🔊 Voice Feedback
Uses pyttsx3 to announce detected mood

⚠️ Important Notes
Requires a working webcam
Internet connection needed for Spotify
Spotify login may be required on first run

🚧 Future Improvements
🎨 Better UI design
🎵 Direct Spotify playback integration
🤖 Improved emotion accuracy
📱 Mobile or web version

👩‍💻 Author
Suhani

⭐ If you like this project

Give it a star on GitHub ⭐
