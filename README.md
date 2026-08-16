# Artificail Intelligence in Predicting Toothwear Using Deep Learning

An AI-based computer vision pipeline for automated detection and analysis of **Non-Carious Cervical Lesions (NCCL)** using tooth segmentation, image classification, lesion localization, and web-based visualization.

## Overview

Non-Carious Cervical Lesions (NCCLs) involve structural loss around the cervical region of a tooth. Early identification is important to help prevent further dental damage and support treatment planning.

Traditional assessment mainly relies on manual visual examination, which can be time-consuming and may vary between observers. Small lesion regions can also be difficult to identify in dental images with variations in image quality, lighting, tooth orientation, and surrounding structures.

To address these challenges, I developed a **multi-stage deep learning pipeline** that processes a dental image through three main stages:

- **YOLOv8s-seg** for individual tooth segmentation
- **ResNet50** for NCCL vs Normal classification
- **YOLOv5** for NCCL lesion localization

A **Flask-based web application** was also developed to visualize the model predictions.

The overall workflow is:

**Dental Image → Tooth Segmentation → Tooth Classification → Lesion Localization → Visualization**

---

## Problem Statement

Automated analysis of dental images presents several challenges:

- Manual identification can be time-consuming and subjective.
- Small or early-stage lesions can be difficult to identify visually.
- Dental images can vary in quality and appearance.
- Precise lesion localization is challenging.
- Background regions in complete dental images can interfere with classification.

The project therefore focuses on separating these tasks into individual stages rather than attempting to perform the complete analysis using a single model.

---

## Project Objectives

- Prepare and annotate dental images containing NCCL and normal tooth conditions.
- Segment individual teeth from dental images using YOLOv8s-seg.
- Classify segmented teeth as **NCCL** or **Normal** using ResNet50.
- Localize NCCL lesion regions using YOLOv5.
- Develop a Flask-based interface to visualize the predictions.

---

## Approach

```text
The project follows a multi-stage pipeline:

                    Dental Image
                         │
                         ▼
               Image Preprocessing
                         │
                         ▼
                 YOLOv8s-seg
               Tooth Segmentation
                         │
                         ▼
                Individual Tooth
                     Crops
                         │
                 ┌───────┴───────┐
                 ▼               ▼
             ResNet50          YOLOv5
          Classification    Lesion Localization
                 │               │
                 ▼               ▼
           NCCL / Normal     Lesion Region
                 │               │
                 └───────┬───────┘
                         ▼
                Diagnostic Output
                         │
                         ▼
                    Flask App
```

The main idea is to first isolate the relevant tooth region and then perform classification and lesion localization on the segmented tooth images.

In simple terms:

**YOLOv8s-seg → finds the tooth**
**ResNet50 → classifies the tooth**
**YOLOv5 → locates the lesion**

---

## Dataset

Approximately **270 dental images** were collected for the project, including images containing NCCL and normal tooth conditions.

- 270 original dental images
- Dataset preparation and annotation performed using **Roboflow**

The original images were processed to generate individual tooth regions for the classification and lesion-localization stages.

---

## Data Preparation

Individual teeth were annotated using polygon-based instance segmentation annotations for the YOLOv8 segmentation stage.

The segmented tooth images were then categorized into two classes:

- **NCCL**
- **Normal**

A total of **873 segmented tooth images** were generated for classification dataset preparation.

After augmentation, the classification dataset contained:

- **2,233 training images**
- **800 testing images**, with 400 NCCL and 400 Normal images

For lesion localization, polygon annotations were created around the NCCL regions. A total of **493 annotated tooth images** were prepared, consisting of:

- 345 training images
- 49 validation images
- 99 testing images

Data augmentation was also applied to increase image diversity and improve model robustness.

---

## Tooth Segmentation

### YOLOv8s-seg

YOLOv8s-seg was used to identify individual teeth within the dental images.

The predicted segmentation masks were used to generate tighter tooth crops. This helped reduce irrelevant background information and provided more focused inputs for the classification and lesion-localization stages.

The segmentation model achieved approximately **90% mAP@50** and successfully generated individual tooth regions for further analysis.

---

## NCCL Classification

### ResNet50

The segmented tooth images were passed to a ResNet50 model for binary classification.

The model predicts whether the tooth belongs to:

- **NCCL**
- **Normal**

The use of segmented tooth regions allows the classifier to focus on the tooth morphology and potential lesion characteristics rather than the surrounding image.

The model achieved approximately **90% classification accuracy** on the test set.

From the 800 test images:

- 360 NCCL images were correctly classified.
- 360 Normal images were correctly classified.
- 40 NCCL images were classified as Normal.
- 40 Normal images were classified as NCCL.

---

## Lesion Localization

### YOLOv5

Classification determines whether a tooth is predicted as NCCL or Normal, but it does not indicate where the lesion is located.

To provide lesion-level information, a separate YOLOv5 model was trained using polygon annotations around the NCCL regions.

The model was used to identify the suspected lesion region and provide confidence-based localization.

The lesion-localization stage achieved approximately **87.5% localization performance**, with stable precision and recall across confidence thresholds and a maximum F1-score of approximately **0.88**.

---

## Web-Based Diagnostic System

A **Flask-based web application** was developed to bring the trained models together into an interactive interface.

The application allows a user to:

- Upload a dental image
- Process the image through the trained models
- Identify individual teeth
- Predict NCCL or Normal
- Localize suspected lesion regions
- Display prediction confidence and visual results

This provides a simple interface for demonstrating the outputs of the complete AI pipeline.

---

## Results

The developed system produced the following overall results:

| Task                | Model       |        Result |
| ------------------- | ----------- | ------------: |
| Tooth Segmentation  | YOLOv8s-seg |   ~90% mAP@50 |
| NCCL Classification | ResNet50    | ~90% Accuracy |
| Lesion Localization | YOLOv5      |        ~87.5% |

The results demonstrate the feasibility of combining segmentation, classification, and lesion localization into a single dental image analysis pipeline.

---

## Technologies Used

- **Python**
- **YOLOv8 / Ultralytics**
- **YOLOv5**
- **ResNet50**
- **TensorFlow / Keras**
- **PyTorch**
- **OpenCV**
- **Roboflow**
- **Scikit-learn**
- **Matplotlib**
- **Flask**

---

## Limitations

- The dataset size was relatively limited.
- Dental images showed variations in quality and appearance.
- Model performance depends on annotation quality.
- Errors during tooth segmentation can affect downstream classification.
- GPU resources are required for efficient model training.
- The reported results demonstrate technical feasibility and should not be considered clinical validation.

This project is therefore intended as a **research and prototype system**, not as a replacement for professional dental diagnosis.

---

## Future Work

- Increase the dataset size using larger clinical datasets.
- Improve tooth and lesion segmentation to reduce error propagation between stages.
- Improve real-time diagnostic performance.
- Explore mobile or cloud-based deployment.
- Extend the framework to additional dental conditions.
- Incorporate explainable AI techniques.
- Evaluate the models on larger and more diverse external datasets.

---

## Conclusion

This project developed a multi-stage deep learning framework for automated NCCL analysis from dental images.

**YOLOv8s-seg** was used to identify and extract individual teeth, **ResNet50** classified the segmented teeth into NCCL and Normal categories, and **YOLOv5** localized suspected lesion regions.

The system achieved approximately **90% classification accuracy**, **90% mAP@50 for tooth segmentation**, and **87.5% lesion localization performance**.

The trained models were also integrated into a Flask-based interface to provide an interactive way of viewing predictions, confidence scores, and lesion locations.

Overall, the project demonstrates the application of deep learning and computer vision to a multi-stage dental image analysis problem, combining **segmentation, classification, localization, and deployment** in a single workflow.

---

## Disclaimer

This project is intended for **research and educational purposes**. Model predictions should not be interpreted as a substitute for professional dental examination or clinical diagnosis.
