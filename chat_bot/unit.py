from langchain_groq import ChatGroq
api_key = "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"
def text_gen(text):
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0,
        max_tokens=256,  # Set a limit to prevent excessive token usage
        timeout=10,  # Avoid infinite waiting
        max_retries=2,
        api_key=api_key,
    )
    
    messages = [{"role": "system", "content": text}]
    
    try:
        ai_msg = llm.invoke(messages)
        return ai_msg.content
    except Exception as e:
        print(f"Error: {e}")
        return "Error generating response"