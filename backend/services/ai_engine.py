import os
import google.generativeai as genai
from PIL import Image
import io
import json
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Load the API key from environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini Vision model (1.5 Flash is fast and cheap)
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_plant_image(image_bytes: bytes) -> dict:
    """
    Takes an image file in bytes, sends it to Gemini Vision,
    and returns structured JSON with diagnosis and treatment.
    """
    try:
        # Open the image using Pillow
        img = Image.open(io.BytesIO(image_bytes))
        
        # Create the prompt for the AI
        prompt = """
        You are an expert agricultural botanist. Analyze this plant image.
        Identify if there is a pest, disease, or nutrient deficiency.
        Return your answer STRICTLY as a JSON object with this exact format:
        {
          "disease_name": "Name of the disease or 'Healthy'",
          "confidence_score": "Estimated confidence 0-100%",
          "description": "Brief explanation of what is happening",
          "organic_treatment": "How to treat it organically",
          "chemical_treatment": "Recommended chemical fertilizer/pesticide"
        }
        """
        
        # Send the image and prompt to Gemini
        response = model.generate_content([prompt, img])
        
        # Gemini might return markdown code blocks, so we clean it up
        raw_text = response.text
        # Remove ```json and ``` if they exist
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        # Convert the string into a Python dictionary
        result_json = json.loads(raw_text.strip())
        return result_json
        
    except Exception as e:
        print(f"AI Error: {e}")
        return {"error": "Failed to analyze image. Please try another photo."}