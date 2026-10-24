# Computer Vision Experiments

An OpenCV experiment that outlines image contours and flattens four-corner pages with perspective correction.

![Number grids, geometric shapes, and a checkerboard with detected contours and flattened scans](./project-reel.gif)

## Run it

Install the Python dependencies:

```bash
python -m pip install opencv-python numpy
```

Place an input image at `paper_photo.jpg`, then run:

```bash
python digitaltype_to_handwrite.py
```

The script writes `contours.png` with detected contours and `scanned_like.png` with the perspective-corrected page. It also opens preview windows.
