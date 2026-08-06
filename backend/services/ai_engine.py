import os
import google.generativeai as genai
from PIL import Image
import io
import json
import re
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Load the API key from environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_best_model():
    """
    Automatically finds a working Gemini model available on this API key.
    """
    try:
        # Get a list of all models available for this API key
        available_models = genai.list_models()
        
        # Look for a 1.5 flash model first (fastest)
        for m in available_models:
            if 'generateContent' in m.supported_generation_methods:
                if 'flash' in m.name.lower():
                    print(f"Found working model: {m.name}")
                    return genai.GenerativeModel(m.name)
                    
        # Fallback to pro if flash isn't found
        for m in available_models:
            if 'generateContent' in m.supported_generation_methods:
                if 'pro' in m.name.lower():
                    print(f"Found working model: {m.name}")
                    return genai.GenerativeModel(m.name)
                    
    except Exception as e:
        print(f"Error listing models: {e}")
        
    # Absolute fallback
    return genai.GenerativeModel('gemini-1.5-flash')

# Initialize the best model automatically
model = get_best_model()

def analyze_plant_image(image_bytes: bytes) -> dict:
    try:
        # Open the image using Pillow
        img = Image.open(io.BytesIO(image_bytes))
        
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
        Do not include any other text before or after the JSON.
        """
        
        response = model.generate_content([prompt, img])
        raw_text = response.text
        
        # Use Regex to extract ONLY the JSON part { ... }
        json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        
        if json_match:
            json_str = json_match.group(0)
            result_json = json.loads(json_str)
            return result_json
        else:
            return {
                "disease_name": "Unknown",
                "confidence_score": "N/A",
                "description": "The AI could not process the image clearly. Please try a closer, clearer photo.",
                "organic_treatment": "N/A",
                "chemical_treatment": "N/A"
            }
        
    except Exception as e:
        print(f"AI Error: {e}")
        return {
            "disease_name": "Unknown",
            "confidence_score": "N/A",
            "description": f"An error occurred: {str(e)}",
            "organic_treatment": "N/A",
            "chemical_treatment": "N/A"
        }