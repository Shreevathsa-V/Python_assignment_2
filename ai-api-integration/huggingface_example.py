import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://router.huggingface.co/v1/chat/completions"


def query_huggingface(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {"role": "system", "content": "Give direct answers only. Do not include reasoning."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 100,
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return f"HTTP {response.status_code}: {response.text}"

        data = response.json()

        # Case 1: Standard OpenAI format
        if "choices" in data:
            message = data["choices"][0].get("message", {})

            # Try content first
            content = message.get("content", "").strip()

            # If content is empty, use reasoning
            if not content:
                content = message.get("reasoning", "").strip()

            # Final fallback
            if not content:
                return "No usable response generated."

            return content

        # Case 2: Some models return 'text'
        if "choices" in data and "text" in data["choices"][0]:
            return data["choices"][0]["text"]

        # Case 3: Direct text response
        if "text" in data:
            return data["text"]

        # Case 4: fallback → show raw
        return f"No proper content. Raw response:\n{data}"

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("=== Hugging Face API ===")

    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Hugging Face...\n")

    result = query_huggingface(user_prompt)

    print("Response:\n")
    print(result)