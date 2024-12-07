# Sentiment Analyzer for XLSX Documents

# Overview:
This script analyzes sentiments of text data in an XLSX file. It identifies the sentiment as Positive, Negative, or Neutral using TextBlob and provides polarity and subjectivity scores.

# Requirements:
- Python 3.8 or newer
- Libraries:
  - pandas
  - textblob
  - openpyxl

# Installation:
1. Install the required libraries using pip:
   - `pip install pandas textblob openpyxl`
2. (Optional) Download NLTK corpora for TextBlob:
   - `python -m textblob.download_corpora`

# Usage:
1. Place your input XLSX file in the working directory.
2. Ensure the file contains a "Text" column with the text to analyze.
3. Update the script with the file path and sheet name.
4. Run the script using Python.
5. The output file will include:
   - Sentiment (Positive, Negative, Neutral)
   - Polarity (-1 to 1)
   - Subjectivity (0 to 1)

# Output Example:
Text: "I love this product!"
Sentiment: Positive
Polarity: 0.75
Subjectivity: 0.8

# Author:
Muhammad Anas Akhtar
