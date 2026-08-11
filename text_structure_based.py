from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.
These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""


# Initialize RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Maximum size of each chunk
    chunk_overlap=0      # No overlap between chunks
)


# Split the text into smaller chunks
chunks = splitter.split_text(text)


# Print number of chunks
print(len(chunks))

# Print all chunks
print(chunks)