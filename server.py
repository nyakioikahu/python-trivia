from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

QUESTION = "What is the name of my first dog?"
ANSWER = "Daisy"

QUESTION2 = "Am I 18+?"
ANSWER2 = "Yes"

QUESTION3 = "What High School did I study in?"
ANSWER3 = "Kabarak"

def handle_request(request):
    parsed_path = urlparse(request.path)
    params = parse_qs(parsed_path.query)

    message = "No answer yet"


    if "answer" in params:
        if clean_input(params["answer"][0]) == ANSWER.lower():
            message = "You know me well!, friend verified :)"
        else:
            message = "Just say you want to cut me off :("
    
    if "yn" in params:
        if params["tf"][0] == ANSWER2.lower():
            message = "You know me well!, friend verified"
        else:
            message = "Just say you want to cut me off :("

    if "answer" in params:
        if clean_input(params["answer"][0]) == ANSWER3.lower():
            message = "You know me well!, friend verified :)"
        else:
            message = "Just say you want to cut me off :("

    show_question(request, message)

def clean_input(input):
    return input.strip().lower()

def show_question(response, message=""):
    html = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>How well do you know Nyakio:)</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color:rgb(176, 148, 199); }}
            h1 {{ color: pink; }}
            .q-container {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                background: rgb(204, 248, 234);
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
                color: black;
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
                <label for="y"> Yes </label>
                <input type="radio" name="yn" value="yes" id="y"/>
                <label for="n"> No </label>
                <input type="radio" name="yn" value="no" id="n"/>
                <button type="submit">Check</button>
            </form>
        </div>
         <div class="q-container">
            <h1>{QUESTION3}</h1>
            <form>
                <input type="text" name="answer" placeholder="Type your answer">
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
