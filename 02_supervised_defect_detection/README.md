# Supervised Defect Detection

This section contains the supervised object detection experiments performed for car damage detection.

The main objective was to detect two types of vehicle damage:

- `dent`
- `scratch`

## Dataset

The final cleaned dataset contains:

- Train: 16,331 images
- Validation: 2,041 images
- Test: 2,042 images
- Total: 20,414 images
- Classes: `dent`, `scratch`

The dataset was prepared by combining and cleaning multiple car damage datasets.

Detailed dataset preparation is documented in:

`../01_dataset_preparation/`

## Experiments

Three YOLO experiments were performed during the project.

### YOLOv8n Baseline

The first experiment was used as the baseline.

It was trained using an earlier version of the merged dataset before the final dataset cleaning process.

Details:

`01_yolov8n_baseline/README.md`

### YOLO11n

YOLO11n was trained using the final cleaned dataset containing the two target classes.

Details:

`02_yolov11n/README.md`

### YOLO11s

YOLO11s was also trained using the final cleaned dataset.

Details:

`03_yolov11s/README.md`

## Evaluation

After training, the best weights from the experiments were evaluated separately on the unseen test set.

The test set contains 2,042 images.

Test evaluation results and model comparisons are documented separately in:

`../03_evaluation/`

This section includes:

- Test metrics
- Confusion matrices
- Precision-recall curves
- Model comparison

## Experiment Structure

```text
02_supervised_defect_detection/
│
├── README.md
│
├── 01_yolov8n_baseline/
│   └── README.md
│
├── 02_yolov11n/
│   └── README.md
│
└── 03_yolov11s/
    └── README.md
