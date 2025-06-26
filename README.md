# TEXT-SUMMARIZATION-TOOL



INTRODUCTION:
With the help of the straightforward yet effective Python application Text Summarization Tool, users may create succinct summaries of large paragraphs or articles. It provides keyword extraction and word count analysis in addition to using Natural Language Processing (NLP) techniques to extract the most pertinent phrases from the provided text. Because Tkinter, a Python GUI package, was used in its design, the program is interactive and easy to use.
An important NLP approach that enables users to rapidly understand the main idea of lengthy textual content is text summary. This tool offers an effective method of extracting the most important information, whether it is being used by professionals to condense reports, students to summarize academic papers, or casual users to simplify publications.

FEATURES:
>>NLP-Based Summarization:The application extracts important sentences from the given text using Latent Semantic Analysis (LSA), a statistical method of summarization. Even though the summary is much shorter than the original text, it guarantees that the sense is retained.
>>The extraction of keywords:It assists users in determining the most significant subjects addressed in the original article by extracting the top five most pertinent keywords from the text.
>>A Study of Word Count Analysis:helps readers comprehend the reduction ratio by displaying both the original and summary word counts.
>>Easy to Use GUI:The program, which was created using Tkinter, has a straightforward graphical user interface. Users may input text, click the "Summarize" button, and get the summary and other information right away.
>>Moveable Text Field:Because both the input text box and the output summary box may be scrolled, handling huge text inputs and quickly reviewing the summarized material is made simple.

TECHNOLOGIES USED:
-Python 3 – Core programming language
-Tkinter – GUI library for interactive user interface
-NLTK (Natural Language Toolkit) – Used for tokenization, stopword removal, and NLP tasks
-Sumy – Summarization library based on LSA
-Regular Expressions (re) – For keyword extraction and text processing
-Collections (Counter) – To determine keyword frequency

INSTALLATION & SETUP:
Prerequisites:Before running the program, ensure you have Python installed on your system. You also need to install the required libraries.
Step 1: Install Python Libraries:
Run the following commands in your terminal or command prompt to install the required dependencies: pip install nltk sumy
Step 2: Download NLTK Resources:
Since the tool uses stopwords and tokenization, you need to download the necessary NLTK resources: 
import nltk
nltk.download('stopwords')
nltk.download('punkt')
Step 3: Run the Application:
Once the dependencies are installed, save the Python script (summarizer.py) and run it using: python summarizer.py

HOW TO USE:
Launch the Application – Run the script, and a GUI window will open.
Enter Text – Type or paste the lengthy text into the input area.
Click "Summarize" – Press the summarize button to process the text.
View Summary & Keywords – The summarized text, word counts, and keywords will be displayed instantly.

CODE BREAKDOWN:
summarize_text(): Extracts key sentences from the input text using LSA summarization.
extract_keywords(): Uses word frequency analysis to determine the most relevant keywords.
Tkinter GUI Elements:
-ScrolledText(): Creates a scrollable text area.
-Button(): Calls the summarization function on click.
-Label(): Displays word count and extracted keywords.

FUTURE ENCHANCEMENTS:
>> Adjustable Summary Length – Allow users to specify the number of sentences in the summary.
>> Copy Summary Button – A button to copy the generated summary to the clipboard.
>> Save Summary as a File – Option to save the summary as a text file.
>> More Summarization Algorithms – Implement additional NLP-based summarization techniques like TextRank and LexRank.

CONCLUSION:
The Text Summarization Tool is an excellent solution for quickly condensing long-form text into short and meaningful summaries. It’s an easy-to-use, efficient, and accurate NLP-based summarization system that can help professionals, students, and researchers extract essential information from lengthy documents.With its intuitive GUI, users can input text, click a button, and receive summarized text along with key insights in just seconds!


OUTPUT:

![Image](https://github.com/user-attachments/assets/0307af58-5a10-4dbc-bed2-8073dcecd733)

![Image](https://github.com/user-attachments/assets/ae2217db-c53e-416e-9aeb-bd36acc0b372)
