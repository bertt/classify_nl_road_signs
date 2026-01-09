# classify_nl_road_signs

Code for testing https://huggingface.co/Panoramax/classify_nl_road_signs

Blog see https://bertt.wordpress.com/2026/01/09/classifying-dutch-road-signs-with-ai/

Instructions on Ubuntu:

1] Clone repository

```
git clone https://github.com/bertt/classify_nl_road_signs.git
cd classify_nl_road_signs
```
2] Initialize machine

```
sudo apt update
apt install python3.12-venv
sudo apt install -y libgl1
```

3] Initialize Python

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
4] Run program

```
python classify_road_signs.py ./images
⬇️  Model downloaden van Hugging Face...
✅ Model geladen: /home/bertt/.cache/huggingface/hub/models--Panoramax--classify_nl_road_signs/snapshots/0e64fb42d312ce2e87edb3291f715b7bc465b68e/classify_nl_road_signs.pt

📷 Afbeelding: images/A01-50.png

image 1/1 /home/bertt/dev/github.com/bertt/verkeersborden/images/A01-50.png: 224x224 maxspeed:50 1.00, maxspeed:50:end 0.00, maxspeed:5 0.00, maxweight 0.00, maxspeed:70 0.00, 23.9ms
Speed: 1.3ms preprocess, 23.9ms inference, 0.0ms postprocess per image at shape (1, 3, 224, 224)
➡️  Voorspelling: maxspeed:50
📊 Confidence: 1.00
```



