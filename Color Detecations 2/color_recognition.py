import cv2
import numpy as np

def detect_color(frame):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color ranges for detection
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

    detected_colors = []

    for color_name, (lower_color, upper_color) in color_ranges.items():
        # Threshold the HSV image to get only the specified color
        mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))

        # Check if there are non-zero pixels in the mask
        if cv2.countNonZero(mask) > 0:
            detected_colors.append(color_name)

    return detected_colors

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Detect colors
        detected_colors = detect_color(frame)

        # Display the detected colors at the top of the screen
        text = ', '.join(detected_colors)
        cv2.putText(frame, f"Detected Colors: {text}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Color Detection', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
