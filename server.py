from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

QUESTION = "What's my favourite color"
ANSWER = "red"

QUESTION2 = "Do I have a phone"
ANSWER2 = "True"


def handle_request(request):
    parsed_path = urlparse(request.path)
    params = parse_qs(parsed_path.query)

    message = "No answer yet"


    if "answer" in params:
        if clean_input(params["answer"][0]) == ANSWER.lower():
            message = "You know my favourite color!, friend verified :)"
        else:
            message = "Couldn't be worse, reconsidering friendship :("
    
    if "tf" in params:
        if params["tf"][0] == ANSWER2.lower():
            message = "Thats correct, friend verified"
        else:
            message = "Couldn't be worse, reconsidering friendship :("
    

    show_question(request, message)

def clean_input(input):
    return input.strip().lower()

def show_question(response, message=""):
    html = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Trivia</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color: #f4f4f4; }}
            h1 {{ color: #4CAF50; }}
            .q-container {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                background: white;
                padding: 20px;
                margin: 20px auto;
                width: 60%;
                min-height: 7rem;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }}
            input, button {{ padding: 10px; margin: 10px; font-size: 16px; }}
            button {{
                background-color: #008CBA;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }}
            button:hover {{ background-color: #005f73; }}
            p {{ font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="q-container">
            <h1>{QUESTION}</h1>
            <form>
                <input type="text" name="answer" placeholder="Type your answer">
                <button type="submit">Check</button>
            </form>
        </div>

        <div class="q-container">
            <h1>{QUESTION2}</h1>

            <form>
                <label for="t"> True </label>
                <input type="radio" name="tf" value="true" id="t"/>
                <label for="f"> False </label>
                <input type="radio" name="tf" value="false" id="f"/>
                <button type="submit">Check</button>
            </form>
        </div>

        <p>FINAL VERDICT: {message}</p>
    </body>
    </html>"""

    
    response.send_response(200)
    response.send_header("Content-type", "text/html")
    response.end_headers()
    response.wfile.write(html.encode())

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request(self)

if __name__ == "__main__":
    server = HTTPServer(("", 8000), RequestHandler)
    print("Server running on port 8000...")
    server.serve_forever()
