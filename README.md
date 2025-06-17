# 🎬 Movie Recommender System

A content-based movie recommender system built with **Python**, **Streamlit**, and **The Movie Database (TMDB) API**. Instantly get similar movie suggestions with high-quality posters and a modern UI.

---

## 🔗 Live Demo

🟢 Hosted at: [https://6830-2001-4858-aaaa-77-167-2f4c-64a-e012.ngrok-free.app](https://6830-2001-4858-aaaa-77-167-2f4c-64a-e012.ngrok-free.app)

---

## 🖼️ Preview

![App Screenshot](https://raw.githubusercontent.com/atul2501/Movie_Recommender_System/main/Screenshot.png)

---

## 🚀 Features

- 🔎 Select any movie from the dropdown
- 🤖 Get top 5 similar movie recommendations
- 🖼 Display of dynamic movie posters from TMDB
- 🧪 Works with `.pkl` similarity matrix
- 🎨 Clean UI built using Streamlit

---

## 🧠 How It Works

This app uses **content-based filtering** on movie metadata (genres, cast, crew, keywords) and a precomputed similarity matrix to suggest related titles. Movie posters are fetched in real-time from TMDB using their API.

---

## 📦 Project Structure

```

movie-recommender-system/
│
├── app.py                 # Main Streamlit app
├── movies\_dict.pkl        # Pickled movie metadata
├── similarity.pkl         # Pickled similarity matrix (excluded from GitHub)
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku deployment file
├── setup.sh               # Streamlit config setup
├── README.md              # You're reading it 🙂

````

---

## 🛠️ Installation

### ✅ Run Locally

1. Clone the repo:
```bash
git clone https://github.com/atul2501/Movie_Recommender_System.git
cd Movie_Recommender_System
````

2. Set up a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 🌐 Make It Public (ngrok)

1. [Download ngrok](https://ngrok.com/download)
2. Run:

```bash
ngrok http 8501
```

Share the generated public link!

---

## ☁️ Deploy on Heroku

1. Install Heroku CLI
2. Create an app:

```bash
heroku create movie-recommender-app
```

3. Push to Heroku:

```bash
git push heroku main
```

Heroku will use `Procfile` and `setup.sh` to launch the app.

---

## 📸 Screenshot

> Replace with your GitHub-hosted image (or use the one already uploaded):

![Preview](Screenshot.png)

---

## 👤 Author

* **Name:** Atul Yadav
* **GitHub:** [atul2501](https://github.com/atul2501)

---

## 📄 License

Licensed under the [MIT License](LICENSE)

---

## 🙌 Support

If you found this useful, give a ⭐ on GitHub and share the link!

````

---

### 📌 Final Step

To make the screenshot appear correctly on GitHub:

1. Rename your uploaded screenshot file to `Screenshot.png`
2. Place it in the **root** of your repo
3. Commit and push:
```bash
git add Screenshot.png
git commit -m "Add app screenshot"
git push
````
