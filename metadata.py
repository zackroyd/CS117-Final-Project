from exif import Image
from pathlib import Path
from coordinateMath import dms_to_decimal
import csv

IMAGE_SOURCE_PATH = 'imagesBackup'


def scanForImages(source:Path):
    for item in source.rglob("*"):
        if item.is_dir():
            continue
        img = Image(str(item))
        if img.has_exif and hasattr(img, "gps_latitude"):
            lat = dms_to_decimal(img.gps_latitude, img.gps_latitude_ref)
            lon = dms_to_decimal(img.gps_longitude, img.gps_longitude_ref)
            yield str(item), lat, lon


def main():
    with open('output.csv', 'w+', newline='', encoding='utf-8') as out:
        writer = csv.writer(out)
        headers = ['Path', 'Latitude', 'Longitude']
        writer.writerow(headers)
        for imagepath, lat, lon in scanForImages(Path(IMAGE_SOURCE_PATH)):
            writer.writerow([imagepath, lat, lon])
            
if __name__ == '__main__':
    main()
            