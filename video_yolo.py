from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("ind.mp4", show=True, save=True)


