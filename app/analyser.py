"""
This srcipt is used to access pixel averaging functionality to analyse frames
to identify when an IDE is active - reducing the cost factor for calling the
AI APIs for identifying code.
"""

from PIL.Image import Image
from pathlib import Path

RgbColor = tuple[int, int, int]
"""RGB color value.

An RGB type alias used to refernce color values as a tuple containing integer values
between 0-255. (Red, Green, Blue)
"""

DownSampleImage = list[list[RgbColor]]
"""Downsampled 2D Image data.

A type alias that reprosent a 2D data structure used to store the most frequently occuroing RGB value 
identified within a scaled section of the original raw image.
"""

ImageResolution = tuple[int, int]



def extract_pixel_average(source: Image | Path, resolution: ImageResolution) -> DownSampleImage:
    """Extract the RGB pixel average from an image.
    
    Downsample an image based of the desired accuracy.
    Extract the average RGB value for each scaled pixel before parsing to a DownSampleImage.
    
    Args:
        source (Image | Path):        A Pillow Image or RAW file-path to extract RGB values from.
        resolution (tuple[int, int]): The scaled-down image size (width, height) to extract,  
        the lower the resolution, the lower the accuracy.
    
    Raises:
        FileNotFoundError: If the source is a Path that doesn't reflect a pre-existing path struction.
        ValueError:        If the resolution argument is not within the range of the image.
    """
    if isinstance(source, Path):
        image_path = source.as_uri()
        if not source.exists():
            raise FileNotFoundError(f"Unable to locate the raw source image: {image_path}.")
        source = Image.open(image_path)

    res_width, res_height = resolution
    image_width, image_height = source.size
    pixel_width, pixel_height = int(image_width / res_width), int(image_height / res_height)

    if not (0 < res_width <= image_width or 0 < res_height <= image_height):
        raise ValueError("Required extraction resolution must be greater than 0" 
                         + "and not exceed the source file resolution.")

    downsample = []

    for y in range(res_height):
        rgb_averages = []
        for x in range(res_height):
            x1, y1 = x + pixel_width, y + pixel_height
            section = source.crop(
                (x, y, x1 if x1 <= image_width else image_width, 
                 y1 if y1 <= image_height else image_height))
            average = section.resize((1, 1)).getpixel((0, 0))
            rgb_averages.append(average)
        downsample.append(rgb_averages)
    return downsample
