# Car Damage Detection Demo

This folder contains the interactive demo for the car damage detection project.

The demo uses the trained YOLO11n model to detect two types of car damage:

* `dent`
* `scratch`

## Demo

### Live Demo

[Open the Car Damage Detection Demo](https://cardamagedetectiontask-f9lgzuumacpydyk5hf3zdp.streamlit.app/)

The demo provides a simple interface where a user can upload a car image and run damage detection.

The model returns:

* Detected damage type
* Bounding boxes
* Confidence scores

## Model

* **Model:** YOLO11n
* **Image size:** 640×640
* **Confidence threshold:** 0.25
* **Classes:** `dent`, `scratch`

The trained model weights (`best.pt`) are stored separately in the public Hugging Face model repository:

`seemil/car-damage-yolo11n`

The GitHub repository does not contain the model weights.

During deployment, the Streamlit application downloads the model automatically from Hugging Face.

## Running the Demo

### Install Dependencies

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Local Model

For local development, the application can use a local `best.pt` file if it is placed inside the `04_demo` directory.

If the local model file is not available, the application automatically downloads the model from Hugging Face.

### Start the Application

From the project root:

```bash
python -m streamlit run 04_demo/app.py
```

The application will open in the browser.

## Usage

1. Upload a car image.
2. Click **Detect Damage**.
3. The YOLO11n model analyzes the image.
4. Detected damage is displayed with bounding boxes and confidence scores.

If no damage is detected, the application displays:

> No damage detected.

## Deployment

The demo is deployed using Streamlit Community Cloud.

The application code is hosted on GitHub, while the trained model weights are hosted separately on Hugging Face.

```text
GitHub
├── 04_demo/
│   └── app.py
└── requirements.txt

Hugging Face
└── best.pt

Streamlit Cloud
└── Downloads best.pt automatically
```

## Note

This demo is intended to demonstrate the trained model's inference process. The demo output should not be interpreted as a guarantee of damage detection accuracy for real-world vehicle inspection.
