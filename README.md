# Trivia Web Server

This project is a simple web-based trivia game using Python's built-in HTTP server. It asks users questions and evaluates their responses.

## Features
- Runs a local web server on port `8000`.
- Asks users a trivia question via a web page.
- Evaluates their responses and displays a message based on correctness.
- Uses `watchdog` to auto-restart the server on code changes.

## Prerequisites
Ensure you have Python installed. This project works with Python 3.

## Installation and Setup
### 1. Clone the Repository
```sh
git clone https://github.com/JKUAT-Inspire-Youth-In-STEM/python-trivia.git
cd JKUAT-Inspire-Youth-In-STEM
```

### 2. Install Dependencies
Install `watchdog` to enable auto-restart on code changes:
```sh
pip install watchdog
```

### 3. Run the Server
Start the server manually:
```sh
python server.py
```
Or use `watchmedo` for auto-restarting when files change:
```sh
watchmedo auto-restart --pattern="*.py" --recursive -- python server.py
```

### 4. Access the Trivia Page
Open your browser and visit:
```
http://localhost:8000
```

## Modifying the Questions
To modify the questions, edit the variables in `server.py`:
```python
QUESTION = "Your question here"
ANSWER = "correct answer"
QUESTION2 = "Another question"
ANSWER2 = "true"  # For True/False
```

## Troubleshooting
- If the server doesn't start, ensure port 8000 is not in use.
- If changes are not reflected, restart the server.

## License
This project is open-source. Feel free to modify and improve it.

