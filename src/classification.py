"""
Obstacle Classification Module
Classifies detected obstacles based on contour area
"""

import cv2

def classify_obstacles(contours, area_thresholds):
    """
    Classify obstacles based on their contour area
    
    Args:
        contours: List of detected contours
        area_thresholds: Dictionary with 'small' and 'medium' area thresholds
        
    Returns:
        classified_obstacles: List of dictionaries containing contour info and classification
    """
    
    classified_obstacles = []
    
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)
        
        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        
        # Classify based on area thresholds
        if area < area_thresholds['small']:
            classification = "Small Obstacle"
            color = (0, 255, 255)  # Yellow for small obstacles (debris)
        elif area < area_thresholds['medium']:
            classification = "Medium Obstacle"
            color = (0, 165, 255)  # Orange for medium obstacles (equipment/luggage)
        else:
            classification = "Large Obstacle"
            color = (0, 0, 255)    # Red for large obstacles (vehicles)
        
        # Store obstacle information
        obstacle_info = {
            'contour': contour,
            'area': area,
            'bounding_box': (x, y, w, h),
            'classification': classification,
            'color': color,
            'center': (x + w//2, y + h//2)
        }
        
        classified_obstacles.append(obstacle_info)
    
    return classified_obstacles

def get_classification_summary(classified_obstacles):
    """
    Generate a summary of detected obstacles by category
    
    Args:
        classified_obstacles: List of classified obstacle dictionaries
        
    Returns:
        summary: Dictionary with counts for each obstacle type
    """
    
    summary = {
        'Small Obstacle': 0,
        'Medium Obstacle': 0,
        'Large Obstacle': 0,
        'Total': len(classified_obstacles)
    }
    
    for obstacle in classified_obstacles:
        classification = obstacle['classification']
        if classification in summary:
            summary[classification] += 1
    
    return summary

def update_area_thresholds(small_threshold=None, medium_threshold=None):
    """
    Update area thresholds for classification
    
    Args:
        small_threshold: New threshold for small obstacles
        medium_threshold: New threshold for medium obstacles
        
    Returns:
        updated_thresholds: Dictionary with updated thresholds
    """
    
    # Default thresholds
    thresholds = {
        'small': 2000,
        'medium': 10000
    }
    
    # Update if new values provided
    if small_threshold is not None:
        thresholds['small'] = small_threshold
    
    if medium_threshold is not None:
        thresholds['medium'] = medium_threshold
    
    return thresholds

def get_obstacle_details(obstacle):
    """
    Get detailed information about a specific obstacle
    
    Args:
        obstacle: Obstacle dictionary from classification
        
    Returns:
        details: Formatted string with obstacle details
    """
    
    details = f"""
    Classification: {obstacle['classification']}
    Area: {obstacle['area']:.0f} pixels
    Bounding Box: {obstacle['bounding_box']}
    Center: {obstacle['center']}
    """
    
    return details.strip()