import os
import sys
from dotenv import load_dotenv

# Add the app directory to the Python path
sys.path.append("/app")

from langchain.text_splitter import RecursiveCharacterTextSplitter
from recursive_text_splitter import TextSplitter
from azure_search_uploader import IndexedTextConsumerAzure

text = """What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.
"""


load_dotenv()
PDF_PATH = os.path.join("/app", "media", "constitution_of_india.pdf")


def get_required_env_var(var_name: str) -> str:
    """
    Retrieve a required environment variable with error handling.

    Args:
        var_name (str): Name of the environment variable to retrieve.

    Returns:
        str: Value of the environment variable.

    Raises:
        ValueError: If the environment variable is not set.
    """
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Required environment variable '{var_name}' is not set.")
    return value


def main():
    extracted_text = TextSplitter(
        pdf_path=PDF_PATH,
        chunk_size=2000,
        chunk_overlap=500,
    ).split_pdf_text()

    azure_api_key = get_required_env_var("AZURE_API_KEY")
    azure_endpoint = get_required_env_var("AI_SEARCH_INDEX_ENDPOINT")
    azure_index_name = get_required_env_var("AI_SEARCH_INDEX_NAME")

    IndexedTextConsumerAzure().upload_documents_to_index(
        azure_api_key=azure_api_key,
        azure_endpoint=azure_endpoint,
        azure_index_name=azure_index_name,
        documents=extracted_text,
    )


def main2():
    print("Chunker begin")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        separators=["\n\n", "\n", " "],
        is_separator_regex=False,
    )
    texts = text_splitter.split_text(text)
    print(len(texts))  # 11
    print(texts[0])  # 'What I Worked On\n\nFebruary 2021'


if __name__ == "__main__":
    main()
