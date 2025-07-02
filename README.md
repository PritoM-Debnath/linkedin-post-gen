# 🤖 LinkedIn Post Generator

Generate personalized topic-specific LinkedIn posts using a few-shot learning approach and LLMs (like LLaMA 3.3) via Groq API. This Streamlit-based app allows you to select a topic, language, and desired length and generates a professional post with examples from your previous posts' data.

---

## 🚀 Features

- **Streamlit UI**: Intuitive interface for post generation.
- **Few-Shot Prompting**: Dynamically curates writing examples to guide the LLM.
- **Tag Normalization**: Unifies similar tags using LLM-powered mapping.
- **Multilingual Support**: Generates posts in English or Bangla.
- **LLM-backed Metadata Extraction**: Automatically determines post language, tags, and length.
- **Fully Modular Codebase**: Easy to extend and integrate.
- **Personalized data**: Uses previous posts as examples, therefore matching the writing style.

---

## 📂 Project Structure

```
├── data                  # Folder for storing personalized and processed post as JSON format
├── main.py               # Streamlit web app
├── few_shot.py           # Loads filtered examples based on tag/length/language
├── llm_helper.py         # Handles Groq LLM configuration
├── post_generation.py    # Prompt building and post generation logic
├── preprocess.py         # Metadata extraction and tag normalization using LLM
└── requirements.txt      # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/PritoM-Debnath/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Create Environment

Using Conda:

```bash
conda create -n linkedin-gen python=3.10
conda activate linkedin-gen
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the App

```bash
streamlit run main.py
```

---

## 📊 Example Use Cases

- If you share insights, this tool might be helpful
- HR creating personalized post
- Coaches posting motivational content
- Thought leaders posting in Bangla or English

---

## 🧠 How it Works

- **Preprocessing**: Raw posts are parsed and tagged using an LLM.
- **Few-Shot Sampling**: Relevant examples are selected to guide output style.
- **Prompt Engineering**: Posts are generated using length, language, and topic.
- **LLM Provider**: The Groq-hosted LLaMA 3.3 is used for fast, high-quality output.

---

## ✅ TODO

- [ ] Parse post from linkedIn using profile url
- [ ] Integrate more LLM providers
- [ ] Add download and share features
- [ ] Improve multi-language handling with locale fallback

---


