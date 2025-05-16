import os
import subprocess
import zipfile

def install_gdown():
    try:
        import gdown
    except ImportError:
        subprocess.run(["pip", "install", "gdown"], check=True)

def download_model():
    install_gdown()
    import gdown  # Import after installing

    url = "https://drive.google.com/uc?id=1um2ngcJ3BwSQVBmYsMceYM5IuOembqKR"
    output = "model.zip"

    print("⬇️ Downloading model...")
    gdown.download(url, output, quiet=False)

    print("📦 Extracting model...")
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("ai_code_critic_5000")
    os.remove(output)
    print("✅ Model is ready.")

if __name__ == "__main__":
    download_model()
