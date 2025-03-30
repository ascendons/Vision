import os
import subprocess

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

    # Define model name
    model_name = "custom-ollama-model2"

    # Use a writable directory (your project path)
    modelfile_path = os.path.expanduser("~/IdeaProjects/Vision/llm-engine/models/Modelfile")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(modelfile_path), exist_ok=True)

    # Escape double quotes in combined_text
    combined_text = combined_text.replace('"', '\\"').replace("\ufeff", "")

    # Write the model definition to a file
    with open(modelfile_path, "w", encoding="utf-8") as f:
        f.write(f"FROM llama3.2\n\nPARAMETER temperature 0\n\nSYSTEM \"\"\"\n{combined_text}\n\"\"\"")

    # Call Ollama via command-line to create the model
    try:
        subprocess.run(["ollama", "create", model_name, "-f", modelfile_path], check=True)
        print(f"Model '{model_name}' trained successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error training model: {e}")

    return model_name