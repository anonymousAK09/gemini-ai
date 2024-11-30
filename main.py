import os
import time
from tqdm import tqdm
from google.cloud import language_v1

def display_loading_animation():
    for _ in tqdm(range(10), desc="Setting up...", ascii=False):
        time.sleep(0.2)

def main():
    print("Welcome to Gemini AI!")
    print("By anonymousAK09")

    display_loading_animation()

    # Set up Google Cloud credentials (replace with your service account key path)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/service_account_key.json"

    # Create a LanguageServiceClient instance
    client = language_v1.LanguageServiceClient()

    print("Setup complete!")

    while True:
        prompt = input("Enter your prompt: ")
        if prompt == "exit":
            break

        # Generate text using the model
        response = client.analyze_sentiment(request={"document": {"content": prompt}})

        print(f"Sentiment Score: {response.document_sentiment.score}")
        print(f"Sentiment Magnitude: {response.document_sentiment.magnitude}")

if __name__ == "__main__":
    main()
