# 🤖 Solo AI – Voice Controlled Python Assistant

**Solo** is a personal voice-activated assistant built with Python.  
It can open websites, play songs from a pre-defined YouTube playlist, and read out the top 5 BBC news headlines – all triggered by your voice.

This lightweight project is perfect for beginners who want to explore Python's speech recognition, web automation, and API handling capabilities.

---

## 🔧 Features

🎤 **Voice Activation with Wake Word**  
- Wake word: `solo`  
- Uses Google Speech Recognition API for capturing voice commands

🌐 **Smart Web Navigation**  
- Opens websites like Google, YouTube, Facebook, Instagram, GitHub, and LinkedIn

🎵 **Music Playlist Integration**  
- Play songs using commands like: `play lofi`  
- YouTube links are stored in `playlist.py` as a dictionary

🗞️ **Live News Updates**  
- Fetches top 5 headlines from **BBC News** using NewsAPI  
- Reads news aloud using text-to-speech

🗣️ **Text-to-Speech Output**  
- Built-in voice responses using `pyttsx3`

---

## 📁 Project Structure

```
mega-project/
├── main.py         # Core voice assistant logic
├── playlist.py     # Music dictionary (YouTube links)
└── README.md       # Project documentation
```

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install speechrecognition
pip install pyttsx3
pip install requests
pip install pyaudio   # Might require additional setup
```

🔧 **Note for Windows users:**  
If `pyaudio` gives an error, use:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 API Key

The assistant uses **NewsAPI** to fetch news. You’ll need a free API key from:  
👉 https://newsapi.org/

Paste your API key inside `main.py` like this:

```python
newsapi = "YOUR_API_KEY_HERE"
```

---

## ▶️ How to Run

```bash
python main.py
```

Once running:

- Say **“solo”** to activate the assistant
- Then give a voice command like:
  - `open google`
  - `open facebook`
  - `play lofi`
  - `news`

---

## 🧠 Customize Your Playlist

Open `playlist.py` and update your music like this:

```python
music = {
    "lofi": "https://www.youtube.com/watch?v=abcd1234",
    "sad": "https://www.youtube.com/watch?v=efgh5678",
    "happy": "https://www.youtube.com/watch?v=ijkl9012"
}
```

---

## 📌 Example Commands

| Command        | Action                         |
|----------------|--------------------------------|
| `solo`         | Wake the assistant             |
| `open google`  | Opens Google in browser        |
| `play lofi`    | Plays the "lofi" YouTube song  |
| `news`         | Reads top 5 BBC headlines      |

---

## 🚀 Future Scope

- Add weather updates  
- Integrate with Spotify or WhatsApp  
- Add desktop notifications  
- GUI using `Tkinter` or `PyQt`

---

## 📜 License

This project is open-source and free to use.

---

## 🙋‍♂️ Author

**Himanshu Sen**  
🔗 [GitHub Profile](https://github.com/Himanshusen273)
