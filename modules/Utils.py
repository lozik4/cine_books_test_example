import datetime
import os
import time
from io import BytesIO

from PIL import Image
from selenium import webdriver

import config_file as cfg


class ScrolledScreenshot:

    @staticmethod
    def get_image(driver: webdriver):
        driver.execute_script(f"window.scrollTo({0}, {0})")
        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        rectangles = []
        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height
            if top_height > total_height:
                top_height = total_height
            while ii < total_width:
                top_width = ii + viewport_width
                if top_width > total_width:
                    top_width = total_width
                rectangles.append((ii, i, top_width, top_height))
                ii = ii + viewport_width
            i = i + viewport_height
        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if previous is not None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            file_name = f'{cfg.BASE_DIR}/data/temp_screenshots/part_{part}.png'
            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])
            stitched_image.paste(screenshot, offset)
            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle
        buf = BytesIO()
        stitched_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        return byte_im


def convert_str_to_seconds(value: str) -> float:
    x = time.strptime(value.split(',')[0], '%H:%M:%S')
    return datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
