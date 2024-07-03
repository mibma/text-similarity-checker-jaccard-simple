import re
import streamlit as st

# Function to clean text by removing stop words and non-alphabet characters
def clean_text(text):
    stop_words = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])
    
    # Remove non-alphabet characters and convert to lower case
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Split text into words and remove stop words
    words = text.split()
    cleaned_text = ' '.join(word for word in words if word not in stop_words)
    
    return cleaned_text

# Function to calculate similarity and difference
def calculate_similarity(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    similarity = words1.intersection(words2)
    difference = words1.symmetric_difference(words2)
    
    return len(similarity), len(difference)

# Function to calculate Jaccard similarity
def jaccard_similarity(similarity, difference):
    union = similarity + difference
    return float(similarity) / union if union != 0 else 0

if __name__ == "__main__":
    st.title("Text Similarity Checker")
    st.write("This app calculates the similarity between two text files using Jaccard similarity.")

    uploaded_file1 = st.file_uploader("Upload the first text file", type=["txt"])
    uploaded_file2 = st.file_uploader("Upload the second text file", type=["txt"])

    if uploaded_file1 and uploaded_file2:
        text1 = uploaded_file1.read().decode("utf-8")
        text2 = uploaded_file2.read().decode("utf-8")
        
        cleaned_text1 = clean_text(text1)
        cleaned_text2 = clean_text(text2)
        
        similarity, difference = calculate_similarity(cleaned_text1, cleaned_text2)
        print(similarity,difference)
        jaccard_sim = jaccard_similarity(similarity, difference)
        print(jaccard_sim)
        st.write(f"The similarity between the texts is {jaccard_sim:.2f}")

