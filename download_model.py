import os
import subprocess

def download_model():
    url = "https://drive.google.com/uc?id=1um2ngcJ3BwSQVBmYsMceYM5IuOembqKR"
    output = "model.zip"

    print("⬇️ Downloading model zip from Google Drive...")
    try:
        subprocess.run(["wget", url, "-O", output], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to download model from Google Drive.")
        return

    print("📦 Extracting model...")
    try:
        subprocess.run(["unzip", "-o", output, "-d", "ai_code_critic_5000"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to unzip model archive.")
        return

    os.remove(output)
    print("✅ Model ready.")

if __name__ == "__main__":
    download_model()
