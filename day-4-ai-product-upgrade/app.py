import requests
import os
from dotenv import load_dotenv
from prompts import get_prompt

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Request failed: {e}"


def main():
    print("\n AI STUDY ASSISTANT (Day 4)")
    print("Type '4' to exit\n")

    while True:
        print("\n=== MENU ===")
        print("1. Explain")
        print("2. Summarize")
        print("3. Quiz Generator")
        print("4. Exit")

        mode = input("\nChoose option: ").strip()

        if mode == "4":
            print("Goodbye ")
            break

        if mode not in ["1", "2", "3"]:
            print(" Invalid option. Try again.")
            continue

        text = input("\nEnter topic/text: ").strip()

        if text.lower() == "exit":
            print("Goodbye ")
            break

        prompt = get_prompt(mode, text)
        answer = ask_ai(prompt)

        print("\n AI RESPONSE:\n")
        print(answer)
        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()