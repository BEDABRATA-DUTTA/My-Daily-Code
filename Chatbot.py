import tkinter as tk
from tkinter import scrolledtext

# LangChain imports
from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace,
)
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Your HF Token
token = "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"

# LLM Model
llm_raw = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=200,
    huggingfacehub_api_token=token
)

llm = ChatHuggingFace(llm=llm_raw)

# Chat History
chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

# ---------------- GUI SECTION ---------------- #

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("700x600")
root.config(bg="#1e1e1e")

# Chat Display Box
chat_window = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=70, height=25,
    bg="#2d2d2d", fg="white", font=("Segoe UI", 12)
)
chat_window.pack(pady=10)
chat_window.config(state=tk.DISABLED)

# Input Field
user_entry = tk.Entry(
    root, width=60,
    font=("Segoe UI", 13),
    bg="#2d2d2d", fg="white"
)
user_entry.pack(side=tk.LEFT, padx=10, pady=5)

# Send Button
def send_message():
    user_text = user_entry.get()
    if not user_text:
        return
    
    # Display user message
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_text}\n", "user")
    chat_window.config(state=tk.DISABLED)
    
    user_entry.delete(0, tk.END)

    # Add to chat history
    chat_history.append(HumanMessage(content=user_text))

    # Exit condition
    if user_text.lower() == "exit":
        root.quit()
        return

    # Get AI Response
    ai_response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=ai_response.content))

    # Display AI response
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"AI: {ai_response.content}\n\n", "ai")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

# Button
send_btn = tk.Button(
    root, text="Send", width=10,
    font=("Segoe UI", 13),
    command=send_message,
    bg="#0078d7", fg="white"
)
send_btn.pack(side=tk.LEFT, padx=10)

# Bind Enter Key
root.bind("<Return>", lambda event: send_message())

# Chat Formatting
chat_window.tag_config("user", foreground="#00b7ff")
chat_window.tag_config("ai", foreground="#98fb98")

# Run App
root.mainloop()
