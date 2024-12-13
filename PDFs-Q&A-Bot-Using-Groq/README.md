Project: Talk with multiple pdf's. Deep dive ina conversation to understand details in the pdf's.

*Note: Groq: We utilise groqChat, which in turns benefits from their powerful LPU to provide with efficient and high performing AI inference.

Flow:
  All the required env are loaded
  if vector embeddings has'nt been performed yet:
    Call embedding model
    load pdfs and store in a cariable (docs)
    split text in doc in chunks and make final doc
    use FAISS for clustering of text in vector (use embeddings and final document)

  prompt input is taken
  vector embedding is called when submit button pressed
  if prompt input has been given
    takes a chain based on prompt and LLM
    vector is retrieved as vector object
    retrieval chain created based on retrieval and document chain
    then retrieval chain is invoked with the input prompt and response is stored
    print the response

  Addtionally, sidebar is used to upload PDFs

  
    
