import nltk
import re
import tkinter as tk
from tkinter import scrolledtext
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from collections import Counter
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

def summarize_text():
    """Summarize the input text and display results in the GUI."""
    text = text_input.get("1.0", tk.END).strip()
    
    if not text:
        result_label.config(text="⚠️ Please enter text to summarize.")
        return
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 3)  # Extract 3 sentences
    
    summarized_text = " ".join(str(sentence) for sentence in summary)
    original_word_count = len(text.split())
    summarized_word_count = len(summarized_text.split())
    keywords = extract_keywords(text, top_n=5)

    # Display results in the GUI
    summary_output.config(state=tk.NORMAL)
    summary_output.delete("1.0", tk.END)
    summary_output.insert(tk.END, summarized_text)
    summary_output.config(state=tk.DISABLED)

    result_label.config(text=f"Original Words: {original_word_count} | Summarized Words: {summarized_word_count}")
    keywords_label.config(text="Keywords: " + ", ".join(keywords))

def extract_keywords(text, top_n=5):
    """Extract keywords based on word frequency."""
    words = re.findall(r'\b\w+\b', text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words)
    return [word for word, _ in word_freq.most_common(top_n)]

# GUI Setup
root = tk.Tk()
root.title("Text Summarization Tool")
root.geometry("600x500")

# Title
title_label = tk.Label(root, text="Text Summarization Tool", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Text Input
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_input.pack(pady=10)

# Summarize Button
summarize_button = tk.Button(root, text="Summarize", font=("Arial", 12), command=summarize_text)
summarize_button.pack(pady=5)

# Summary Output
summary_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=6, state=tk.DISABLED)
summary_output.pack(pady=10)

# Result Labels
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()
keywords_label = tk.Label(root, text="", font=("Arial", 12))
keywords_label.pack()

# Run GUI
root.mainloop()
