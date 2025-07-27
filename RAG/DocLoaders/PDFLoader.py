from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader("./Dharmesh_resume_23_july (1).pdf")

# Extract documents (1 per page by default)
documents = loader.load()


print(documents[0].page_content)  # Print the content of the first pagecls 