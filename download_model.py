import gdown
import zipfile
import os

url = "https://drive.google.com/uc?id=1um2ngcJ3BwSQVBmYsMceYM5IuOembqKR"  # Your zipped model
output = "model.zip"

if not os.path.exists("ai_code_critic_5000"):
    print("⬇️ Downloading model...")
    gdown.download(url, output, quiet=False)

    print("📦 Extracting...")
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("ai_code_critic_5000")

    os.remove(output)
    print("✅ Model ready.")
