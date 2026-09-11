# Dataset Card: **finetuning_test - aubaac_step_test**
---

## Dataset Overview
> **Dataset Description**  
> The aim of this Dataset is to test the few-shot finetuning performance of a well perfoming, generalistic screw detection model on a specific domain / task
> Specificly, this dataset is used to find the optimal number of optimization steps for few-shot finetuning
> For this purpose, the Dataset contains 10 images in the train set and a larger amount in the val set, to find where the model starts overfitting

---

## Dataset Summary
- **Total number of images:** 25

- **Split distribution:**
  - **Training images:** 10
  - **Validation images:** 15
  - **Test images:** 0

- **Data type:**
  RGB images, YOLO annotation format

---

## Classes
- **Number of classes:** 1
- **Class names:**
  - screw (id: 0)

---

## Additional Notes (Optional)
- This dataset version was built automatically.
- Ensure class mappings are consistent across all sources.
- Add known limitations or biases here.



