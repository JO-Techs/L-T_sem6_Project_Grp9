# Runway Obstacle Detection System

**Course:** Drone Technologies - CIA 3 Project  
**Title:** Runway Obstacle Detection  
**Group:** 9

## Project Overview

This project implements an automated runway obstacle detection system using computer vision techniques. The system analyzes runway images to identify and classify potential obstacles that could pose safety risks to aircraft operations.

### Key Features

- **Automated Detection:** Uses OpenCV contour detection to identify obstacles
- **Size-based Classification:** Categorizes obstacles as Small, Medium, or Large
- **Visual Feedback:** Draws bounding boxes and labels on detected obstacles
- **Configurable Thresholds:** Adjustable area thresholds for classification
- **Batch Processing:** Processes multiple images automatically
- **Detailed Reporting:** Provides obstacle counts and classifications

### Obstacle Categories

| Category | Area Range | Typical Objects | Color Code |
|----------|------------|-----------------|------------|
| **Small Obstacle** | < 2000 pixels | Debris, small objects | Yellow |
| **Medium Obstacle** | 2000-10000 pixels | Equipment, luggage | Orange |
| **Large Obstacle** | ≥ 10000 pixels | Vehicles, large equipment | Red |

## Technical Implementation

### Detection Pipeline

1. **Image Preprocessing**
   - Grayscale conversion
   - Gaussian blur for noise reduction
   - Adaptive thresholding
   - Morphological operations

2. **Obstacle Detection**
   - Contour detection using OpenCV
   - Area-based filtering
   - Bounding box extraction

3. **Classification**
   - Size-based categorization
   - Configurable area thresholds

4. **Visualization**
   - Bounding box drawing
   - Classification labels
   - Summary statistics

### Libraries Used

- **OpenCV:** Image processing and computer vision
- **NumPy:** Numerical operations and array handling
- **Matplotlib:** Optional visualization enhancements

## Installation Steps

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd L-T_sem6_Project_Grp9
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python -c "import cv2, numpy; print('Installation successful!')"
   ```

## How to Run

### Basic Usage

1. **Add test images:**
   - Place runway images in the `images/` folder
   - Supported formats: JPG, JPEG, PNG

2. **Run the detection system:**
   ```bash
   python main.py
   ```

3. **View results:**
   - Processed images will be saved in `outputs/` folder
   - Original and detected images will be displayed
   - Press any key to continue between images

### Sample Test Images

Download these royalty-free runway images for testing:

1. **Unsplash Airport Images:**
   - https://unsplash.com/s/photos/airport-runway
   - https://unsplash.com/s/photos/aircraft-runway

2. **Pexels Aviation Images:**
   - https://www.pexels.com/search/runway/
   - https://www.pexels.com/search/airport/

3. **Pixabay Airport Collection:**
   - https://pixabay.com/images/search/runway/
   - https://pixabay.com/images/search/airport/

### Configuration

Modify area thresholds in `main.py`:

```python
AREA_THRESHOLDS = {
    'small': 2000,    # Adjust for small obstacle threshold
    'medium': 10000   # Adjust for medium obstacle threshold
}
```

## Example Output

### Console Output
```
==================================================
RUNWAY OBSTACLE DETECTION SYSTEM
Course: Drone Technologies - CIA 3
==================================================

Processing: runway1.jpg
Results saved to: outputs/detected_runway1.jpg
Obstacles detected: 3
Press any key to continue to next image...

Processing complete!
```

### Visual Output
- **Bounding Boxes:** Colored rectangles around detected obstacles
- **Labels:** Classification text with area information
- **Summary:** Total count by obstacle category
- **Center Points:** Marked centers of detected objects

## Project Structure

```
L-T_sem6_Project_Grp9/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── main.py                  # Main execution file
│
├── src/                     # Source code modules
│   ├── preprocessing.py     # Image preprocessing functions
│   ├── detection.py         # Obstacle detection algorithms
│   ├── classification.py    # Size-based classification
│   └── visualization.py     # Result visualization
│
├── images/                  # Input runway images
│   ├── runway1.jpg         # Sample test images
│   └── runway2.jpg         # (Add your images here)
│
├── outputs/                 # Processed output images
│   ├── detected_runway1.jpg # Results with bounding boxes
│   └── detected_runway2.jpg # and classification labels
│
└── report/                  # Project documentation
    └── project_report.md    # Detailed academic report
```

## Key Functions

### Preprocessing Module (`src/preprocessing.py`)
- `preprocess_image()`: Complete image preprocessing pipeline
- `apply_edge_detection()`: Alternative edge-based preprocessing

### Detection Module (`src/detection.py`)
- `detect_obstacles()`: Main contour detection function
- `get_bounding_boxes()`: Extract bounding rectangles
- `filter_overlapping_contours()`: Remove duplicate detections

### Classification Module (`src/classification.py`)
- `classify_obstacles()`: Size-based obstacle classification
- `get_classification_summary()`: Generate detection statistics
- `update_area_thresholds()`: Modify classification parameters

### Visualization Module (`src/visualization.py`)
- `visualize_results()`: Draw bounding boxes and labels
- `add_summary_overlay()`: Add statistics overlay
- `create_side_by_side_comparison()`: Compare original vs processed

## Applications

- **Airport Safety:** Automated runway inspection
- **Drone Operations:** Pre-flight runway clearance
- **Security Systems:** Perimeter monitoring
- **Maintenance:** Debris detection and removal
- **Emergency Response:** Rapid obstacle assessment

## Advantages

- **Automated Processing:** Reduces manual inspection time
- **Consistent Detection:** Eliminates human error
- **Real-time Capability:** Fast processing for immediate results
- **Scalable Solution:** Handles multiple images efficiently
- **Configurable System:** Adjustable parameters for different scenarios

## Limitations

- **Lighting Dependency:** Performance varies with lighting conditions
- **Resolution Sensitivity:** Requires adequate image resolution
- **Static Analysis:** Processes still images only
- **Threshold Tuning:** May require parameter adjustment for different environments
- **False Positives:** May detect shadows or markings as obstacles

## Future Enhancements

- **Video Processing:** Real-time video stream analysis
- **Machine Learning:** Deep learning-based object detection
- **Multi-class Detection:** Specific object type identification
- **Weather Adaptation:** Robust performance in various weather conditions
- **Integration:** API development for drone systems

## Troubleshooting

### Common Issues

1. **No images found:**
   - Ensure images are in the `images/` folder
   - Check file formats (JPG, JPEG, PNG)

2. **Import errors:**
   - Verify OpenCV installation: `pip install opencv-python`
   - Check Python version compatibility

3. **Poor detection results:**
   - Adjust area thresholds in `main.py`
   - Try different preprocessing parameters

4. **Display issues:**
   - Ensure display is available (not headless environment)
   - Check OpenCV GUI support

### Support

For technical issues or questions:
- Review the project documentation
- Check function docstrings for parameter details
- Verify input image quality and format

---

**Developed for Drone Technologies Course - CIA 3 Assessment**  
**Academic Year 2024**