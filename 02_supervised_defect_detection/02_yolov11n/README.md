# YOLO11n

This experiment was performed using the cleaned car damage dataset.

## Model

- Model: YOLO11n
- Epochs: 50
- Image size: 640×640
- Batch size: Auto
- Pretrained: Yes
- Optimizer: Auto

## Dataset

The model was trained using the cleaned vehicle damage dataset containing two classes:

- `dent`
- `scratch`

Dataset configuration:

`merged-car-defect_datasets_2`  
https://app.roboflow.com/sevde-gul-emil/merged-car-defect_datasets_2/1

## Purpose

This experiment was performed to evaluate YOLO11n on the cleaned dataset and compare its performance with the YOLOv8n baseline.

YOLO11n was selected as a lightweight model for detecting small vehicle dents and scratches.

## Validation Results

The following values are from the validation results at the end of the 50-epoch training run.

| Metric | Result |
|---|---:|
| Precision | 60.48% |
| Recall | 45.12% |
| mAP50 | 47.61% |
| mAP50-95 | 27.84% |

The training and validation results are included in the `results` folder.

## Test Evaluation

After training, the best model weights were evaluated separately on the test set.

- Test images: 2,042
- Image size: 640×640
- Model weights: `best.pt`

Test evaluation results are documented separately in:

`03_evaluation/`

The test outputs include confusion matrices, precision-recall curves, and sample predictions.
