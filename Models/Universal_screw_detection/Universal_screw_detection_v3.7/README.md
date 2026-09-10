# Model Card: **Universal_screw_detection** (v3.7)

## Overview
---
> **Model description**  
> Add a short manual description here.  
> Example: *This model performs screw detection on different images...*  

**Model Type:** yolo26s.pt  
**Version:** 3.7  
**Created:** 2026-09-09T15:33:55.401748  
**Git Commit ID:** main @c537889  
**HPO:** No

---

## Training Procedure
### Training Procedure

| Key | Value |
|-----|-------|
| Epochs | 800 |
| Batch size | 8 |
| Optimizer | AdamW |
| Learning rate | 0.008 |
| Fitness target | Ultralytics default |
| Integrated Data augmentations | augmentation: Yes<br>flipud: 0.200<br>fliplr: 0.500<br>mosaic: 0.200<br>mixup: 0.100<br>hsv_h: 0.010<br>hsv_s: 0.150<br>hsv_v: 0.150 |

---

## Dataset Information

> **Dataset description**  
> Add a short manual description here.  
> Example: *This dataset contains images and labels of various screws...*  

### Dataset Information

| Key | Value |
|-----|-------|
| dataset_name | igmr_universal_dataset/v4 |
| num_classes | 1 |
| class_names | ['screw'] |
| num_train_images | 90 |
| num_val_images | 24 |
| num_test_images | 40 |

## Synthetic Data

| Key | Value |
|-----|-------|
| additional_train_images | 50 |
| num_backgrounds | 83 |
| num_objects | 499 |
| generator_name | SyntheticGenerator |
| seed | None |
| min_objects_per_image | 0 |
| max_objects_per_image | 8 |
| background_source | background/images |
| object_source | objects/images |

---

## Performance Metrics

> **Evaluation**  
> Add a manual evaluation of the performance here.  
> Example: *This model has good performance for Usecase A, but for Usecase B...*  

### Performance Metrics

| Key | Value |
|-----|-------|
| precision_global | 0.889 |
| recall_global | 0.693 |
| mAP50 | 0.838 |
| mAP50-95 | 0.613 |
