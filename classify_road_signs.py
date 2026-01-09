from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from pathlib import Path
import sys


MODEL_REPO = "Panoramax/classify_nl_road_signs"
MODEL_FILE = "classify_nl_road_signs.pt"


def load_model():
    print("⬇️  Model downloaden van Hugging Face...")
    model_path = hf_hub_download(
        repo_id=MODEL_REPO,
        filename=MODEL_FILE
    )
    print(f"✅ Model geladen: {model_path}")
    return YOLO(model_path)


def classify_images(image_path: str):
    model = load_model()

    path = Path(image_path)

    if path.is_file():
        images = [path]
    elif path.is_dir():
        images = list(path.glob("*.jpg")) + list(path.glob("*.png"))
        if not images:
            raise ValueError("Geen .jpg of .png afbeeldingen gevonden.")
    else:
        raise ValueError("Ongeldig pad.")

    for img in images:
        print(f"\n📷 Afbeelding: {img}")
        results = model(img)

        for r in results:
            probs = r.probs
            class_id = probs.top1
            confidence = float(probs.top1conf)
            label = model.names[class_id]

            print(f"➡️  Voorspelling: {label}")
            print(f"📊 Confidence: {confidence:.2f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Gebruik:")
        print("  python classify_road_signs.py pad/naar/image_of_map")
        sys.exit(1)

    classify_images(sys.argv[1])

