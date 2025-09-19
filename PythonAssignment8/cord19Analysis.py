
# ===============================
# 1. Import Libraries
# ===============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

# ===============================
# 2. Load Data
# ===============================

#DID NOT INCLUDE THE METADATA.CSV FILE WHEN COMMITING BECAUSE OF IT'S LARGE SIZE

csv_file = "metadata.csv"   
df = pd.read_csv(csv_file, low_memory=False)

# ========================
# 3. Basic Exploration
# ===============================
# Show dataset shape and preview
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataFrame info:")
print(df.info())
print("\nShape of dataset (rows, cols):", df.shape)

# Missing values summary
print("\nMissing values per column:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Numerical summary
print("\nSummary statistics for numerical columns:")
print(df.describe())

# ===============================
# 4. Data Cleaning
# ===============================
# Drop rows with missing title or publish_time
df_clean = df.dropna(subset=['title', 'publish_time']).copy()

# Fill missing journal names with "Unknown"
df_clean['journal'] = df_clean['journal'].fillna("Unknown")

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')

# Extract year
df_clean['year'] = df_clean['publish_time'].dt.year

# Word count for abstracts
df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(x.split()))

print("\nShape after cleaning:", df_clean.shape)

# ===============================
# 5. Basic Analysis
# ===============================
# Papers per year
papers_per_year = df_clean['year'].value_counts().sort_index()
print("\nPapers per year:")
print(papers_per_year)

# Top 10 journals
top_journals = df_clean['journal'].value_counts().head(10)
print("\nTop 10 Journals:")
print(top_journals)

# Generate WordCloud for titles
all_titles = " ".join(df_clean['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)

# ===============================
# 6. Streamlit Application
# ===============================
st.title("CORD-19 Dataset Analysis")
st.write("This interactive app lets you explore COVID-19 research metadata from the CORD-19 dataset.")

# Dataset overview
st.subheader("Dataset Overview")
st.write("Shape of dataset:", df_clean.shape)
st.dataframe(df_clean.head())

# Publications per year
st.subheader("Publications Over Time")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(x=papers_per_year.index, y=papers_per_year.values, marker="o", ax=ax1)
ax1.set_title("Number of Publications per Year")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# Top journals
st.subheader("Top Journals")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
ax2.set_title("Top 10 Journals Publishing COVID-19 Research")
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# WordCloud visualization
st.subheader("WordCloud of Paper Titles")
fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.imshow(wordcloud, interpolation="bilinear")
ax3.axis("off")
st.pyplot(fig3)

# Interactive year filter
st.subheader("Filter Papers by Year")
year_selected = st.slider("Select a year", int(df_clean['year'].min()), int(df_clean['year'].max()))
filtered_df = df_clean[df_clean['year'] == year_selected]
st.write(f"Showing {filtered_df.shape[0]} papers from {year_selected}:")
st.dataframe(filtered_df[['title', 'journal', 'publish_time']].head(10))

