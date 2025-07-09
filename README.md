# 🦾 YOLOv8 Real-Time Object Detection

This repository contains a real-time object detection system built using the **YOLOv8** model from the **Ultralytics** library. YOLO (You Only Look Once) is a state-of-the-art object detection algorithm known for its speed and accuracy.

---

## 🔍 What is YOLO?

**YOLO (You Only Look Once)** is a deep learning model used for real-time object detection. Unlike traditional methods, YOLO divides the image into grids and predicts bounding boxes and class probabilities directly in a single evaluation — making it extremely fast.

---

## 🆚 YOLOv8 vs YOLOv5 vs YOLOv3

| Feature             | YOLOv3            | YOLOv5                | YOLOv8 (Latest)         |
|---------------------|-------------------|------------------------|--------------------------|
| 📅 Release Year     | 2018              | 2020 (by Ultralytics) | 2023                    |
| ⚙️ Framework        | Darknet           | PyTorch               | PyTorch                 |
| 🧠 Architecture     | Manually designed | Custom PyTorch        | Fully re-engineered     |
| 🧪 Export Support   | Limited           | ONNX, TorchScript     | ONNX, CoreML, TFLite    |
| 📦 Model Formats    | `.weights`        | `.pt`                 | `.pt`, `.onnx`, etc.    |
| 🏃 Real-time Speed  | Fast              | Faster                | Fastest                 |
| 🎯 Accuracy         | Good              | Great                 | Best                    |
| 🧩 Post-processing  | Manual            | Auto (via NMS, etc.)  | Optimized               |

> **YOLOv8** offers out-of-the-box better performance, cleaner codebase, and easier training/inference pipelines.

---

## ⚡ Powered by Ultralytics

[Ultralytics](https://github.com/ultralytics/ultralytics) is the official developer behind YOLOv5 and YOLOv8. Their open-source tools provide simple Python APIs for training, testing, and deploying models in just a few lines.

---

## 🧠 Features of this Project

- ✅ Real-time webcam detection  
- ✅ Image and video input support  
- ✅ Powered by YOLOv8n (`nano` version for speed)  
- ✅ Built using Ultralytics and OpenCV  
- ✅ Can be extended to train on custom datasets  

---

## 🛠 Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/DishaaJ/YOLOv8-Object-Detection.git
cd YOLOv8-Object-Detection
python -m venv venv
venv\Scripts\activate   # For Windows
pip install -r requirements.txt
```

---

## 📸 Sample Detection

![YOLOv8 Sample Detection](https://github.com/user-attachments/assets/3b2b17ae-ab50-44b4-8b07-71894d5b51c6)

---

## 📄 License

This project is for educational and research purposes only.

---

## 🙋‍♀️ Author

Made with ❤️ by **Disha Jain**