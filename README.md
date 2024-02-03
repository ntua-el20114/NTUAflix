<p align="center">
  <img src="logo.png" alt="Logo of Ntuaflix">
</p>

# Ntuaflix
Welcome to Ntuaflix, a comprehensive platform for movie enthusiasts! Dive into a vast collection of movies,
express your preferences through likes or dislikes,engage in conversations with a specialized movie chatbot,
and get personalized movie recommendations. Ntuaflix combines a robust backend with a user-friendly interface,
ensuring an enjoyable and interactive movie browsing experience.

## Features

- **Explore Movies and Actors**: Browse through an extensive database of movies and actors.
- **Interactive Movie Recommendations**: Receive personalized movie suggestions based on your preferences.
- **Chatbot**: Engage in movie-related conversations with our AI-powered chatbot.
- **Like/Dislike System**: Express your opinions on movies with a simple like or dislike.
- **Web and CLI Interface**: Access Ntuaflix via a sleek web application or a command-line interface.

## Technology Stack

Our application leverages a mix of technologies to deliver a seamless and efficient user experience:

- **MySQL**: Robust database for storing movie and actor data.
- **Jupyter Notebooks**: For crafting SQL queries and managing database operations.
- **Python Flask**: Back-end API development.
- **Torch & NLTK**: Powering our AI chatbot for natural language processing.
- **Prolog & Python**: Engine for our intelligent movie recommender system.
- **Front-end Web App**: Developed using Python Flask, HTML, and CSS.
- **CLI Client**: Built with the Python Argparse library for command-line functionality.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- MySQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ntua/softeng23-44
    ```

2. Navigate to repository:
   ```bash
   cd softeng23-44
    ```

3. Install required packages:
   ```bash
   cat requirements.txt | xargs -n 1 pip install --no-deps --ignore-installed || true
    ```
### Running the App

4. Run the webapp here:
   ```bash
   cd front_end/
   python app.py
    ```
5. Run the cli client here:
   ```bash
   cd cli_client/
   python se2344.py
    ```

## Demo

Check out our [YouTube demo](https://www.youtube.com/) to see Ntuaflix in action!

