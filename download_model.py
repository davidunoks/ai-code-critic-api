import gdown
import zipfile
import os

# Direct Google Drive download URL (replace with your file ID)
url = "https://drive.google.com/uc?id=1um2ngcJ3BwSQVBmYsMceYM5IuOembqKR"
zip_path = "model.zip"
model_folder = "ai_code_critic_5000"

if not os.path.exists(model_folder):
    print("⬇️ Downloading model from Google Drive...")
    gdown.download(url, zip_path, quiet=False)

    print("📦 Extracting model...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(model_folder)

    os.remove(zip_path)
    print("✅ Model downloaded and ready.")
else:
    print("✅ Model already exists. Skipping download.")
