from langchain_community.document_loaders import WebBaseLoader
loader=WebBaseLoader(["https://commons.wikimedia.org/wiki/Commons:Welcome"]) # can give list of URLs as well
# loader=WebBaseLoader("https://commons.wikimedia.org/wiki/Commons:Welcome") // can give single URL as well


doc=loader.load()


print(doc[0].page_content)  # Print the content of the first page