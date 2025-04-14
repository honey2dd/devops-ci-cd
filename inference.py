import os

def fake_inference(image_path):
    print(f"Processing {image_path}...")
    print("Detected garbage: Yes" if "polluted" in image_path else "Detected garbage: No")

if __name__ == "__main__":
    image_folder = "test_images"
    images = [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png"))]

    for img in images:
        fake_inference(os.path.join(image_folder, img))
