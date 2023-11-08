# yolo2labelme

A python script for converting annotation format(yolo-txt to labelme-json).

## Installation
```bash
pip install yolo-to-labelme
```
## Usage
Arguments:

`--yolo` : path to YOLO annotations directory.

`--labelme(optional)` : path to output directory.
 
`--width(optional)` : default value is 1024.

`--height(optional)` : default value is 1024.

`--classes` : Path to the classes file(TXT format).

`--img_ext(optional)` : Image file extension (e.g., .jpg, .png, etc.).

### CLI Usage:
Specify yolo-labels-directory, output directory(optional), classes file, image size(width, height)(optional), and image extention(optional).

```bash
yolotolabelme --yolo path/to/yoloAnnotations --labelme path/to/output --classes path/to/classes-file
```

## Useful links

Yolo to labelme: https://pypi.org/project/yolo-to-labelme/

Lableme to yolo : https://pypi.org/project/labelme2yolo/
