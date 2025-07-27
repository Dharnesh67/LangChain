from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " ", ""]
)


long_text = ("This is a sample text to be split into smaller chunks. Each chunk will have a maximum size of 100 characters, "
             "and there will be no overlap between the chunks. " * 10)
chunks = splitter.split_text(long_text)



print(chunks)  # Print the list of text chunks