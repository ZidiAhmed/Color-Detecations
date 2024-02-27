# Color Detection using OpenCV

This Python script utilizes OpenCV to perform real-time color detection from a webcam feed. The detected colors are then displayed at the top of the video feed.

## Prerequisites

Make sure you have the required libraries installed:

```bash
pip install opencv-python
```

## Usage

1. Run the script by executing the following command:

   ```bash
   python color_detection.py
   ```

2. A window will open displaying the webcam feed.

3. The script detects colors within predefined color ranges and displays the detected colors at the top of the video feed.

4. Press the 'q' key to exit the application.

## Color Ranges

The script defines specific color ranges in HSV (Hue, Saturation, Value) format for detection. You can modify the `color_ranges` dictionary to include additional colors or adjust existing ranges as needed.

```python
color_ranges = {
    'Green': ((40, 50, 50), (80, 255, 255)),
    'Red': ((0, 100, 100), (10, 255, 255)),
    'Blue': ((90, 50, 50), (130, 255, 255)),
    'Yellow': ((20, 100, 100), (40, 255, 255)),
    'Purple': ((140, 50, 50), (170, 255, 255)),
    'Orange': ((10, 100, 100), (20, 255, 255)),
    'Pink': ((150, 50, 50), (170, 255, 255)),
    'Brown': ((10, 50, 50), (20, 200, 200)),
    # Add more colors as needed
}
```

Feel free to customize these color ranges according to your requirements.

## Exit

Press the 'q' key to exit the application and close the webcam feed window.

**Note:** Make sure to adjust the color ranges based on your specific use case or the objects you want to detect.