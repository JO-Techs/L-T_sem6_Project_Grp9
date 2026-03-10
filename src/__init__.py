"""
Runway Obstacle Detection System - Source Package
Course: Drone Technologies - CIA 3 Project

This package contains the core modules for runway obstacle detection:
- preprocessing: Image preprocessing operations
- detection: Obstacle detection using contour analysis
- classification: Size-based obstacle classification
- visualization: Result visualization and display
"""

__version__ = "1.0.0"
__author__ = "Group 9"
__course__ = "Drone Technologies"
__project__ = "CIA 3 - Runway Obstacle Detection"

# Import main functions for easy access
from .preprocessing import preprocess_image
from .detection import detect_obstacles
from .classification import classify_obstacles
from .visualization import visualize_results

__all__ = [
    'preprocess_image',
    'detect_obstacles', 
    'classify_obstacles',
    'visualize_results'
]