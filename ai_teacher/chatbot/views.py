from django.shortcuts import render
from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os

def home(request):
    load_dotenv(override=True)
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)
    
    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=question
            )
            answer = response.text
        except Exception as e:
            error_str = str(e).lower()
            if "leaked" in error_str or "permission_denied" in error_str or "403" in error_str:
                answer = f"Error: The API key is invalid or leaked. (Key starts with: {api_key[:8]}...). Please ensure you have updated the .env file in d:/chatbot/ai_teacher/.env with a valid key."
            elif "429" in error_str or "resource_exhausted" in error_str:
                answer = "Error: You have reached the Gemini API rate limit or quota. Please wait about 30-60 seconds before trying again. If you just created this key, it might take a minute to fully activate."
            else:
                answer = f"An error occurred: {str(e)}"

    return render(request, "index.html", {"answer": answer})
