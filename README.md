
# Optical Flow Video Segmentation
Welcome to the Optical Flow Video Segmentation project! This repository contains code for segmenting video sequences using the Farneback method of optical flow. The primary goal is to estimate the motion of objects in a video based on the apparent motion of pixels between consecutive frames.

## Table of Contents
- Introduction
- Features
- Installation
- Usage
- Contributing
- License
- Contact
- Acknowledgements

## Introduction
The Optical Flow Video Segmentation project utilizes the Farneback method for estimating dense optical flow in video sequences. Unlike the Lucas-Kanade method, which is sensitive to noise and cannot handle large, rapid motions, the Farneback method provides more reliable flow fields by computing a polynomial expansion between frames.

## Features
- **Dense Optical Flow Estimation**: Uses the Farneback method to provide a dense estimation of optical flow.
- **Motion Intensity Classification**: Classifies motion intensity into three levels (low, moderate, high) based on the mean intensity of the flow and its produced HSV colors.
- **Motion Detection and Segmentation**: Analyzes the produced HSV colors to capture significant motion and determine the start and end of movements.

## Installation
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites:
- Python 3.x
- OpenCV
- NumPy

### Steps
```sh
# Clone the Repository
git clone https://github.com/mazen251/Optical-Flow-Video-Segmentation.git
cd Optical-Flow-Video-Segmentation-master

# Install Dependencies
pip install -r requirements.txt
```

## Usage
### Importance of Video Segmentation
Video segmentation is a crucial task in computer vision and has numerous applications, including surveillance, autonomous driving, human-computer interaction, and video editing. Accurate segmentation allows for the precise identification and tracking of objects within a video, enabling systems to understand and react to dynamic scenes.

The Farneback method of optical flow used in this project offers a dense and robust estimation of motion between video frames. This is particularly important in scenarios with rapid or complex motions where traditional methods like Lucas-Kanade may fail.

### How It Works
The Farneback method computes the apparent motion of pixels between consecutive frames to estimate the optical flow. The intensity of this motion is then classified into three levels: low, moderate, and high. By analyzing the HSV (Hue, Saturation, Value) color representation of the flow, the system can distinguish between different types of movements and determine the start and end points of significant actions.


The analysis focuses on the produced HSV colors (red, blue, and yellow) to capture significant motion. The presence of all three colors indicates significant motion, while the absence of one suggests weak motion. If all colors fade to black, it signifies the end of the movement.

### Running the Code
To run the optical flow video segmentation on a video file:
```sh
# Execute the Script
python OpticalFlow.py --input <path_to_video_file>
```
Replace \`<path_to_video_file>\` with the path to your video file.

## Contributing
Contributions are welcomed to improve this project. To contribute, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
Mazen Walid - [@Mazen Walid](https://www.linkedin.com/in/mazen-walid-225582208/)

## Acknowledgements
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
