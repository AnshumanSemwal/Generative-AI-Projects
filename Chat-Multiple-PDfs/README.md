About:
  Chat with multiple Pdfs uploaded. Ask any question and extract required information as deeemed fit.

Flow:
     with sidebar:
      pdfs uploaded
      if button submitted:
        get_pdf_text function is called (stored in raw_text):
          text page by page is extracted
        get_text_chunks is called (stored in text_chunks):
          Recursively spitted text stored in chunks
        get_vector_store function is called and text_chunks is sent to embedded 
      User's question is taken
      if question, function user_input is called:
        database loaded which contains vector embeddings
        similarity search is applied to find relevant information
        conversational chain is created using get_conversational_chain function:
        prompt template model is provided and chain is loaded.
      response is retrieved using pdfs, user_question
      print the response
