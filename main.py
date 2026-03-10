"""
Runway Obstacle Detection System
Course: Drone Technologies - CIA 3 Project
Author: Group 9

Main execution file for runway obstacle detection using computer vision
"""

import cv2
import numpy as np
import os
from src.preprocessing import preprocess_image
from src.detection import detect_obstacles
from src.classification import classify_obstacles
from src.visualization import visualize_results

# Configuration parameters
AREA_THRESHOLDS = {
    'small': 2000,
    'medium': 10000
}

def main():
    """
    Main function to execute runway obstacle detection
    """
    # Input and output paths
    input_folder = "images"
    output_folder = "outputs"
    
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Process all images in the input folder
    if not os.path.exists(input_folder):
        print(f"Error: {input_folder} directory not found!")
        return
    
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not image_files:
        print("No image files found in the images directory!")
        print("Please add runway images to the 'images' folder")
        return
    
    for image_file in image_files:
        print(f"\nProcessing: {image_file}")
        
        # Load image
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Error loading image: {image_file}")
            continue
        
        # Step 1: Preprocess the image
        processed_image = preprocess_image(image)
        
        # Step 2: Detect obstacles using contour detection
        contours = detect_obstacles(processed_image)
        
        # Step 3: Classify obstacles based on area
        classified_obstacles = classify_obstacles(contours, AREA_THRESHOLDS)
        
        # Step 4: Visualize results
        result_image = visualize_results(image.copy(), classified_obstacles)
        
        # Save output
        output_path = os.path.join(output_folder, f"detected_{image_file}")
        cv2.imwrite(output_path, result_image)
        
        # Display results
        cv2.imshow(f"Original - {image_file}", image)
        cv2.imshow(f"Detected Obstacles - {image_file}", result_image)
        
        print(f"Results saved to: {output_path}")
        print(f"Obstacles detected: {len(classified_obstacles)}")
        
        # Wait for key press to continue
        print("Press any key to continue to next image...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("=" * 50)
    print("RUNWAY OBSTACLE DETECTION SYSTEM")
    print("Course: Drone Technologies - CIA 3")
    print("=" * 50)
    main()
    print("\nProcessing complete!")