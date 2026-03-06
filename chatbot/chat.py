import os
import google.genai as genai


api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set!")


client = genai.Client(api_key=api_key)


user_question = input("Ask me anything: ")


response = client.models.generate_content(
    model="gemini-2.5-flash",  
    contents=f"You are a helpful and accurate assistant. Answer this question truthfully:\n{user_question}"
)


print("\nAnswer:")
print(response.text)