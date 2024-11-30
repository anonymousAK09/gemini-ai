import os
import time
from tqdm import tqdm
from google.ai.language import LanguageServiceClient

def display_loading_animation():
    for _ in tqdm(range(10), desc="Setting up...", ascii=False):
        time.sleep(0.2)

def main():
    print("Welcome to Gemini AI!")
    print("By anonymousAK09")

    display_loading_animation()

    # Get API key from user
    api_key = input("Enter your API key: ")

    # Set API key as environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/api_key.json"

    # Create a LanguageServiceClient instance
    client = LanguageServiceClient()

    print("Setup complete!")

    while True:
        prompt = input("Enter your prompt: ")
        if prompt == "exit":
            break

        # Generate text using the model
        response = client.generate_text(
            request={
                "prompt": prompt,
                "model": "text-davinci-003",  # Replace with the appropriate model
            }
        )

        print(response.text)

if __name__ == "__main__":
    main()
