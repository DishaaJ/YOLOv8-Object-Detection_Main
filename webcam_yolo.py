from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# 0 = default webcam
results = model(source=0, show=True, save=True)


