from langchain.text_splitter import CharacterTextSplitter

txtsplitter = CharacterTextSplitter(
    chunk_size=10,  # Size of each chunk
    chunk_overlap=5,  # Overlap between chunks
    separator=''
)


result = txtsplitter.split_text("This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, and there will be no overlap between the chunks.")


print(result)  # Print the list of text chunks