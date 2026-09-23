# Dataset Preparation

This section documents the dataset collection, merging, cleaning, and restructuring process used for the car damage detection project.

## Objective

The main objective of the dataset preparation process was to create a consistent dataset for detecting two target types of car damage:

* `dent`
* `scratch`

Multiple car damage datasets were combined and cleaned because the original datasets contained different class names, damage categories, and annotation structures.

## Dataset Preparation Process

The preparation process included the following steps:

1. Collecting car damage datasets from different sources
2. Inspecting the original class structures
3. Combining the datasets
4. Reviewing and consolidating similar damage classes
5. Removing classes that were outside the project scope
6. Creating the final two-class structure:

   * `dent`
   * `scratch`
7. Checking the resulting dataset and annotations
8. Splitting the dataset into train, validation, and test sets

## Final Dataset

The final dataset contains:

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

## Class Structure

The final dataset uses only two classes:

```text
0 → dent
1 → scratch
```

The class structure was standardized so that the supervised detection experiments could use the same target classes.

## Dataset Configuration

The final YOLO dataset uses the following structure:

```text
dataset/
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

The `data.yaml` file defines the two target classes:

```yaml
nc: 2
names: ['dent', 'scratch']
```

## Dataset Details

More detailed information about the source datasets, class structure, cleaning process, and final dataset configuration is documented in:

`dataset_info.md`
