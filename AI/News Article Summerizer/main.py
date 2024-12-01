import tkinter as tk
from textblob import TextBlob
from newspaper import Article

# Function 
def summarize():
    # Geting the URL 
    url = url_text.get().strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    
    article_author = ', '.join(article.authors) if article.authors else "Unknown"
    author.delete('1.0', 'end')
    author.insert('1.0', article_author)

    
    publication.delete('1.0', 'end')
    publication.insert('1.0', str(article.publish_date) if article.publish_date else "Unknown")

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f"Polarity: {analysis.polarity} Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

    # Disableing text fields again to prevent editing
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# Root window setup
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x800')  

#  scrollbar
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.config(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)

canvas.create_window((0, 0), window=frame, anchor="nw")

# Title 
title_label = tk.Label(frame, text="Title")
title_label.pack(pady=5)

# Title  Field
title = tk.Text(frame, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack(pady=5)

# Author 
author_label = tk.Label(frame, text="Author")
author_label.pack(pady=5)

# Author  Field
author = tk.Text(frame, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack(pady=5)

# Publishing Date 
publication_label = tk.Label(frame, text="Publishing Date")
publication_label.pack(pady=5)

# Publication  Field
publication = tk.Text(frame, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack(pady=5)

# Summary 
summary_label = tk.Label(frame, text="Summary")
summary_label.pack(pady=5)

# Summary  Field
summary = tk.Text(frame, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack(pady=5)

# Sentiment 
sentiment_label = tk.Label(frame, text="Sentiment Analysis")
sentiment_label.pack(pady=5)

# Sentiment  Field
sentiment = tk.Text(frame, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack(pady=5)

# URL 
url_label = tk.Label(frame, text="URL")
url_label.pack(pady=5)

# URL  Field
url_text = tk.Entry(frame, width=140)  # Use Entry instead of Text for single-line input
url_text.pack(pady=5)

# Summarize Button
btn = tk.Button(frame, text="Summarize", command=summarize)
btn.pack(pady=20)

# Updateing scroll region to encompass all widgets
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Start the Tkinter main loop
root.mainloop()
