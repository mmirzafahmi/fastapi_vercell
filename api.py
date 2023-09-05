from fastapi import FastAPI, Request, Response, HTTPException, Header

app = FastAPI()


@app.get("/")
def home():

    response = Response(content="Hello, welcome to our public site.")

    return response


@app.get("/response")
def example():

    content = "Hello, this is the response content."

    # Create a Response object and set custom headers
    response = Response(content=content)
    response.headers["X-Custom-Header"] = "This is custom value"
    response.headers["Authorization"] = "pass_token_1234"

    return response


@app.get("/protected")
def protected(api_key: str = Header(None)):

    if api_key is None or api_key != 'password123':
        raise HTTPException(status_code=401, detail="Invalid API key.")

    return {
        "message": "Welcome User to the restricted  area."
    }

