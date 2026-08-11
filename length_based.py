from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


# Load the PDF
loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()


# Split text into fixed-size chunks
splitter = CharacterTextSplitter(
    chunk_size=200,       # Maximum characters per chunk
    chunk_overlap=0,     # No overlapping characters
    separator=''          # Split directly by characters
)


# Split each Document into smaller Documents
result = splitter.split_documents(docs)


# Print the first chunk
print(result[0].page_content)