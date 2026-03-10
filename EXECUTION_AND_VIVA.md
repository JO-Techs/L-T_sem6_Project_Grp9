# Execution Instructions and Viva Questions

## Execution Instructions

### Step-by-Step Setup and Execution

#### 1. Python Installation
```bash
# Check if Python is installed
python --version

# If not installed, download from https://python.org
# Ensure Python 3.7+ is installed
```

#### 2. Project Setup
```bash
# Navigate to project directory
cd L-T_sem6_Project_Grp9

# Verify project structure
dir  # Windows
ls   # Linux/Mac
```

#### 3. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Verify installation
python -c "import cv2, numpy; print('Dependencies installed successfully!')"
```

#### 4. Prepare Test Images
```bash
# Add runway images to images/ folder
# Supported formats: .jpg, .jpeg, .png
# Example: copy runway1.jpg to images/runway1.jpg
```

#### 5. Run the Program
```bash
# Execute main program
python main.py

# Follow on-screen instructions
# Press any key to continue between images
```

#### 6. View Results
```bash
# Check outputs folder for processed images
dir outputs/  # Windows
ls outputs/   # Linux/Mac

# Results will be saved as detected_[original_filename]
```

### Sample Execution Output
```
==================================================
RUNWAY OBSTACLE DETECTION SYSTEM
Course: Drone Technologies - CIA 3
==================================================

Processing: runway1.jpg
Results saved to: outputs/detected_runway1.jpg
Obstacles detected: 3
Press any key to continue to next image...

Processing: runway2.jpg
Results saved to: outputs/detected_runway2.jpg
Obstacles detected: 1
Press any key to continue to next image...

Processing complete!
```

## Screenshot Requirements for LMS Submission

### Required Screenshots

#### 1. Code Running Screenshot
- **What to capture:** Terminal/command prompt showing program execution
- **Include:** 
  - Command used to run the program
  - System output messages
  - Processing status for each image
  - Completion message

#### 2. Input Image Screenshot
- **What to capture:** Original runway image before processing
- **Include:**
  - Clear view of runway with visible obstacles
  - Image filename in window title
  - Full image without cropping

#### 3. Detected Obstacles Screenshot
- **What to capture:** Processed image with bounding boxes and labels
- **Include:**
  - Colored bounding boxes around obstacles
  - Classification labels (Small/Medium/Large Obstacle)
  - Area information for each detection
  - Summary statistics overlay
  - Image filename in window title

#### 4. Project Structure Screenshot
- **What to capture:** File explorer showing complete project directory
- **Include:**
  - All folders (src/, images/, outputs/, report/)
  - All Python files
  - README.md and requirements.txt
  - Sample input and output images

#### 5. Code Editor Screenshot
- **What to capture:** Main code file open in editor
- **Include:**
  - main.py file content
  - Clear view of key functions
  - Proper syntax highlighting
  - Line numbers visible

### Screenshot Guidelines
- Use high resolution (1920x1080 minimum)
- Ensure text is clearly readable
- Include window titles and taskbar
- Capture full screen for context
- Save in PNG format for best quality

## Viva Questions and Answers

### 1. What is OpenCV and why is it used in this project?

**Answer:** OpenCV (Open Source Computer Vision Library) is a comprehensive library for computer vision, machine learning, and image processing tasks. In this project, OpenCV is used because:
- It provides efficient algorithms for image preprocessing (grayscale conversion, blurring, thresholding)
- Contains robust contour detection functions
- Offers drawing capabilities for bounding boxes and labels
- Has optimized implementations for real-time processing
- Supports multiple image formats and provides extensive documentation

### 2. Explain the concept of contours in image processing.

**Answer:** Contours are curves that join continuous points along a boundary having the same color or intensity. In our runway obstacle detection:
- Contours represent the outline/boundary of objects
- They are found using cv2.findContours() after binary thresholding
- Each contour is a sequence of points defining the object's shape
- We use RETR_EXTERNAL to get only outer boundaries
- Contours help us identify separate objects and calculate their properties like area and bounding rectangles

### 3. What is the purpose of image preprocessing in this system?

**Answer:** Image preprocessing prepares the raw image for accurate obstacle detection:
- **Grayscale conversion:** Reduces computational complexity and focuses on intensity variations
- **Gaussian blur:** Removes noise and smooths the image for better edge detection
- **Adaptive thresholding:** Creates binary image that adapts to local lighting conditions
- **Morphological operations:** Removes small noise (opening) and fills gaps (closing)
- This pipeline ensures clean, binary images suitable for contour detection

### 4. How does the classification system work in this project?

**Answer:** The classification system uses area-based categorization:
- **Small obstacles (< 2000 pixels):** Classified as debris, colored yellow
- **Medium obstacles (2000-10000 pixels):** Equipment/luggage, colored orange  
- **Large obstacles (≥ 10000 pixels):** Vehicles/large equipment, colored red
- Area is calculated using cv2.contourArea() function
- Thresholds are configurable in the main.py file
- Each obstacle gets a bounding box with appropriate color coding and label

### 5. What are bounding boxes and how are they calculated?

**Answer:** Bounding boxes are rectangular regions that completely enclose detected objects:
- Calculated using cv2.boundingRect() function on each contour
- Returns (x, y, width, height) coordinates
- x, y represent top-left corner coordinates
- width and height define the rectangle dimensions
- Used for visualization and spatial localization of obstacles
- Help in determining object size and position on the runway

### 6. Explain the difference between simple thresholding and adaptive thresholding.

**Answer:** 
- **Simple thresholding:** Uses a single global threshold value for the entire image. Pixels above threshold become white, below become black.
- **Adaptive thresholding:** Calculates threshold locally for each pixel based on its neighborhood. Better for images with varying lighting conditions.
- In our project, adaptive thresholding is used because runway images may have uneven lighting, shadows, or varying illumination across different areas.

### 7. What is the role of morphological operations in image processing?

**Answer:** Morphological operations modify image structure using a kernel:
- **Opening (erosion + dilation):** Removes small noise and separates connected objects
- **Closing (dilation + erosion):** Fills small gaps and connects nearby objects
- **Erosion:** Shrinks white regions, removes small white noise
- **Dilation:** Expands white regions, fills small black holes
- In our system, these operations clean up the binary image after thresholding, improving contour detection accuracy

### 8. How would you handle false positive detections in this system?

**Answer:** Several strategies can reduce false positives:
- **Area filtering:** Set minimum area threshold to ignore very small detections
- **Aspect ratio filtering:** Remove detections with unrealistic width/height ratios
- **Shape analysis:** Use contour properties like solidity, extent, or circularity
- **Temporal filtering:** For video, track objects across frames
- **Machine learning:** Train classifiers to distinguish between obstacles and runway markings
- **Context awareness:** Consider typical runway features and exclude known permanent structures

### 9. What are the advantages and limitations of contour-based detection?

**Answer:** 
**Advantages:**
- Fast and efficient processing
- Works well for objects with clear boundaries
- Provides shape information
- Suitable for real-time applications
- No training data required

**Limitations:**
- Sensitive to lighting conditions
- May struggle with low contrast objects
- Cannot distinguish between different object types
- Affected by shadows and reflections
- May merge nearby objects or split single objects

### 10. How could this system be improved for real-world deployment?

**Answer:** Several enhancements for real-world use:
- **Deep learning integration:** Use YOLO or R-CNN for better object detection and classification
- **Video processing:** Real-time analysis of video streams from runway cameras
- **Multi-spectral imaging:** Incorporate infrared or thermal imaging for better detection
- **Weather adaptation:** Algorithms that adapt to rain, snow, or fog conditions
- **Database integration:** Store detection history and generate reports
- **Alert systems:** Automatic notifications when obstacles are detected
- **Drone integration:** Mount system on UAVs for automated runway inspection
- **API development:** Integration with airport management systems

### Additional Technical Questions

#### 11. What is the significance of the RETR_EXTERNAL flag in findContours()?

**Answer:** RETR_EXTERNAL retrieves only the outermost contours, ignoring any holes or nested contours inside objects. This is ideal for obstacle detection because:
- We only need the outer boundary of obstacles
- Reduces processing time by ignoring internal structures
- Prevents duplicate detections from nested contours
- Simplifies the contour hierarchy

#### 12. Explain the CHAIN_APPROX_SIMPLE parameter in contour detection.

**Answer:** CHAIN_APPROX_SIMPLE compresses the contour by removing redundant points:
- Stores only the endpoints of horizontal, vertical, and diagonal segments
- Reduces memory usage significantly
- Maintains shape information while using fewer points
- Alternative to CHAIN_APPROX_NONE which stores all contour points
- Sufficient for bounding box calculation and area measurement

---

**Note:** These questions cover the core concepts used in the project and demonstrate understanding of computer vision principles, OpenCV functionality, and practical implementation considerations.