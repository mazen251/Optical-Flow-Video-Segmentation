import numpy as np
import cv2
import time


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:, :, 0], flow[:, :, 1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx * fx + fy * fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[..., 0] = ang * (180 / np.pi / 2)
    hsv[..., 1] = 255
    hsv[..., 2] = np.minimum(v * 4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr


def classify_intensity(prev_counters, counters):
    rate_change = [counters[i] - prev_counters[i] for i in range(3)]
    avg_rate = sum(rate_change) / 3
    if avg_rate < 0.5:
        return "Low"
    elif avg_rate < 2.0:
        return "Moderate"
    else:
        return "High"


def count_colors(hsv):
    red_counter = np.sum((hsv[..., 0] >= 0) & (hsv[..., 0] <= 10))
    green_counter = np.sum((hsv[..., 0] > 40) & (hsv[..., 0] <= 80))
    blue_counter = np.sum((hsv[..., 0] > 100) & (hsv[..., 0] <= 140))
    return red_counter, green_counter, blue_counter


video_path = "Video Input/x2.mp4"
cap = cv2.VideoCapture(video_path)
suc, prev = cap.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
motion_counter = 0
frame_list = []
prev_counters = [0, 0, 0]
motion_detected = False
motion_start_time = 0
motion_gap_threshold = 3

while True:
    suc, img = cap.read()
    if not suc:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    prevgray = gray
    hsv = draw_hsv(flow)
    red, green, blue = count_colors(hsv)
    counters = [red, green, blue]

    if all(counters) and not motion_detected:
        motion_detected = True
        motion_start_time = time.time()

    if motion_detected:
        frame_list.append(img.copy())

    if not all(counters) and motion_detected:
        elapsed_time = time.time() - motion_start_time
        if elapsed_time > motion_gap_threshold:
            motion_counter += 1
            motion_detected = False
            if motion_counter % 2 == 0 and len(frame_list) > 0:
                file_name = f"video_segment_{motion_counter}.mp4"
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(file_name, fourcc, 20.0, (img.shape[1], img.shape[0]))
                for frame in frame_list:
                    out.write(frame)
                out.release()
                frame_list = []

    intensity_class = classify_intensity(prev_counters, counters) if motion_detected else "No Motion"
    prev_counters = counters.copy()

    cv2.putText(hsv, f"Motion Intensity: {intensity_class}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(hsv, f"Motion Counter: {motion_counter}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.namedWindow('flow HSV', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('flow HSV', 800, 600)
    cv2.imshow('flow HSV', hsv)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


