# Movie-Searcher-App

This Python code creates a simple movie search application using the OMDB API. The application uses the requests library to make API requests to retrieve movie information based on user input. The search_movie() function gets the movie name from the entry widget, constructs the API URL, sends a request, and displays the movie's details like title, year, genre, plot, and IMDb rating. If the movie is not found or an error occurs, it displays an error message using messagebox.

The tkinter library is used for the graphical user interface (GUI). It creates a main window with a title "Movie Searcher" and sets its size and background color. GUI elements include a label for the heading, an entry widget for the user to input a movie's name, a search button that triggers the search_movie() function, and labels to display movie information. These labels update dynamically based on the API response. The application runs in a loop using window.mainloop(), allowing the user to interact with it.






