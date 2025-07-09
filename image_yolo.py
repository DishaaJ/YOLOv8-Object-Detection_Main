from ultralytics import YOLO

model = YOLO("yolov8s.pt")  # Use yolov8s.pt or yolov8m.pt for more accuracy

results = model("blr.jpg", show=True, save=True)


