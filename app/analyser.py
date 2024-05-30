"""
This srcipt is used to access pixel averaging functionality to analyse frames
to identify when an IDE is active - reducing the cost factor for calling the
AI APIs for identifying code.
"""
import cv2
from PIL.Image import Image
from pathlib import Path
from typing import Union
import utils
import logging

RgbColor = tuple[int, int, int]
"""RGB color value.

An RGB type alias used to refernce color values as a tuple containing integer values
between 0-255. (Red, Green, Blue)
"""

DownSampleImage = list[list[RgbColor]]
"""Downsampled 2D Image data.

A type alias that represents a 2D data structure used to store the most frequently occuroing RGB value 
identified within a scaled-down block inside the original raw image.
"""

ImageResolution = tuple[int, int]


def convert_frame_to_pillow_image(filename: str, timestamp: float) -> Union[Image, None]:
    """Extracts a frame from a video and parse as a Pillow Image.
    
    Takes a capture of a frame at a specified timestamp from a video, and converts the frame capture
    into a Pillow Image.

    Args:
        filename (str): The filename of the video being captured.
        timestamp (float): The specified time to capture the video at.

    Returns:
        Image: The captured frame in the video as a Pillow Image.
    """
    capture = cv2.VideoCapture(f"{utils.get_vid_save_path()}{filename}")
    if not capture.isOpened():
        logging.error(f"Failed to open {filename} stream")
        return None
    capture.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
    ret, frame = capture.read()

    if ret:
        logging.info(f"Successfully captured frame @ {timestamp}s in file {filename}.")
        try:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            return image
        except cv2.error as e:
            logging.error(f"Failed to convert the captured frame @ {timestamp}s in file {filename} to a Pillow Image.")
    else:
        logging.error(f"Failed to capture frame @ {timestamp}s in file {filename}.")
    capture.release()
        


def extract_pixel_average(source: Image, resolution: ImageResolution) -> DownSampleImage:
    """Extract the RGB pixel average from an image.
    
    Downsample an image based of the desired accuracy.
    Extract the average RGB value for each scaled pixel before parsing to a DownSampleImage.
    
    Args:
        source (Image):               A Pillow Image to extract its RGB pixel averaged values from.
        resolution (tuple[int, int]): The scaled-down image size (width, height) to extract, the lower the resolution, 
                                      the lower the accuracy.

    Returns:
        DownSampleImage: A 2D array containing RGB tuple values representing the pixels values from an averaged downsampled image.
    """
    res_width, res_height = resolution
    image_width, image_height = source.size
    pixel_width, pixel_height = int(image_width / res_width), int(image_height / res_height)

    if not (0 < res_width <= image_width or 0 < res_height <= image_height):
        logging.error("Could not extract average as the desired resolution was out of range.")

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
