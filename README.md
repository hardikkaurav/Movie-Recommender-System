# Movie-Recommender-System

Here’s a clean and complete `README.md` you can use for your GitHub repository of this **Movie Recommender System using Streamlit and TMDB API**.

---

## 📽️ Movie Recommender System

This is a content-based Movie Recommender System built using **Streamlit**, which suggests 5 similar movies to the selected title and fetches posters from the **TMDB API**.



## 📦 Features

✅ Recommend 5 similar movies
✅ Display posters using **TMDB API**
✅ Clean UI built with **Streamlit**
✅ Poster fallback if not available

---

## 📁 Project Structure

```
├── main.py               # Streamlit app code
├── movie_dict.pkl        # Movie data dictionary
├── similarity.pkl        # Precomputed similarity matrix
├── requirements.txt      # Required Python libraries
└── README.md             # Project info
```

---

## 🛠️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```


### 4. Run the app

```bash
streamlit run main.py
```

---

## 🔑 TMDB API Key

This project uses TMDB’s public API to fetch movie posters.

You can get your own API key at: [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

Replace the API key in the `fetch_poster()` function inside `main.py`:

```python
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
```

---

## 🧠 Model Behind

The recommendations are powered by **cosine similarity** between TF-IDF vectors or embeddings (stored in `similarity.pkl`), and the movie metadata from `movie_dict.pkl`.

---

## 📚 Requirements

Here is a sample `requirements.txt`:

```txt
streamlit
pandas
scikit-learn
requests
```

You can generate your own using:

```bash
pip freeze > requirements.txt
```

---

## 📸 Optional: Git LFS for `.pkl` files

If your `movie_dict.pkl` or `similarity.pkl` files are large, use **Git LFS**:

```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git add movie_dict.pkl similarity.pkl
git commit -m "Track large files with Git LFS"
```

---

## 🌐 Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Deploy!

---
