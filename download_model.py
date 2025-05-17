import gdown
import zipfile
import os

url = "https://drive.google.com/uc?id=19Gv03cECuir8A0TE2UcwdvRC_ujxclLg"  # model.zip
output = "model.zip"

model_folder = "ai_code_critic_5000"

if not os.path.exists(model_folder):
    print("⬇️ Downloading model...")
    gdown.download(url, output, quiet=False)

    print("📦 Extracting...")
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall()  # creates ai_code_critic_5000/

    os.remove(output)
    print("✅ Model ready.")
