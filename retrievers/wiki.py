from langchain_community.retrievers import WikipediaRetriever




retriever=WikipediaRetriever(top_k_results=2,lang='en')# Print the list of text chunks



doc=retriever.get_relevant_documents("india vs pakistan")


for d in doc:
    print(d.page_content)  # Print the content of each document retrieved
    print(d.metadata)  # Print the metadata of each document retrieved