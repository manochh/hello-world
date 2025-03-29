from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyA-cfen178XmdCF-5ynE8dJu2bjNSzDB3w")

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=(
        "Generate a story about a cute baby turtle in a 3d digital art style. "
        "For each scene, generate an image."
    ),
    config=types.GenerateContentConfig(
        response_modalities=["Text", "Image"]
    ),
)