# Car_license_template_reader_using_machine_learning

# Project Description

This project is an automated license plate detection and recognition system from videos using computer vision and artificial intelligence techniques. The main pipeline consists of:

1. **License Plate Detection in Video Frames**  
   Using the YOLO (You Only Look Once) model to detect license plate regions in each video frame and crop those areas.

2. **Second Stage Cropping for Accuracy**  
   Performing a second detection and cropping on the cropped plates to improve focus and accuracy.

3. **Image Processing for Character Segmentation**  
   Applying image processing techniques such as grayscale conversion, thresholding, dilation, erosion, and contour detection to isolate individual characters on the license plate.

4. **Optical Character Recognition (OCR)**  
   Using a pretrained TrOCR (Transformer-based OCR) model fine-tuned for Thai characters and digits to read each segmented character from the license plate.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pay501/license_plate_reader_using_machine_learning.git
   
2. Change directory to project directory:

   ```bash
   cd car_license_template_reader_using_machine_learning
   
3. Install necessary lib:

   ```bash
   pip install -r requiements.txt

4. Change directory to file to  run:

   ```bash
   cd prediction

5. run script:

   ```bash
   python video.py

