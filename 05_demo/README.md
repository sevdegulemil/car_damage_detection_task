# Car Damage Detection Demo

This folder contains the interactive demo for the car damage detection project.

The demo uses the trained YOLO11n model to detect two types of car damage:

- `dent`
- `scratch`

## Demo

The demo provides a simple interface where a user can upload a car image and run damage detection.

The model returns:

- Detected damage type
- Bounding boxes
- Confidence scores

## Model

- **Model:** YOLO11n
- **Image size:** 640×640
- **Confidence threshold:** 0.25
- **Classes:** `dent`, `scratch`

The trained model weights (`best.pt`) are not included in the GitHub repository because model files are excluded through `.gitignore`.

## Running the Demo

### 1. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
