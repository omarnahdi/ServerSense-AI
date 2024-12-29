from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.StreamHandler(),  # Output logs to the console
        RotatingFileHandler('app.log', maxBytes=1024 * 1024, backupCount=5)  # Output logs to a file with rotation
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY environment variable is not set")
    raise ValueError("GOOGLE_API_KEY environment variable is not set")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Define server plans globally
server_plans_data = [
    {"id": 1, "name": "Basic Compute", "cpu_cores": 4, "ram_gb": 8, "gpu": "No GPU", "storage_gb": 128,
     "price_in_usd": 20, "description": "Ideal for basic web hosting or lightweight applications."},
    {"id": 2, "name": "Graphics Starter", "cpu_cores": 8, "ram_gb": 16, "gpu": "NVIDIA T4", "storage_gb": 256,
     "price_in_usd": 150, "description": "Good for entry-level GPU workloads like rendering or AI."},
    {"id": 3, "name": "AI Optimized", "cpu_cores": 16, "ram_gb": 32, "gpu": "NVIDIA A100", "storage_gb": 1024,
     "price_in_usd": 600, "description": "Designed for heavy GPU tasks."},
    {"id": 4, "name": "Enterprise Max", "cpu_cores": 32, "ram_gb": 128, "gpu": "NVIDIA H100", "storage_gb": 4096,
     "price_in_usd": "Contact sales on +91 123456789",
     "description": "High-performance solution for enterprise-scale applications."}
]
server_plans_json_str = json.dumps(server_plans_data)

class ChatRequest(BaseModel):
    message: str

@app.post('/api/chat')
async def chat(chat_request: ChatRequest):
    logger.info(f"Received chat request: {chat_request.message}")

    message = chat_request.message

    if not message:
        logger.warning("Empty message received in chat request")
        raise HTTPException(status_code=400, detail="Please provide a message.")

    try:
        prompt = f"""
            You are a server recommendation assistant. Your task is to help users choose a plan from the available options. provide contact sales on +91 123456789 if the you recommend Enterprise Max plan".

            Available Server Plans:
            {server_plans_json_str}

            User Request: "{message}"

            Based on the user's request and the available server plans, recommend the most suitable plan and briefly explain your reasoning.
        """

        response = model.generate_content(prompt)
        logger.info(f"Generated response: {response.text}")
        return {"response": response.text}
    except Exception as e:
        logger.error(f"Error processing chat request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn

    logger.info("Starting the backend server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)