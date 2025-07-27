from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(file_path="path/to/your/file.csv")
documents = loader.load()
print(documents[0].page_content)  # Print the content of the first page