"""
Image Preprocessing Module
Handles image preprocessing operations for runway obstacle detection
"""

import cv2
import numpy as np

def preprocess_image(image):
    """
    Preprocess the input image for obstacle detection
    
    Args:
        image: Input BGR image from OpenCV
        
    Returns:
        processed_image: Binary image ready for contour detection
    """
    
    # Step 1: Convert to grayscale
    # Reduces computational complexity and focuses on intensity variations
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Apply Gaussian blur
    # Reduces noise and smooths the image for better edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Step 3: Apply adaptive thresholding
    # Creates binary image that adapts to local lighting conditions
    # This is better than simple thresholding for varying lighting
    thresh = cv2.adaptiveThreshold(
        blurred, 
        255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        11, 
        2
    )
    
    # Step 4: Apply morphological operations
    # Remove small noise and fill gaps in detected objects
    kernel = np.ones((3, 3), np.uint8)
    
    # Opening: erosion followed by dilation (removes small noise)
    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    # Closing: dilation followed by erosion (fills small gaps)
    processed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    
    return processed

def apply_edge_detection(image):
    """
    Alternative preprocessing using edge detection
    
    Args:
        image: Input BGR image
        
    Returns:
        edges: Edge-detected binary image
    """
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    return edges