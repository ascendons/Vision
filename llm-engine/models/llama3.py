import os
import ollama

def train_model(file_paths):
    """Train an Ollama model using text data from valid files."""
    combined_text = ""

    for file_path in file_paths:
        if os.path.isfile(file_path):  # Check if it's a valid file
            with open(file_path, "r", encoding="utf-8") as f:
                combined_text += f.read() + "\n"
        else:
            print(f"Skipping invalid file path: {file_path}")

    if not combined_text:
        raise ValueError("No valid text data found for training.")

    # Define Ollama training parameters
    model_name = "custom-ollama-model"
    # ollama.create(model_name, {"data": combined_text})
    ollama.create(
        model=model_name,
        from_="mistral",
        adapters={"custom-data": combined_text}  # Add your data file
    )
    # ollama.create(model="test-model", modelfile="FROM mistral\n\nThis is a test.")

    print(f"Model '{model_name}' trained successfully!")
    return model_name