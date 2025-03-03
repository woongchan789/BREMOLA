## 🚗 BREMOLA: No-Reference Image Quality Assessment for Autonomous Driving

## 📌 Overview
This repository provides the implementation of **BREMOLA** (Blind/Referenceless Model via Moving Spectrum and Laplacian Filter), a **No-Reference Image Quality Assessment (NR-IQA)** method tailored for **autonomous driving environments**. BREMOLA is designed to accurately assess image quality degradation, particularly **blur**, in real-time driving scenarios by leveraging a **Fourier transform-based shifted spectrum** and **Laplacian filter for edge detection**.

## 📰 Paper
- **Title**: No-Reference Image Quality Assessment with Moving Spectrum and Laplacian Filter for Autonomous Driving Environment
- **Authors**: Woongchan Nam, Taehyun Youn, Chunghun Ha
- **Published in**: *Vehicles* (MDPI, 2025)
- **DOI**: [10.3390/vehicles7010008](https://doi.org/10.3390/vehicles7010008)

## 🏆 Key Features
- **No-Reference IQA**: Evaluates image quality without needing a reference image.
- **Real-Time Adaptability**: Designed for rapidly changing autonomous driving environments.
- **Fourier Transform-based Shifted Spectrum**: Quantifies image sharpness loss due to blur.
- **Laplacian Filter Compensation**: Reduces metric variance caused by environmental complexity.
- **Robust to Driving Conditions**: Tested on images from diverse locations (Dubai, Los Angeles, San Francisco, Seoul).

## 📊 Experimental Results
BREMOLA demonstrates **higher reliability and accuracy** in detecting blur degradation compared to traditional IQA metrics such as:
- **PSNR (Peak Signal-to-Noise Ratio)**
- **SSIM (Structural Similarity Index)**
- **GMSD (Gradient Magnitude Similarity Deviation)**
- **BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator)**

| Method  | Performance on Driving Images |
|---------|-------------------------------|
| **BREMOLA**  | ✅ Stable, accurate, and robust |
| PSNR    | ❌ Sensitive to noise, low robustness |
| SSIM    | ❌ Requires reference images |
| GMSD    | ❌ Unstable for varying conditions |
| BRISQUE | ❌ High variance in real-world driving |

## 📂 Dataset
The dataset consists of **real-world driving images** from various sources, covering:
- **Different times of day**
- **Urban and highway scenarios**
- **Diverse environmental factors (buildings, vehicles, pedestrians, lighting conditions)**

For privacy reasons, we do not provide the dataset here, but you can use publicly available driving footage from platforms like YouTube.

## 📌 Applications
- **Autonomous Vehicle Safety Monitoring**
- **Real-Time Camera Health Assessment**
- **Image Processing for ADAS (Advanced Driver Assistance Systems)**
- **Surveillance and Traffic Monitoring Systems**

## 🛠️ Future Work
- Extending BREMOLA to **handle other distortions** (e.g., noise, motion blur).
- Improving real-time performance for **embedded systems**.
- Exploring deep-learning-based approaches for further enhancement.

## 📜 License
This project is released under the **MIT License**. See [`LICENSE`](LICENSE) for details.

## 📝 Citation
If you find this work useful, please cite:
```bibtex
@article{nam2025bremola,
  author = {Nam, Woongchan and Youn, Taehyun and Ha, Chunghun},
  title = {No-Reference Image Quality Assessment with Moving Spectrum and Laplacian Filter for Autonomous Driving Environment},
  journal = {Vehicles},
  volume = {7},
  year = {2025},
  doi = {10.3390/vehicles7010008}
}
