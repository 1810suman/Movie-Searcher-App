import requests
import tkinter as tk
from tkinter import messagebox

def search_movie():
    api_key = "YOUR_API_KEY"  # You need to get an API key from http://www.omdbapi.com/
    movie_name = movie_entry.get()
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["Response"] == "False":
            messagebox.showinfo("Error", data["Error"])
        else:
            title_label.config(text="Title: " + data["Title"])
            year_label.config(text="Year: " + data["Year"])
            genre_label.config(text="Genre: " + data["Genre"])
            plot_label.config(text="Plot: " + data["Plot"])

    except Exception as e:
        messagebox.showinfo("Error", "An error occurred.")

# Create the main window
window = tk.Tk()
window.title("Movie Searcher")

# Set window size
window.geometry("800x600")  # Set the width and height

# Set background color
window.configure(bg="orange")

# Create a heading
heading_label = tk.Label(window, text="Movie Searcher", font=("Segoe UI Black", 36), bg="orange")
heading_label.pack(pady=10)  # Add padding

# Create GUI elements
tk.Label(window, text="Enter Movie's Name:", font=("Arial",24), bg="orange").pack()
movie_entry = tk.Entry(window, width=40, font=('Arial 18'))
movie_entry.pack(padx=10, pady=10)

search_button = tk.Button(window, text="Search", font=("Arial", 18), bg="blue", command=search_movie)
search_button.pack()

# Labels to display movie information
title_label = tk.Label(window, text="", font=("Arial", 22), bg="orange")
title_label.pack()

year_label = tk.Label(window, text="", font=("Arial", 22), bg="orange")
year_label.pack()

genre_label = tk.Label(window, text="", font=("Arial", 22), bg="orange")
genre_label.pack()

plot_label = tk.Label(window, text="", font=("Arial", 18), bg="orange", wraplength=500)
plot_label.pack(padx=10, pady=10)

# Start the application
window.mainloop()
