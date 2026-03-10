"""
Visualization Module
Handles drawing bounding boxes, labels, and results display
"""

import cv2
import numpy as np

def visualize_results(image, classified_obstacles):
    """
    Draw bounding boxes and labels on the image for detected obstacles
    
    Args:
        image: Original input image (BGR format)
        classified_obstacles: List of classified obstacle dictionaries
        
    Returns:
        result_image: Image with bounding boxes and labels drawn
    """
    
    result_image = image.copy()
    
    for obstacle in classified_obstacles:
        # Extract obstacle information
        x, y, w, h = obstacle['bounding_box']
        classification = obstacle['classification']
        color = obstacle['color']
        area = obstacle['area']
        
        # Draw bounding rectangle
        cv2.rectangle(result_image, (x, y), (x + w, y + h), color, 2)
        
        # Prepare label text
        label = f"{classification}"
        area_text = f"Area: {area:.0f}"
        
        # Calculate text size for background rectangle
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        thickness = 2
        
        (label_w, label_h), _ = cv2.getTextSize(label, font, font_scale, thickness)
        (area_w, area_h), _ = cv2.getTextSize(area_text, font, font_scale-0.1, thickness-1)
        
        # Draw background rectangle for text
        text_bg_height = label_h + area_h + 10
        text_bg_width = max(label_w, area_w) + 10
        
        cv2.rectangle(
            result_image, 
            (x, y - text_bg_height - 5), 
            (x + text_bg_width, y), 
            color, 
            -1
        )
        
        # Draw label text
        cv2.putText(
            result_image, 
            label, 
            (x + 5, y - area_h - 10), 
            font, 
            font_scale, 
            (255, 255, 255), 
            thickness
        )
        
        # Draw area text
        cv2.putText(
            result_image, 
            area_text, 
            (x + 5, y - 5), 
            font, 
            font_scale - 0.1, 
            (255, 255, 255), 
            thickness - 1
        )
        
        # Draw center point
        center_x, center_y = obstacle['center']
        cv2.circle(result_image, (center_x, center_y), 3, color, -1)
    
    # Add summary information
    add_summary_overlay(result_image, classified_obstacles)
    
    return result_image

def add_summary_overlay(image, classified_obstacles):
    """
    Add summary information overlay to the image
    
    Args:
        image: Image to add overlay to
        classified_obstacles: List of classified obstacles
    """
    
    # Count obstacles by type
    small_count = sum(1 for obs in classified_obstacles if obs['classification'] == 'Small Obstacle')
    medium_count = sum(1 for obs in classified_obstacles if obs['classification'] == 'Medium Obstacle')
    large_count = sum(1 for obs in classified_obstacles if obs['classification'] == 'Large Obstacle')
    total_count = len(classified_obstacles)
    
    # Prepare summary text
    summary_lines = [
        f"Total Obstacles: {total_count}",
        f"Small (Debris): {small_count}",
        f"Medium (Equipment): {medium_count}",
        f"Large (Vehicles): {large_count}"
    ]
    
    # Draw summary background
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    thickness = 2
    
    max_width = 0
    total_height = 0
    
    for line in summary_lines:
        (w, h), _ = cv2.getTextSize(line, font, font_scale, thickness)
        max_width = max(max_width, w)
        total_height += h + 10
    
    # Position summary in top-right corner
    start_x = image.shape[1] - max_width - 20
    start_y = 20
    
    # Draw background rectangle
    cv2.rectangle(
        image, 
        (start_x - 10, start_y - 10), 
        (start_x + max_width + 10, start_y + total_height + 10), 
        (0, 0, 0), 
        -1
    )
    
    # Draw border
    cv2.rectangle(
        image, 
        (start_x - 10, start_y - 10), 
        (start_x + max_width + 10, start_y + total_height + 10), 
        (255, 255, 255), 
        2
    )
    
    # Draw summary text
    y_offset = start_y + 25
    for line in summary_lines:
        cv2.putText(
            image, 
            line, 
            (start_x, y_offset), 
            font, 
            font_scale, 
            (255, 255, 255), 
            thickness
        )
        y_offset += 30

def create_side_by_side_comparison(original, processed):
    """
    Create side-by-side comparison of original and processed images
    
    Args:
        original: Original input image
        processed: Processed image with detections
        
    Returns:
        comparison: Combined image showing both original and processed
    """
    
    # Resize images to same height if needed
    height = min(original.shape[0], processed.shape[0])
    
    original_resized = cv2.resize(original, (int(original.shape[1] * height / original.shape[0]), height))
    processed_resized = cv2.resize(processed, (int(processed.shape[1] * height / processed.shape[0]), height))
    
    # Combine horizontally
    comparison = np.hstack((original_resized, processed_resized))
    
    # Add labels
    cv2.putText(comparison, "Original", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(comparison, "Detected", (original_resized.shape[1] + 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return comparison