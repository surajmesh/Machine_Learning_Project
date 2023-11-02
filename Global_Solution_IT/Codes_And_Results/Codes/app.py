import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
import os
import pandas as pd


print(os.getcwd())

# Change working directory

#os.chdir(r"C:\Users\Suraj\Documents\Analytics_Project_Repo\ML_Projects\Global Solution IT\GAIS-TASK\queries_data")


# show list Of dataset in the directory
#os.listdir("C:\\Users\\Suraj\\Documents\\Analytics_Project_Repo\\ML_Projects\\Global Solution IT\\GAIS-TASK\\queries_data")

# Load the queries dataset
queries_df = pd.read_csv('queries.csv')
#print(queries_df)






# Initialize Streamlit app
st.title("Query Search App")

# Preprocess the dataset
queries_df['processed_text'] = queries_df['query'].apply(lambda x: x.lower())

# make object TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the vectorizer
tfidf_matrix = vectorizer.fit_transform(queries_df['processed_text'])

# function that return similar querires based on given
def search(query, top_n=3):
    # make each char in lower case
    processed_query = query.lower()

    # Handle misspelled words
    spell = SpellChecker()
    tokens = word_tokenize(processed_query)
    corrected_query = ' '.join(spell.correction(token) for token in tokens)

    # Transform the query using the same vectorizer
    query_vector = vectorizer.transform([corrected_query])

    # Cosine similarity between the query and dataset
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Rank the results based on relevance
    ranked_indices = similarity_scores.argsort()[::-1]

    # Return top n results
    top_results = queries_df.iloc[ranked_indices[:top_n]]['query'].tolist()

    if not top_results:
        st.warning("No results found.")
        return []

    return top_results

# Streamlit UI
user_query = st.text_input("Enter your search query:")
if user_query:
    results = search(user_query, top_n=3)

    # Show results
    st.subheader("Top Three Results:")

    if results:
        for i, result in enumerate(results, 1):
            st.write(f"{i}. {result}")
    else:
        st.info("No results found for the given query.")
