# Computer Vision Experiments

An OpenCV experiment that outlines contours in number grids, geometric shapes, and checkerboards, then flattens page perspective.

![Number, geometric shape, and checkerboard examples with detected contours and flattened scans](./project-reel.gif)

## Run it

Install the Python dependencies:

```bash
python -m pip install opencv-python numpy
```

Place an input image at `paper_photo.jpg`, then run:

```bash
python digitaltype_to_handwrite.py
```

The script saves detected contours as `contours.png` and the perspective-corrected page as `scanned_like.png`. It also opens preview windows.
