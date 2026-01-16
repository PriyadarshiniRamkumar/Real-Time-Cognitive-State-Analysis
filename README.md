# Real-Time Cognitive State Classification Using LSTM Networks

## 🚀 Project Overview
[cite_start]This project implements a non-intrusive, vision-based framework to classify human cognitive states in real-time[cite: 1364, 1370]. [cite_start]By capturing temporal variations in facial landmarks through a standard webcam, the system identifies states such as **Alert, Fatigued, Stressed, Distracted, and Neutral**[cite: 1366, 1373].

## 📊 Key Results
* [cite_start]**Performance:** Achieved a high classification accuracy and an **F1-score of 0.88** for fatigue and distraction detection[cite: 21, 1403].
* [cite_start]**Real-Time Response:** Designed for low-latency inference within **100-150 ms** per frame window[cite: 1404].
* [cite_start]**Safety Impact:** Capable of issuing a **5-second pre-alert** before a loss of attention event[cite: 22].

## 🛠 Technical Implementation
* [cite_start]**Feature Extraction:** Used **MediaPipe Holistic** and **OpenCV** to extract 15+ metrics, including Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), PERCLOS, and head pose (pitch/yaw)[cite: 1442, 1611, 1612].
* [cite_start]**Architecture:** Implemented a **Long Short-Term Memory (LSTM)** neural network with stacked layers and dropout regularization to model temporal dependencies[cite: 1398, 1463].
* [cite_start]**Personalized Calibration:** Includes a calibration phase to establish user-specific baseline metrics, accounting for individual facial geometry and lighting variations[cite: 1470, 1478].

## 💻 Tech Stack
* [cite_start]**Deep Learning:** TensorFlow / Keras (LSTM modeling) [cite: 1607]
* [cite_start]**Computer Vision:** MediaPipe, OpenCV [cite: 1611, 1612]
* [cite_start]**Data Processing:** NumPy, Pandas, Scikit-learn [cite: 1608, 1609]
