from dotenv import load_dotenv
import os
from pypdf import PdfReader

# Load environment variables
load_dotenv()

# API client setup
# api_key = os.getenv('API_KEY')  # Make sure the key is correctly fetched
# client = genai.Client(api_key=api_key)

# Define the PDF path
pdf_path = "C:/Users/USER/Documents/_OceanofPDF.com_Why_Nations_Fail_-_Daron_Acemoglu_James_Robinson.pdf"
reader = PdfReader(pdf_path)

# Function to extract text from all pages
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    all_text = {}
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        all_text[i + 1] = text  # Store text per page (starting from 1 for readability)
    return all_text

# Function to search for the exact or partial excerpt in the extracted text
def search_excerpt(excerpt, all_text):
    page_matches = {}
    for page_num, text in all_text.items():
        # Check if the user's excerpt is in the page text
        if excerpt.lower() in text.lower():  # Case-insensitive search
            page_matches[page_num] = text
    return page_matches

# Main function to extract text and search for user input
def main():
    # User input (the excerpt they want to search for)
    user_input = input("Enter the excerpt you want to search for: ")

    # Extract text from all pages of the PDF
    all_text = extract_text_from_pdf(pdf_path)

    # Search for the excerpt in the extracted text
    matches = search_excerpt(user_input, all_text)

    # Print the results
    if matches:
        print("\nFound matches on the following pages:")
        for page_num, page_text in matches.items():
            print(f"\nPage {page_num}:\n{page_text}")
    else:
        print("\nNo matches found.")

# Run the program
if __name__ == "__main__":
    main()
