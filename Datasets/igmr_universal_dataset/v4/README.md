# Dataset Card: **igmr_universal_dataset_v4**
---

## Dataset Overview
> **Dataset Description**  
> The aim of this Dataset is to provide a balanced and varied foundation to train universaly capable screw detection models.  
> Compared to the 'igmr_large_screw_dataset' series, the universal datasets won't contain all of the available Data, to prevent overfitting on a specific object, screw-type or scene. 
> The Datasets will contain a balanced selection of the availiable Data.  
> The core of the universal Datasets is the 'Multi_context_screw_detection' data, which contains images where every scene / object is only represented once, in contrast to the other data sources.  
> The test-images are from the 'Global_evaluation_dataset', to ensure an accurate comparison to different models.  
> Compared to the v3, this dataset does not contain domain specific data in the training split, e.g. (washing machine, mock battery, etc.), so that finetuning strategies can be tested for those domains.  

---

## Dataset Overview
> **Dataset Description**
> _Please add a short description of the dataset._

---

## Dataset Summary
- **Total number of images:** 114

- **Split distribution:**
  - **Training images:** 90
  - **Validation images:** 24
  - **Test images:** 0

- **Data type:**
  RGB images, YOLO annotation format

---

## Data Acquisition
_Describe how and with what equipment the data was collected._

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



