import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
import re
import nltk

# Download NLTK resources
nltk.download('stopwords')

HF_API_KEY = "enter-your-huggingface-api-key"
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"

def generate_mapping(platform_schema):
    """
    Generates a standardized schema mapping using the Hugging Face API.
    :param platform_schema: Description of the platform-specific schema
    :return: Generated mapping
    """
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": f"Map the following fields to a standardized schema: {platform_schema}"
    }
    response = requests.post(HF_API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Hugging Face API error: {response.text}")
    return response.json()[0]['generated_text']

def preprocess_text(text):
    """
    Preprocesses text by cleaning and normalizing it.
    :param text: Input text
    :return: Cleaned text
    """
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join(word for word in text.split() if word not in stopwords.words('english'))
    return text.strip()


def extract_themes(data, topic, num_clusters=8):
    """
    Extracts broad themes from the data for the given topic.
    :param data: List of dictionaries (JSON objects)
    :param topic: Topic to analyze (e.g., "skin")
    :param num_clusters: Number of clusters (themes) to extract
    :return: List of themes
    """
    relevant_content = []

    # Collect relevant content
    for record in data:
        if record.get("source", "").startswith("amazon"):
            for review in record.get("reviews", []):
                content = review.get("content", "")
                if content and topic in content.lower():
                    relevant_content.append(content)

        elif record.get("source", "").startswith("reddit"):
            for comment in record.get("comments", []):
                body = comment.get("body", "")
                if body and topic in body.lower():
                    relevant_content.append(body)

        elif record.get("source", "").startswith("youtube"):
            for comment in record.get("comments", []):
                text = comment.get("text", "")
                if text and topic in text.lower():
                    relevant_content.append(text)

    if not relevant_content:
        return []

    # Preprocess the text
    relevant_content = [preprocess_text(content) for content in relevant_content if content]

    # Vectorize the text using TF-IDF
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(relevant_content)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    # Generate theme labels
    feature_names = vectorizer.get_feature_names_out()
    themes = []
    for i in range(num_clusters):
        top_words = [feature_names[j] for j in kmeans.cluster_centers_[i].argsort()[:-6:-1]]  # Top 5 words per cluster
        theme_label = " ".join(top_words).capitalize()
        themes.append(theme_label)

    return themes