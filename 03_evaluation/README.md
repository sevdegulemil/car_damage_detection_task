# Model Evaluation

This section contains the evaluation results of the trained YOLO models on the test set.

The purpose of this section is to evaluate the trained models on unseen data and compare their detection performance.

## Test Dataset

The test set contains:

- 2,042 images
- 3,741 annotated instances
- 2 classes: `dent`, `scratch`
- Image size: 640×640

The test set was not used during model training.

## Evaluation Results

The test results of the YOLO experiments are summarized in:

`model_comparison.md`

## Evaluation Outputs

This section contains:

- Test metrics
- Confusion matrices
- Precision-recall curves
- Model comparison

### Confusion Matrices

The generated confusion matrices are stored in:

`confusion_matrices/`

The folder contains both standard and normalized confusion matrices for the evaluated models.

## Models Evaluated

The following models are included in the evaluation:

- YOLOv8n
- YOLO11n
- YOLO11s

## Notes

YOLO11n and YOLO11s were trained using the final cleaned dataset.

The YOLOv8n model was originally trained using an earlier version of the dataset and was later evaluated on the final test set as a baseline/reference.

Therefore, the three models should not be interpreted as a strictly controlled benchmark using identical training-data conditions.
