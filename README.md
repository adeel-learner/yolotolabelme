# yolo2labelme

A python script for converting annotation format(yolo-txt to labelme-json).

## Installation
```bash
pip install yolo-to-labelme
```
## Usage
Arguments:

`--yolo` : path to YOLO annotations directory.

`--labelme` : path to output directory.
 
`--width` : default value is 1024.

`--height` : default value is 1024.

`--classes` : Path to the classes file(TXT format).

### CLI Usage:
Specify yolo-labels-directory, output directory(optional), classes file and image size((width, height), optional).

```bash
yolotolabelme --yolo-annotation-dir path/to/yoloAnnotations --labelme-output-dir path/to/output --class-mapping-file path/to/classes-file
```

## Useful links
Github code: https://github.com/adeel-maker/yolo-to-labelme/

Yolo to labelme: https://pypi.org/project/yolo-to-labelme/

Lableme to yolo : https://pypi.org/project/labelme2yolo/