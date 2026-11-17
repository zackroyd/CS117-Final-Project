import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path
import keyboard

HIGH_DISTINCTIVE_KEY = 'q'
MEDIUM_DISTINCTIVE_KEY = 'w'
LOW_DISTINCTIVE_KEY = 'e'
QUIT_KEY = 'm'
IMAGES_PATH = 'images'
HIGH_DISTINCTIVE_PATH = 'Highly Distinctive'
MEDIUM_DISTINCTIVE_PATH = 'Medium Distinctive'
LOW_DISTINCTIVE_PATH = 'Low Distinctive'


def sortImage(image:Path):
    img = mpimg.imread(image)
    plt.imshow(img)
    plt.axis("off")
    plt.show(block=False)
    plt.pause(0.1)
    while True:
        key = keyboard.read_key()
        try:
            if key == HIGH_DISTINCTIVE_KEY:
                image.rename(Path(HIGH_DISTINCTIVE_PATH+'/'+image.name))
                break
            elif key == MEDIUM_DISTINCTIVE_KEY:
                image.rename(Path(MEDIUM_DISTINCTIVE_PATH+'/'+image.name))
                break
            elif key == LOW_DISTINCTIVE_KEY:
                image.rename(Path(LOW_DISTINCTIVE_PATH+'/'+image.name))
                break
            elif key == QUIT_KEY:
                plt.close()
                exit(0)
        except FileExistsError as e:
            image.unlink(missing_ok=True)
    plt.close()


def scanForImages(source:Path):
    if source.is_file():
        return
    iterator = source.iterdir()
    for item in iterator:
        if item.is_file():
            sortImage(item)
        else:
            scanForImages(item)


def main():
    scanForImages(Path(IMAGES_PATH))
        
        
if __name__ == "__main__":
    main()