# Car Damage Detection

An image-based car damage detection project developed as part of an internship.

The project focuses on detecting two types of exterior car damage:

* `dent`
* `scratch`

The main goal was to investigate supervised object detection approaches for car damage analysis, with particular attention to small and subtle damage.

## 🚗 Live Demo

[Open the Car Damage Detection Demo](https://cardamagedetectiontask-f9lgzuumacpydyk5hf3zdp.streamlit.app/)

The interactive demo allows users to upload a car image and view detected dents and scratches with bounding boxes and confidence scores.

## Project Overview

The project consists of several stages:

1. Dataset collection and cleaning
2. Class consolidation and dataset preparation
3. Supervised object detection experiments
4. Test-set evaluation
5. Interactive model demonstration

## 📊 Dataset Preparation

Multiple car damage datasets were combined and cleaned to create a dataset focused on two target classes:

* `dent`
* `scratch`

Final dataset:

| Split      |     Images |
| ---------- | ---------: |
| Train      |     16,331 |
| Validation |      2,041 |
| Test       |      2,042 |
| **Total**  | **20,414** |

The dataset contains **40,616 annotated instances**:

* Dent: 15,395
* Scratch: 25,221

Detailed dataset preparation is documented in:

`01_dataset_preparation/`

## 🤖 Supervised Defect Detection

YOLO-based object detection models were investigated for supervised car damage detection.

The experiments include:

* YOLOv8n baseline
* YOLO11n
* YOLO11s

YOLO11n and YOLO11s were trained using the final cleaned dataset.

The YOLOv8n model was originally trained using an earlier version of the dataset and was later evaluated on the final test set as a baseline/reference.

Detailed experiment information:

`02_supervised_defect_detection/`

## 📈 Model Evaluation

The trained models were evaluated separately on the unseen test set containing 2,042 images.

The evaluation includes:

* Precision
* Recall
* mAP50
* mAP50-95
* Confusion matrices
* Precision-recall curves
* Model comparison

Detailed results:

`03_evaluation/`

## 🖥️ Demo

The project includes an interactive Streamlit application.

The demo uses the trained YOLO11n model to detect:

* Dents
* Scratches

Users can upload a car image and view the model's predictions directly in the browser.

The trained model weights are hosted separately on Hugging Face, while the application code is maintained in this repository.

Demo details:

`04_demo/`

## 📁 Project Structure

```text
car_damage_detection_task/
│
├── 01_dataset_preparation/
│
├── 02_supervised_defect_detection/
│   ├── 01_yolov8n_baseline/
│   ├── 02_yolov11n/
│   └── 03_yolov11s/
│
├── 03_evaluation/
│   └── confusion_matrices/
│
├── 04_demo/
│   ├── app.py
│   └── README.md
│
├── docs/
│   └── internship_report.pdf
│
├── requirements.txt
├── runtime.txt
└── README.md
```

## 🛠️ Technologies

* Python
* Ultralytics YOLO
* PyTorch
* OpenCV
* Roboflow
* Streamlit
* Hugging Face

## 📄 Internship Report

The detailed internship report is available in:

`docs/internship_report.pdf`

## ⚠️ Note

This project is an internship research and development study.

The demo demonstrates model inference and should not be interpreted as a guarantee of damage detection accuracy for real-world car inspection.
