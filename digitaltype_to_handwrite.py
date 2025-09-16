import cv2
import numpy as np

# Load image
img = cv2.imread("paper_photo.jpg")

# Optional: convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Preprocess: blur to reduce noise
gray_blur = cv2.GaussianBlur(gray, (5,5), 0)

# Detect edges for perspective correction
edges = cv2.Canny(gray_blur, 30, 100)  # Try different thresholds

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Visualize all contours
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0,255,0), 2)
cv2.imshow("Contours", contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find largest contour (assuming it’s the paper)
if contours:
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    paper_contour = contours[0]

    # Try different epsilon values
    for eps in [0.01, 0.02, 0.03]:
        epsilon = eps * cv2.arcLength(paper_contour, True)
        approx = cv2.approxPolyDP(paper_contour, epsilon, True)
        print(f"With epsilon={eps}, approx corners: {len(approx)}")
        if len(approx) == 4:
            print("Found 4-corner contour!")
            pts = np.float32([point[0] for point in approx])
            width = max(np.linalg.norm(pts[0]-pts[1]), np.linalg.norm(pts[2]-pts[3]))
            height = max(np.linalg.norm(pts[1]-pts[2]), np.linalg.norm(pts[3]-pts[0]))
            dst = np.float32([[0,0],[width,0],[width,height],[0,height]])
            M = cv2.getPerspectiveTransform(pts, dst)
            warped = cv2.warpPerspective(img, M, (int(width), int(height)))
            cv2.imwrite("scanned_like.png", warped)
            cv2.imshow("Warped", warped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
    else:
        print("No contour with four corners found for any epsilon.")
else:
    print("No contours found in image.")
