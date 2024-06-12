import os
import json

if __name__ == "__main__":
    data_path = "data/vi_sharegpt4v.json"
    image_folder = "data/images"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File {data_path} not found")

    with open(data_path, "r") as f:
        data = json.load(f)

    for idx, conv in enumerate(data):
        image = conv["image"]
        image_path = os.path.join(image_folder, image)

        if not os.path.exists(image_path):
            print(f"Image {image_path} not found in conversation {idx}")