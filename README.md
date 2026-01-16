# Real-Time Cognitive State Classification Using LSTM Networks

## Project Overview
This project implements a non-intrusive, vision-based framework to classify human cognitive states in real-time. By capturing temporal variations in facial landmarks through a standard webcam, the system identifies states such as Alert, Fatigued, Stressed, Distracted, and Neutral.

##  Key Results
Performance: Achieved a high classification accuracy and an F1-score of 0.88 for fatigue and distraction detection.
Real-Time Response: Designed for low-latency inference within **100-150 ms** per frame window.
Safety Impact:Capable of issuing a 5-second pre-alert before a loss of attention event.

## Technical Implementation
Feature Extraction: Used MediaPipe Holistic and OpenCV to extract 15+ metrics, including Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), PERCLOS, and head pose (pitch/yaw).
Architecture: Implemented a Long Short-Term Memory (LSTM) neural network with stacked layers and dropout regularization to model temporal dependencies
Personalized Calibration:Includes a calibration phase to establish user-specific baseline metrics, accounting for individual facial geometry and lighting variations

##  Tech Stack
Deep Learning:TensorFlow / Keras (LSTM modeling) 
Computer Vision: MediaPipe, OpenCV 
Data Processing: NumPy, Pandas, Scikit-learn 
