# Model Comparison

This document summarizes the test-set performance of the YOLO models used in the project.

## Test Dataset

The test set contains:

- 2,042 images
- 3,741 annotated instances
- 2 classes: `dent`, `scratch`
- Image size: 640×640

The test set was not used during model training.

## Test Results

| Model | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| YOLOv8n | 20.88% | 14.89% | 11.03% | 5.79% |
| YOLO11n | 72.39% | 53.59% | 60.44% | 36.31% |
| YOLO11s | 72.45% | 51.77% | 59.03% | 35.50% |

## Dataset Difference

The YOLO11n and YOLO11s models were trained using the final cleaned dataset containing the two target classes:

- `dent`
- `scratch`

The YOLOv8n model was originally trained as a baseline using an earlier version of the merged dataset, before the final dataset cleaning and restructuring process.

Therefore, the YOLOv8n result should be interpreted as a **baseline/reference result** rather than as a strictly controlled comparison under identical training-data conditions.

## Class-Level Results

### YOLOv8n

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| dent | 5.07% | 5.80% | 1.43% | 0.40% |
| scratch | 36.69% | 23.97% | 20.63% | 11.18% |

### YOLO11n

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| dent | 75.44% | 68.08% | 74.08% | 45.34% |
| scratch | 69.34% | 39.10% | 46.80% | 27.28% |

### YOLO11s

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| dent | 73.97% | 65.36% | 71.56% | 42.96% |
| scratch | 70.93% | 38.18% | 46.50% | 28.03% |

## Interpretation

The test results show that the two YOLO11 experiments achieved substantially higher detection metrics on the cleaned dataset than the earlier YOLOv8n baseline.

For the YOLO11 experiments, dent detection produced higher recall and mAP values than scratch detection. This indicates that scratch detection remained a more challenging part of the task.

YOLO11n and YOLO11s were trained under the same dataset configuration and can therefore be compared directly within the cleaned-dataset experiments.

The results should be interpreted together with the dataset difference described above rather than as a controlled three-model benchmark.

## Evaluation Outputs

The generated evaluation outputs are organized as follows:

```text
03_evaluation/
├── README.md
├── model_comparison.md
└── confusion_matrices/
