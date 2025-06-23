import os
import markdown
import google.generativeai as genai
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from app.constants import INITIAL_PROMPT, SAMPLE_RESPONSE


# Load environment variables from .env file
load_dotenv()

# --- Application Setup ---
app = FastAPI(
    title="Prompt Engineering Teacher",
    description="An interactive web application to teach prompt engineering concepts.",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

# Although not used in this version, it's good practice to mount a static directory
# app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Pydantic Models ---
# This model defines the structure of the incoming request body for the /api/prompt endpoint
class PromptRequest(BaseModel):
    prompt: str

# --- Google Generative AI Configuration ---
# Ensure you have a .env file with GOOGLE_API_KEY="your_key_here"
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Warning: GOOGLE_API_KEY environment variable not found.")
    # The app can still run, but API calls will fail.
    # This allows frontend development without a key.
else:
    genai.configure(api_key=api_key)

# --- Helper Functions ---
def load_exercise_content(exercise_name: str) -> str:
    """
    Loads the markdown content for a given exercise and converts it to HTML.
    Args:
        exercise_name: The name of the exercise directory.
    Returns:
        The exercise content as an HTML string.
    Raises:
        HTTPException: If the exercise file is not found.
    """
    file_path = f"exercises/{exercise_name}/description.md"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content)
        return html_content
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Exercise '{exercise_name}' not found.")


# --- API Endpoints ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main page of the application.
    It loads the content for the 'zero_shot_prompting' exercise by default.
    """
    # Load the exercise content from the markdown file
    exercise_html = load_exercise_content("zero_shot_prompting")

    # Render the main index.html template with the exercise content
    return templates.TemplateResponse(
        "index.html", {"request": request, "exercise_html": exercise_html}
    )


@app.post("/api/prompt")
async def get_llm_response(prompt_request: PromptRequest):
    """
    Receives a user's prompt and returns a response from the Google Gemini model.
    """
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="Google API key is not configured on the server.",
        )

    try:
        # The requirement mentioned 'gemini-2.0-flash', but 'gemini-1.5-flash' is the
        # current recommended and available model in the 'flash' family.
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        chat = model.start_chat(history=[])
        tutor_prompt = INITIAL_PROMPT.format(
            exercise_content="Generating a simple Python function to get factorial of number using Zero-Shot Prompting",
            user_prompt=prompt_request.prompt
        )

        # For development, we return a sample response. In production, you would use the line below.
        print(prompt_request.prompt)
        response = chat.send_message(tutor_prompt)
        response_html = markdown.markdown(str(response.text))
        # return response_html
        return HTMLResponse(content=response_html,
                            media_type="text/html",
                            status_code=200)

    except Exception as e:
        # Handle potential errors from the API call
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Error fetching response from the LLM.")

# To run the app, use the command: uvicorn main:app --reload