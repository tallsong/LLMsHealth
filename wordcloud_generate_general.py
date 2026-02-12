import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from keybert import KeyBERT
from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df =pd.read_parquet("dataset/combined_filtered.parquet") # Change YOUR_CSV

# Load the model
model = KeyBERT('sentence-transformers/stsb-roberta-base')

# Add custom keywords, stuff that doesnt add value
custom_stopwords = [
    "study",
    "results",
    "method",
    "methods",
    "analysis",
    "using",
    "based",
    "approach",
    "conclusion",
    "nan",
    "use",
    "research",
    "review",
    "showed",
    "set",
    "freetext",
    "reviewed",
    "case",
]


stopwords = list(ENGLISH_STOP_WORDS) + custom_stopwords

# Extract top 25 keywords per document
all_keywords_per_record = []

# Please make sure your abstract column is CLEANED PROPERLY, lowercase etc.
for idx, abstract in enumerate(df["abstract"].dropna().astype(str)):
    print(f"Completed {idx} records so far") if idx % 10 == 0 else None
    keywords = model.extract_keywords(
        abstract,
        stop_words=stopwords,
        top_n=25,
    )
    all_keywords_per_record.append(keywords)


# Aggregate scores across all documents
keyword_weights = defaultdict(float)
for record_keywords in all_keywords_per_record:
    for word, score in record_keywords:
        keyword_weights[word] += score  # sum scores across all records

# sort and take top 100 for cleaner word cloud
keyword_weights = dict(sorted(keyword_weights.items(), key=lambda x: x[1], reverse=True)[:100])

wordcloud = WordCloud(
    background_color='white',
    prefer_horizontal=0.9, # 90% chance of horizontal text (Default)
    colormap="winter", # or spring
    max_words=100, # Max number of words to display
    relative_scaling=0.8, # Importance of relative word frequencies for font-size 
    random_state=1,
    width=1920, 
    height=1080,
).generate_from_frequencies(keyword_weights)

# CHANGE ACCORDINGLY!!! Capital First letters!
HEALTHCARE_SECTION_NAME =  "scientific research"

# Display the generated image
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") # Hide the axes
plt.title(f'Word Cloud {HEALTHCARE_SECTION_NAME} Abstracts (RoBERTa)')

DPI = 200
WIDTH_INCHES = 1920 / DPI
HEIGHT_INCHES = 1080 / DPI

# Set the desired final size and save BEFORE showing
current_fig = plt.gcf()
current_fig.set_size_inches(
    WIDTH_INCHES, HEIGHT_INCHES
)

# CHANGE ACCORDINGLY
SAVE_FILE_NAME = "imaging_wordcloud"
plt.savefig(f"./{SAVE_FILE_NAME}.png", dpi=DPI, bbox_inches="tight")  # Save

# 3. Display the figure (if desired)
plt.show()

# 4. Close the figure
plt.close(current_fig)

print(
    f"Plot saved successfully at {WIDTH_INCHES:.1f}x{HEIGHT_INCHES:.1f} inches with {DPI} DPI, resulting in 1920x1080 pixels."
)