
import os
from difflib import SequenceMatcher

def read_text(file_path):
    """
    Read and extract text from a text file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def calculate_similarity(text1, text2):
    """
    Calculate the similarity score between two texts using the SequenceMatcher ratio.
    """
    matcher = SequenceMatcher(None, text1, text2)
    return matcher.ratio()

def compare_resume_and_job_description(resume_path, job_description_path):
    """
    Compare the similarity between a resume and a job description.
    """
    resume_text = read_text(resume_path)
    job_description_text = read_text(job_description_path)

    similarity_score = calculate_similarity(resume_text, job_description_text)
    similarity_percentage = similarity_score * 100
    return similarity_percentage

if __name__ == '__main__':
    resume_path = input("Enter the full path of your resume file: ")
    job_description_path = input("Enter the full path of the job description file: ")

    if not os.path.isfile(resume_path) or not os.path.isfile(job_description_path):
        print("Failed to find resume or job description files.")
    else:
        score = compare_resume_and_job_description(resume_path, job_description_path)
        print(f"Similarity Score: {score:.2f}%")

