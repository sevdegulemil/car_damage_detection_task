# Dataset Information

The dataset used in this project was created by combining and cleaning multiple car damage datasets.

## Source Datasets

The following datasets were used as sources during the dataset preparation process:

* [Merged-Car-Defect_datasets-1](https://app.roboflow.com/sevde-gul-emil/merged-car-defect_datasets/1)
* [Car_Dent_Scratch_Detection(1) Computer Vision Model](https://universe.roboflow.com/sindhu/car_dent_scratch_detection-1)

The source datasets contained different class names and damage categories. These datasets were reviewed, combined, and cleaned according to the scope of the project.

## Dataset Preparation

The main preparation steps were:

* Combining multiple car damage datasets
* Reviewing the original class structure
* Removing classes outside the project scope
* Consolidating relevant classes
* Standardizing the labels into two target classes:

  * `dent`
  * `scratch`
* Creating the final train, validation, and test splits

## Final Dataset

The final cleaned dataset contains:

| Split      |     Images |
| ---------- | ---------: |
| Train      |     16,331 |
| Validation |      2,041 |
| Test       |      2,042 |
| **Total**  | **20,414** |

The dataset contains **40,616 annotated instances**:

| Class     | Annotations |
| --------- | ----------: |
| `dent`    |      15,395 |
| `scratch` |      25,221 |
| **Total** |  **40,616** |

### Final Classes

```text
0 → dent
1 → scratch
```

## Final Roboflow Dataset

The cleaned and combined dataset was maintained as:

[merged-car-defect_datasets_2](https://app.roboflow.com/sevde-gul-emil/merged-car-defect_datasets_2/1)

This final dataset was used for the YOLO11n and YOLO11s training experiments.
