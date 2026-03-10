"""
Test Image Generator for Runway Obstacle Detection
Creates synthetic runway images with obstacles for testing
"""

import cv2
import numpy as np
import os

def create_test_runway_image(width=1200, height=800, filename="test_runway.jpg"):
    """
    Create a synthetic runway image with obstacles for testing
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        filename: Output filename
    """
    
    # Create base runway image (gray surface)
    img = np.ones((height, width, 3), dtype=np.uint8) * 120
    
    # Add runway texture (slight noise for realism)
    noise = np.random.normal(0, 10, (height, width, 3))
    img = np.clip(img + noise, 0, 255).astype(np.uint8)
    
    # Add runway centerline
    center_x = width // 2
    cv2.line(img, (center_x, 0), (center_x, height), (255, 255, 255), 8)
    
    # Add dashed centerline
    dash_length = 40
    gap_length = 20
    y = 0
    while y < height:
        cv2.line(img, (center_x, y), (center_x, min(y + dash_length, height)), (255, 255, 0), 4)
        y += dash_length + gap_length
    
    # Add side lines
    cv2.line(img, (50, 0), (50, height), (255, 255, 255), 4)
    cv2.line(img, (width-50, 0), (width-50, height), (255, 255, 255), 4)
    
    return img

def add_obstacles_to_image(img, obstacle_config):
    """
    Add obstacles to the runway image
    
    Args:
        img: Base runway image
        obstacle_config: List of obstacle dictionaries
    """
    
    for obstacle in obstacle_config:
        x, y = obstacle['position']
        w, h = obstacle['size']
        color = obstacle['color']
        
        # Add some 3D effect with shadow
        shadow_offset = 3
        cv2.rectangle(img, (x + shadow_offset, y + shadow_offset), 
                     (x + w + shadow_offset, y + h + shadow_offset), 
                     (50, 50, 50), -1)
        
        # Draw main obstacle
        cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
        
        # Add highlight for 3D effect
        cv2.rectangle(img, (x, y), (x + w//3, y + h//3), 
                     tuple(min(255, c + 50) for c in color), -1)

def generate_test_images():
    """
    Generate multiple test images with different obstacle configurations
    """
    
    # Ensure images directory exists
    os.makedirs("images", exist_ok=True)
    
    # Test Image 1: Small debris
    print("Generating runway1.jpg - Small debris...")
    img1 = create_test_runway_image()
    obstacles1 = [
        {'position': (200, 300), 'size': (25, 15), 'color': (80, 60, 40)},  # Small debris
        {'position': (800, 200), 'size': (30, 20), 'color': (60, 80, 40)},  # Small debris
        {'position': (400, 500), 'size': (20, 25), 'color': (40, 60, 80)},  # Small debris
    ]
    add_obstacles_to_image(img1, obstacles1)
    cv2.imwrite("images/runway1.jpg", img1)
    
    # Test Image 2: Medium equipment
    print("Generating runway2.jpg - Medium equipment...")
    img2 = create_test_runway_image()
    obstacles2 = [
        {'position': (300, 250), 'size': (80, 60), 'color': (0, 100, 200)},    # Equipment
        {'position': (700, 400), 'size': (90, 70), 'color': (200, 100, 0)},    # Luggage cart
        {'position': (150, 600), 'size': (60, 80), 'color': (100, 200, 0)},    # Equipment
    ]
    add_obstacles_to_image(img2, obstacles2)
    cv2.imwrite("images/runway2.jpg", img2)
    
    # Test Image 3: Large vehicles
    print("Generating runway3.jpg - Large vehicles...")
    img3 = create_test_runway_image()
    obstacles3 = [
        {'position': (400, 200), 'size': (150, 100), 'color': (50, 50, 200)},   # Large vehicle
        {'position': (200, 500), 'size': (120, 80), 'color': (200, 50, 50)},    # Vehicle
    ]
    add_obstacles_to_image(img3, obstacles3)
    cv2.imwrite("images/runway3.jpg", img3)
    
    # Test Image 4: Mixed obstacles
    print("Generating runway4.jpg - Mixed obstacles...")
    img4 = create_test_runway_image()
    obstacles4 = [
        {'position': (100, 150), 'size': (20, 15), 'color': (80, 60, 40)},      # Small
        {'position': (300, 300), 'size': (75, 55), 'color': (0, 150, 200)},     # Medium
        {'position': (600, 450), 'size': (140, 90), 'color': (200, 50, 100)},   # Large
        {'position': (800, 200), 'size': (25, 20), 'color': (60, 80, 40)},      # Small
        {'position': (450, 600), 'size': (85, 65), 'color': (150, 100, 0)},     # Medium
    ]
    add_obstacles_to_image(img4, obstacles4)
    cv2.imwrite("images/runway4.jpg", img4)
    
    # Test Image 5: Clean runway (no obstacles)
    print("Generating runway5.jpg - Clean runway...")
    img5 = create_test_runway_image()
    cv2.imwrite("images/runway5.jpg", img5)
    
    print("\nTest images generated successfully!")
    print("Files created in 'images/' folder:")
    print("- runway1.jpg (Small debris)")
    print("- runway2.jpg (Medium equipment)")
    print("- runway3.jpg (Large vehicles)")
    print("- runway4.jpg (Mixed obstacles)")
    print("- runway5.jpg (Clean runway)")
    print("\nYou can now run: python main.py")

if __name__ == "__main__":
    print("=" * 50)
    print("RUNWAY TEST IMAGE GENERATOR")
    print("Creating synthetic runway images for testing...")
    print("=" * 50)
    generate_test_images()