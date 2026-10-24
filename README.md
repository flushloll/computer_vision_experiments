# Computer Vision Experiments

An OpenCV experiment that finds page corners and corrects perspective in number grids, geometric worksheets, and checkerboards.

![Number, shape, and checkerboard examples before and after perspective correction](./project-reel.gif)

## Run it

Install the Python dependencies:

```bash
python -m pip install opencv-python numpy
```

Place an input image at `paper_photo.jpg`, then run:

```bash
python digitaltype_to_handwrite.py
```

The script saves the perspective-corrected page as `scanned_like.png` and opens preview windows.
