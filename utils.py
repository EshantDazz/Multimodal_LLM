import os
from datetime import datetime
import uuid
import base64


async def save_uploaded_file(uploaded_file) -> str:
    # Create images directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")

    # Generate unique filename using timestamp and UUID
    timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id: str = str(uuid.uuid4())[:8]
    file_extension = os.path.splitext(uploaded_file.name)[1]
    filename: str = f"image_{timestamp}_{unique_id}{file_extension}"
    filepath: str = os.path.join("images", filename)

    # Save the file
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return filepath


async def delete_image(filepath) -> None:
    if os.path.exists(path=filepath):
        os.remove(path=filepath)
        print(f"Deleted image: {filepath}")


async def encode_image(image_path) -> str:
    with open(file=image_path, mode="rb") as image_file:
        return base64.b64encode(image_file.read()).decode(encoding="utf-8")
