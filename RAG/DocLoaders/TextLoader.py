from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    "./cricket.txt",
    encoding="utf-8",
    autodetect_encoding=True,
)


docs= loader.load()

print(docs[0].page_content)
