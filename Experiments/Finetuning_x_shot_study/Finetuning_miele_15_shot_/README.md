# Experiment Card: **Finetuning_x_shot_study** (Finetuning_miele_15_shot_)

## Overview
---
> **Model description**  
> Add a short manual description here.  
> Example: *This model performs screw detection on different images...*  

**Model Type:** Universal_screw_detection v3.7 (best.pt)  
**Experiment Group:** Finetuning_x_shot_study  
**Experiment Name:** Finetuning_miele_15_shot_  
**Created:** 2026-09-17T08:04:27.564656  
**Git Commit ID:** main @629022f  
**HPO:** No

---

## Training Procedure
### Training Procedure

| Key | Value |
|-----|-------|
| Epochs | 1000 |
| Early stopping patience | Ultralytics default |
| Batch size | 2 |
| Optimizer | AdamW |
| Learning rate | 0.005 |
| Fitness target | precision=0, recall=0, map50=0.5, map50_95=0.5 |
| Integrated Data augmentations | augmentation: Yes<br>flipud: 0.300<br>fliplr: 0.500<br>mosaic: 0.100<br>hsv_h: 0.010<br>hsv_s: 0.150<br>hsv_v: 0.150 |

---

## Dataset Information

> **Dataset description**  
> Add a short manual description here.  
> Example: *This dataset contains images and labels of various screws...*  

### Dataset Information

| Key | Value |
|-----|-------|
| dataset_name | finetuning_study/miele_15_shot |
| num_classes | 1 |
| class_names | ['screw'] |
| num_train_images | 15 |
| num_val_images | 10 |
| num_test_images | 10 |


---

## Performance Metrics

> **Evaluation**  
> Add a manual evaluation of the performance here.  
> Example: *This model has good performance for Usecase A, but for Usecase B...*  

### Performance Metrics

| Key | Value |
|-----|-------|
| precision_global | 0.811 |
| recall_global | 0.603 |
| mAP50 | 0.648 |
| mAP50-95 | 0.324 |
