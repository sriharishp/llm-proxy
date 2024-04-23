## Requirements
* pydantic
* fastapi
* httpx

## Usage

1. Start the FastAPI server:
   ```sh
   uvicorn app.app:app --reload
   ```

2. The server will be running at `http://127.0.0.1:8000`. You can access the following endpoints:
   - Chat completions: `POST /completions`

   The copmletions endpoint expects the request body to be a JSON object that MUST contain the model attribute and whatever further attributes are expected alongside your model of choice. The header must correspond to whichever model you are choosing to route to.
