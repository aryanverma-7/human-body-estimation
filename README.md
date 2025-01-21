
# 🎓 AICTE Internship - Human Pose Estimation and Motion Detection 🚀

Welcome to the AICTE Internship repository! This project focuses on human pose estimation using OpenCV and MediaPipe, along with motion detection capabilities. It also includes a Streamlit-based web app for pose estimation visualization.

## 📂 Directory Structure

```
└── akshaysenn-aicte-internship/
    ├── README.md            # Project documentation
    ├── Estimation_app.py    # Streamlit app for human pose estimation
    ├── Module2-Image.py     # Pose estimation on a static image using MediaPipe
    ├── Module2-Video.py     # Pose estimation in a video using MediaPipe
    ├── MotionDetection.py   # Basic motion detection using OpenCV
    ├── app.py               # Simple Streamlit app
    ├── graph_opt.pb         # TensorFlow model for pose estimation
    └── test.py              # Verifies MediaPipe installation
```

## ⚙️ Technologies Used

- **OpenCV** 🖼️: For image and video processing.
- **MediaPipe** 🦵: For pose estimation and motion detection.
- **Streamlit** 📊: To create interactive web applications.
- **TensorFlow** 🤖: To load and use pre-trained pose estimation models.

---

## 📄 File Descriptions

### `Estimation_app.py`

This file contains a **Streamlit** app that performs **human pose estimation** on images. It uses a **TensorFlow** model and **OpenCV** to detect human body parts and visualize the pose.

#### Features:
- Upload an image 📸 for pose estimation.
- Detection threshold slider 🎚️ for customizing detection sensitivity.
- Display original image and pose estimation results.

### `Module2-Image.py`

This script uses **MediaPipe** to perform pose estimation on a static image. It detects keypoints like joints and limbs, then visualizes them.

#### Features:
- Image loading and processing.
- Pose landmarks and connections drawn on the image.
- Visual feedback of detected poses.

### `Module2-Video.py`

This file performs pose estimation on videos using **MediaPipe**. It captures video frames, processes them, and draws pose landmarks and connections.

#### Features:
- Process video frames in real-time 🎥.
- Pose detection with **Mediapipe Pose**.
- Display the video with landmarks and connections.

### `MotionDetection.py`

This script demonstrates basic **motion detection** using **OpenCV**. It reads an image, processes it, and allows saving the result to the filesystem.

#### Features:
- Image reading and motion detection.
- Save processed images.

### `app.py`

A basic **Streamlit** app to get started. It simply displays a welcoming message.

#### Features:
- Title and description display.

### `test.py`

Verifies if **MediaPipe** is correctly installed and working.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/akshaysenn-aicte-internship.git
   cd akshaysenn-aicte-internship
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run Estimation_app.py
   ```

---

## 🚀 How to Use

### Pose Estimation (Image)
1. Launch the app by running `Estimation_app.py`.
2. Upload an image and adjust the detection threshold.
3. View the pose estimation results in real-time.

### Pose Estimation (Video)
1. Modify the `Module2-Video.py` to provide the path to your video.
2. Run the script, and it will display the processed video with pose landmarks.

### Motion Detection
1. Use `MotionDetection.py` to test basic motion detection on images.
2. Process and save the results to the filesystem.

---

## 🔧 Dependencies

- `opencv-python` 🖼️: Image and video processing.
- `mediapipe` 🦵: Pose estimation.
- `streamlit` 📊: Web app creation.
- `tensorflow` 🤖: Model inference for pose detection.

---

## 🌟 Acknowledgments

- **AICTE** for providing the opportunity to work on this internship project.
- **OpenCV** and **MediaPipe** teams for their amazing libraries that make computer vision easier.

---

## 📞 Contact

For any queries, reach out at:  
- Email: `theakshaysen.com`
- LinkedIn: [Akshay Sain](https://www.linkedin.com/in/akshaysenn)

---

Happy Coding! 🎉
