import os
import pdfplumber
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

#PDF_FOLDER = "pdfs"  # Folder where your PDFs are stored
PDF_FOLDER=r'C:\Users\bedab\OneDrive\Desktop\Interview Prep' 

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def search_keyword_in_pdfs(keyword):
    results = []
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            path = os.path.join(PDF_FOLDER, filename)
            text = extract_text_from_pdf(path)
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if keyword.lower() in line.lower():
                    # Show a few lines of context
                    context = "\n".join(lines[max(0, i-1): min(len(lines), i+2)])
                    results.append(f"📄 File: {filename}\n{context}\n{'-'*40}")
    return results

def on_search():
    keyword = entry.get()
    if not keyword:
        messagebox.showinfo("Input Error", "Please enter a keyword.")
        return

    results = search_keyword_in_pdfs(keyword)
    output.delete('1.0', tk.END)
    if results:
        output.insert(tk.END, "\n\n".join(results))
    else:
        output.insert(tk.END, "❌ No related context found.")

# GUI
root = tk.Tk()
root.title("Finder")
root.geometry("700x500")
root.configure(bg="#B2BEB5") 

tk.Label(root, text="Enter Context Below").pack(pady=5)
entry = tk.Entry(root,width=50)
entry.pack(pady=5)

#tk.Button(root, text="Search", command=on_search).pack(pady=10)
tk.Button(root, text="Search",width=15,height=2, bg="#B2BEB5", fg="black").pack(pady=5)

output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=55)
output.pack(pady=10)

root.mainloop()
