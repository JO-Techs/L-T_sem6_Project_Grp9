# Sample Test Images for Runway Obstacle Detection

## Royalty-Free Image Sources

### 1. Unsplash (Free High-Quality Images)

**Airport Runway Images:**
- Search URL: https://unsplash.com/s/photos/airport-runway
- Recommended images:
  - "Empty airport runway" by Ross Parmly
  - "Aircraft on runway" by Ashim D'Silva
  - "Airport runway lights" by Hanson Lu

**Aircraft and Aviation:**
- Search URL: https://unsplash.com/s/photos/aircraft-runway
- Look for images with:
  - Clear runway surfaces
  - Visible objects or equipment
  - Good lighting conditions

### 2. Pexels (Free Stock Photos)

**Runway Collection:**
- Search URL: https://www.pexels.com/search/runway/
- Recommended searches:
  - "airport runway"
  - "aircraft landing"
  - "aviation ground"

**Airport Images:**
- Search URL: https://www.pexels.com/search/airport/
- Filter for:
  - Landscape orientation
  - High resolution (1920x1080+)
  - Clear visibility

### 3. Pixabay (Free Images)

**Aviation Category:**
- Search URL: https://pixabay.com/images/search/runway/
- Additional searches:
  - "airport tarmac"
  - "aircraft ground"
  - "aviation infrastructure"

### 4. Wikimedia Commons (Public Domain)

**Airport Infrastructure:**
- Search URL: https://commons.wikimedia.org/wiki/Category:Airport_runways
- Benefits:
  - Public domain images
  - High-quality documentation photos
  - Various airport locations worldwide

## Image Selection Criteria

### Ideal Test Images Should Have:

1. **Clear Runway Surface:**
   - Visible runway markings
   - Good contrast between surface and objects
   - Minimal shadows or glare

2. **Visible Objects:**
   - Equipment, vehicles, or debris
   - Various sizes for classification testing
   - Clear object boundaries

3. **Good Image Quality:**
   - Resolution: 1024x768 minimum
   - Format: JPEG or PNG
   - Good lighting conditions

4. **Suitable Perspective:**
   - Ground-level or slightly elevated view
   - Runway surface clearly visible
   - Objects not too distant

### Objects to Look For:

- **Small Objects:** Debris, tools, small equipment
- **Medium Objects:** Luggage carts, ground equipment, cones
- **Large Objects:** Vehicles, aircraft tugs, large machinery

## Download Instructions

### Method 1: Manual Download
1. Visit the recommended websites
2. Search for "airport runway" or "aircraft ground"
3. Select high-quality images with visible objects
4. Download and save to `images/` folder
5. Rename files as `runway1.jpg`, `runway2.jpg`, etc.

### Method 2: Sample Images Description

**For testing purposes, create or find images with:**

1. **runway1.jpg** - Empty runway with small debris
2. **runway2.jpg** - Runway with ground equipment
3. **runway3.jpg** - Runway with vehicles
4. **runway4.jpg** - Mixed obstacles of different sizes

## Image Preparation Tips

### Before Using Images:

1. **Resize if necessary:**
   ```python
   # Optional: Resize large images
   import cv2
   img = cv2.imread('large_image.jpg')
   resized = cv2.resize(img, (1920, 1080))
   cv2.imwrite('runway1.jpg', resized)
   ```

2. **Check image quality:**
   - Ensure good contrast
   - Verify objects are clearly visible
   - Test with different lighting conditions

3. **Organize files:**
   - Place all test images in `images/` folder
   - Use descriptive filenames
   - Keep original copies as backup

## Creating Synthetic Test Images

### If Real Images Are Not Available:

1. **Use Image Editing Software:**
   - Create simple runway backgrounds
   - Add rectangular objects of different sizes
   - Vary object colors and positions

2. **Simple Test Pattern:**
   ```python
   # Create a simple test image
   import cv2
   import numpy as np
   
   # Create blank runway image
   img = np.ones((600, 800, 3), dtype=np.uint8) * 128
   
   # Add runway markings
   cv2.line(img, (400, 0), (400, 600), (255, 255, 255), 5)
   
   # Add test objects
   cv2.rectangle(img, (100, 100), (150, 130), (0, 0, 0), -1)  # Small
   cv2.rectangle(img, (300, 200), (400, 280), (0, 0, 0), -1)  # Medium
   cv2.rectangle(img, (500, 300), (650, 450), (0, 0, 0), -1)  # Large
   
   cv2.imwrite('images/test_runway.jpg', img)
   ```

## Legal Considerations

### When Using Downloaded Images:

1. **Check License:**
   - Ensure images are royalty-free or public domain
   - Read usage terms and conditions
   - Give proper attribution if required

2. **Academic Use:**
   - Most free stock photo sites allow academic use
   - Always verify license terms
   - Keep records of image sources

3. **Commercial Use:**
   - If planning commercial deployment, verify commercial usage rights
   - Consider purchasing licensed images for commercial applications

## Troubleshooting Image Issues

### Common Problems and Solutions:

1. **Poor Detection Results:**
   - Try images with better contrast
   - Ensure objects are clearly visible
   - Check image resolution and quality

2. **No Objects Detected:**
   - Verify objects are large enough (>100 pixels area)
   - Adjust threshold parameters in main.py
   - Try different preprocessing settings

3. **Too Many False Positives:**
   - Use images with cleaner backgrounds
   - Adjust area thresholds
   - Try images with better lighting

---

**Note:** Always respect copyright and licensing terms when downloading and using images. For academic projects, most free stock photo sites provide suitable images under permissive licenses.