\# Computer Vision App — OpenCV + DeepFace



Satisfies roadmap requirement: Computer Vision with OpenCV and DeepFace.



\## Stack

OpenCV, DeepFace, TensorFlow — run on Google Colab (local install was too slow on this machine; pivoted per the plan's backup strategy)



\## What it does

1\. OpenCV: detects a face in an uploaded image using a Haar Cascade classifier, draws a bounding box, saves the output

2\. DeepFace: analyzes the detected face for age, gender, and emotion using pre-trained deep learning models



\## How to run

Open cv\_deepface\_app.ipynb in Google Colab, upload a face image as face\_image.jpeg, run all cells.



\## What I learned

\- OpenCV stores images in BGR, not RGB - requires explicit color conversion

\- Haar Cascades: classical face detection using grayscale brightness patterns

\- DeepFace uses real deep neural networks (not classical CV) for higher-level facial analysis

\- When a local install is too slow/unreliable, pivoting to Colab is a legitimate engineering decision, not a shortcut



\## Limitations

\- Single static image only, no webcam/video support

\- Local install never completed - all testing done on Colab

