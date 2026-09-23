# YOLO11s

This experiment was performed using the cleaned car damage dataset.

## Model

- Model: YOLO11s
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

This experiment was performed to evaluate YOLO11s on the cleaned dataset and compare its performance with the other YOLO experiments.

YOLO11s was tested as a larger model than YOLO11n to observe its performance on the same dataset.

## Validation Results

The following values are from the validation results at the end of the 50-epoch training run.

| Metric | Result |
|---|---:|
| Precision | 62.14% |
| Recall | 42.90% |
| mAP50 | 46.39% |
| mAP50-95 | 26.63% |

The training arguments, results, and evaluation plots are included in the `results` folder.

## Test Evaluation

After training, the best model weights were evaluated separately on the test set.

- Test images: 2,042
- Image size: 640×640
- Model weights: `best.pt`

Test evaluation results are documented separately in:

`03_evaluation/`

The test outputs include confusion matrices, precision-recall curves, and sample predictions.
