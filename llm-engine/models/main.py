# main.py
from dataRetrieval import fetch_drive_files
from llama3 import train_model

def main():
    print("Fetching data from Google Drive...")
    files = fetch_drive_files()

    if files:
        print("Training model with retrieved data...")
        model_name = train_model(files)
        print(f"Model '{model_name}' is ready to use!")

if __name__ == "__main__":
    main()