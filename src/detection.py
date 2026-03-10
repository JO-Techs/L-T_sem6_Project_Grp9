"""
Obstacle Detection Module
Handles contour detection and bounding box extraction
"""

import cv2
import numpy as np

def detect_obstacles(processed_image):
    """
    Detect obstacles in the processed binary image using contour detection
    
    Args:
        processed_image: Binary image from preprocessing
        
    Returns:
        valid_contours: List of contours representing detected obstacles
    """
    
    # Step 1: Find contours in the binary image
    # RETR_EXTERNAL: retrieves only outer contours
    # CHAIN_APPROX_SIMPLE: compresses horizontal, vertical, and diagonal segments
    contours, hierarchy = cv2.findContours(
        processed_image, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE
    )
    
    # Step 2: Filter contours based on area and shape
    valid_contours = []
    min_area = 100  # Minimum area to consider as an obstacle
    
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)
        
        # Filter out very small contours (likely noise)
        if area > min_area:
            # Additional shape filtering can be added here
            # For example, aspect ratio, solidity, etc.
            
            # Calculate bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)
            
            # Filter based on aspect ratio (avoid very thin lines)
            aspect_ratio = w / h if h > 0 else 0
            if 0.1 < aspect_ratio < 10:  # Reasonable aspect ratio range
                valid_contours.append(contour)
    
    return valid_contours

def get_bounding_boxes(contours):
    """
    Extract bounding boxes from contours
    
    Args:
        contours: List of contours
        
    Returns:
        bounding_boxes: List of (x, y, w, h) tuples
    """
    
    bounding_boxes = []
    
    for contour in contours:
        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        bounding_boxes.append((x, y, w, h))
    
    return bounding_boxes

def filter_overlapping_contours(contours, overlap_threshold=0.5):
    """
    Remove overlapping contours to avoid duplicate detections
    
    Args:
        contours: List of contours
        overlap_threshold: Minimum overlap ratio to consider as duplicate
        
    Returns:
        filtered_contours: List of non-overlapping contours
    """
    
    if len(contours) <= 1:
        return contours
    
    # Get bounding boxes
    boxes = [cv2.boundingRect(contour) for contour in contours]
    areas = [cv2.contourArea(contour) for contour in contours]
    
    # Sort by area (largest first)
    sorted_indices = sorted(range(len(areas)), key=lambda i: areas[i], reverse=True)
    
    filtered_contours = []
    used_indices = set()
    
    for i in sorted_indices:
        if i in used_indices:
            continue
            
        filtered_contours.append(contours[i])
        used_indices.add(i)
        
        # Check for overlaps with remaining contours
        x1, y1, w1, h1 = boxes[i]
        
        for j in sorted_indices:
            if j <= i or j in used_indices:
                continue
                
            x2, y2, w2, h2 = boxes[j]
            
            # Calculate intersection
            x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
            y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
            intersection = x_overlap * y_overlap
            
            # Calculate union
            union = w1 * h1 + w2 * h2 - intersection
            
            # Check overlap ratio
            if union > 0 and intersection / union > overlap_threshold:
                used_indices.add(j)
    
    return filtered_contours