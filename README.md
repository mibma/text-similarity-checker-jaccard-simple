# Text Similarity Checker

This is a simple Streamlit web application that calculates the similarity between two text files using Jaccard similarity.

## Features

- Upload and compare two text files.
- Clean the text by removing stop words and non-alphabet characters.
- Calculate the similarity and difference between the cleaned texts.
- Display the similarity score using Jaccard similarity.

## Requirements

- Python 3.x
- Streamlit
- re (regular expressions)

## Installation

Clone the repository or download the script file.
## Usage

1. Run the Streamlit app.

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit 

3. Upload two text files to compare their similarity.

## Example

1. Upload the first text file.
2. Upload the second text file.
3. The app will display the similarity score between the two texts.

## Explanation of Code

### clean_text Function

- Removes non-alphabet characters and stop words.
- Converts text to lower case.

### calculate_similarity Function

- Computes the number of common words and unique words between two cleaned texts.

### jaccard_similarity Function

- Calculates the Jaccard similarity index based on the intersection and union of the word sets.

### Streamlit Interface

- Provides a simple interface to upload two text files, processes the texts, and displays the similarity result.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me directly.

