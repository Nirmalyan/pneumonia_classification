
# Pneumonia Classification

This repository contains code to analyze and build an end to end x-ray image classifier using pretrained convolutional neural networks (CNN).

## Problem Statement

Medical imaging is technique of creating visual depiction of the interior body parts
for medical analysis (physiology).In existing system, the patient visits a radiologist to
get a scan on the advise of his/her doctor. Then the patient waits for scan image results and
takes the hard copy back to the doctor. The doctor then analyzes the images to infer if the
patient has the disease. The drawbacks of the existing system are,

* Identifying and extracting details from the images is a tedious and repetitive task. Alot of manual work is involved.

* Even those images that are analyzed are not always accurate and are sometimes interpreted incorrectly by radiologists.

* The other challenge faced by the diagnostics industry is the shortage of radiological talent.

* Advances in imaging technology have significantly increased resolution, increasing the need for radiologists to identify more intricate and granular details.

## Data

In this study, dataset contains 5856 frontal chest X-ray images. The images in the
dataset are of varying resolutions from 714x419 to 2337x2026. There are 1583 normal case,
4273 pneumonia case images in the dataset. In this study 0 represents normal cases, 1
represents pneumonia cases.

## Methodology 

Deep learning requires large amount of unstructured data to reproduce accurate and
reliable results. Such quantity of data is not always available and varies from problem to
problem. Specifically clinical data are difficult to gather and labeling them is computationally
expensive and time-consuming process. This problem can be overcome with the help of
transfer learning. It based on the idea that knowledge acquired by learning a certain task to
can be used to solve similar ones. This project utilized the fine tuning aspect of transfer
learning using CNN. The initial layers of CNN are generally used to predict high level
features such as edges and shapes. The final layers contain weights and low level feature that
are used for classification. Thus by freezing the initial layers and training the final layers can
improve the accuracy of the classifier without the need for training through the entire layer.

## Evaluation 

Since the selected classification problem is binary (only two classes are
involved), a confusion matrix can be used as performance metric. There are other
performance metrics in addition to confusion matrix like: overall accuracy, sensitivity. F1,
area under ROC curve and specificity. At last manual interpretation of results is essential to
articulate it with the help of representations in the form of tables and figures.

## Results 

Confusion Matrix:

![alt text](https://github.com/Nirmalyan/pneumonia_classification/blob/main/screenshots/confusion-matrix.png?raw=true)

User Interface:

![alt text](https://github.com/Nirmalyan/pneumonia_classification/blob/main/screenshots/ui-prediction.png?raw=True)

Prediction:

![alt text](https://github.com/Nirmalyan/pneumonia_classification/blob/main/screenshots/user-interface.png?raw=True)

## Conclusions 

The project demonstrates how to classify positive and negative pneumonia data from
a collection of X-ray images. Even though the pneumonia class had higher
sample, the model was able to predict all the classes with overall accuracy of 97.8011 %.
Further the model does not over fit which is evident from the almost equal training and
validation loss. The architecture has generalized well and could be used to train other medical
datasets too. 

The application proves the fact that deep learning methods are effective in automating the
diagnostic process and providing effective treatment. This does not eliminate the diagnostic
process of a single doctor rather supports his/her by acting as a confirmation system. The
platform can act as initial decision maker which enables the doctor to treat the patient more
effectively. This mutual existence greatly reduces human as well as computer error at the
same time.