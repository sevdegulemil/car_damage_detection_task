# YOLOv8n Baseline

This experiment was used as the baseline for car damage detection.

## Model

- Model: YOLOv8n
- Epochs: 50
- Image size: 640×640
- Batch size: 16
- Pretrained: Yes
- Optimizer: Auto

## Dataset

The model was trained using the earlier merged vehicle damage dataset:

`Merged-Car-Defect_datasets-1`  
https://app.roboflow.com/sevde-gul-emil/merged-car-defect_datasets/1

This was the dataset used before the later cleaning and restructuring process.

## Purpose

The baseline was created to establish an initial reference point before experimenting with newer YOLO models and the cleaned dataset.

## Validation Results

The following values are from the validation results of the original training run.

| Metric | Result |
|---|---:|
| Precision | 53.21% |
| Recall | 35.81% |
| mAP50 | 38.04% |
| mAP50-95 | 21.56% |

The original training results and evaluation plots are included in the `results` folder.

## Test Evaluation

After training, the best model weights were evaluated separately on the test set.

- Test images: 2,042
- Image size: 640×640
- Model weights: `best.pt`

Test evaluation results are documented separately in:

`03_evaluation/`

The test outputs include confusion matrices, precision-recall curves, and sample predictions.
