## 🚗 BREMOLA: No-Reference Image Quality Assessment for Autonomous Driving

## 📌 Overview
This repository provides the implementation of **BREMOLA** (Blind/Referenceless Model via Moving Spectrum and Laplacian Filter), a **No-Reference Image Quality Assessment (NR-IQA)** method tailored for **autonomous driving environments**. BREMOLA is designed to accurately assess image quality degradation, particularly **blur**, in real-time driving scenarios by leveraging a **Fourier transform-based shifted spectrum** and **Laplacian filter for edge detection**.

## 📰 Paper
- **Title**: No-Reference Image Quality Assessment with Moving Spectrum and Laplacian Filter for Autonomous Driving Environment
- **Authors**: Woongchan Nam, Taehyun Youn, Chunghun Ha
- **Published in**: *Vehicles*
- **DOI**: [10.3390/vehicles7010008](https://doi.org/10.3390/vehicles7010008)

## 🏆 Key Features
- **No-Reference IQA**: Evaluates image quality without needing a reference image.
- **Real-Time Adaptability**: Designed for rapidly changing autonomous driving environments.
- **Fourier Transform-based Shifted Spectrum**: Quantifies image sharpness loss due to blur.
- **Laplacian Filter Compensation**: Reduces metric variance caused by environmental complexity.
- **Robust to Driving Conditions**: Tested on images from diverse locations (Dubai, Los Angeles, San Francisco, Seoul).

## 📊 Experimental Results
<img width="1275" alt="image" src="https://github.com/user-attachments/assets/148a4db9-c900-4b73-8adb-e22da72a86f6" />

### **Comparison Before and After Applying BREMOLA**  
**Before applying BREMOLA**, NR-IQA methods based on moving spectrum analysis showed **high variability in quality metric values due to environmental factors (lighting, number of objects, etc.)**, especially for **low blur levels (1×1 to 5×5 filters)**. In particular, **overlapping metric values between 1×1 (original) and 3×3 (mild blur) made it difficult to distinguish normal and degraded conditions**. However, **after applying BREMOLA, the Laplacian filter was used to compensate for image complexity**, reducing variance in quality metrics and **providing a more consistent decrease in values as blur increased**, making it easier to identify degraded images.  

<img width="1542" alt="image" src="https://github.com/user-attachments/assets/2fe214fb-de35-4b84-8867-cc80fcb60de8" />

### **Comparison with Traditional IQA Metrics**  
PSNR and SSIM, as **Full-Reference IQA (FR-IQA) methods, require an original reference image**, making them unsuitable for autonomous driving. **BRISQUE, a No-Reference IQA (NR-IQA) method, was highly sensitive to environmental changes**, leading to **inconsistent quality assessments influenced more by image complexity than actual blur**. In contrast, **BREMOLA is robust to environmental variations and provides a reliable measure of blur**, making it **better suited for real-time camera sensor monitoring in autonomous driving environments**. 🚗💡

---
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
