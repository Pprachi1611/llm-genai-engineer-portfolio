import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"



def build_prompt(mode, user_input):
    if mode == "1":
        return f"You are a helpful tutor. Explain simply with examples:\n{user_input}"
    elif mode == "2":
        return f"Summarize this in simple words:\n{user_input}"
    elif mode == "3":
        return f"Convert this into clean bullet-point notes:\n{user_input}"
    else:
        return user_input



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
    print("AI Study Helper (CLI)")
    print("Type 'exit' anytime to quit\n")

    while True:
        print("\nChoose Mode:")
        print("1 → Explain")
        print("2 → Summarize")
        print("3 → Generate Notes")

        mode = input("Enter choice: ").strip()

        if mode.lower() == "exit":
            print("Goodbye ")
            break

        if mode not in ["1", "2", "3"]:
            print(" Invalid choice")
            continue

        user_input = input("\nAsk something: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye ")
            break

        prompt = build_prompt(mode, user_input)
        answer = ask_ai(prompt)

        print("\n AI Response:\n")
        print(answer)


if __name__ == "__main__":
    main()