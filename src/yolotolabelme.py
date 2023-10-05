import os
import json
import argparse

def load_class_mapping(mapping_file):
    class_mapping = {}
    with open(mapping_file, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            class_name = line.strip()
            class_mapping[index] = class_name
    return class_mapping

def convert_yolo_to_labelme(yolo_annotation_dir, labelme_output_dir, image_width, image_height, class_mapping):
    # Create LabelMe output directory if it doesn't exist
    os.makedirs(labelme_output_dir, exist_ok=True)

    # Iterate through YOLO(txt format) annotation files
    for yolo_annotation_file in os.listdir(yolo_annotation_dir):
        if yolo_annotation_file.endswith('.txt'):
            # Parse YOLO annotation
            with open(os.path.join(yolo_annotation_dir, yolo_annotation_file), 'r') as yolo_file:
                yolo_annotations = yolo_file.readlines()

            labelme_shapes = []

            for yolo_annotation in yolo_annotations:
                annotation_parts = yolo_annotation.strip().split()
                if len(annotation_parts) == 5:  # Bounding box format
                    class_id, x_center, y_center, width, height = map(float, annotation_parts)

                    # Calculate coordinates for LabelMe bounding box and rescale coordinates to match image size
                    x1, y1 = int(x_center * image_width - (width * image_width) / 2), int(y_center * image_height - (height * image_height) / 2)
                    x2, y2 = int(x_center * image_width + (width * image_width) / 2), int(y_center * image_height + (height * image_height) / 2)

                    shape_type = 'rectangle'
                elif len(annotation_parts) > 5:  # Polygon format
                    class_id = float(annotation_parts[0])
                    polygon_points = [int(float(x)) for x in annotation_parts[1:]]
                    shape_type = 'polygon'
                else:
                    continue  # Skip invalid annotations

                if class_id in class_mapping:
                    class_label = class_mapping[class_id]
                else:
                    class_label = 'unknown'  # Handle unknown classes

                if shape_type == 'rectangle':
                    labelme_shapes.append({
                        'label': class_label,
                        'points': [[x1, y1], [x2, y1], [x2, y2], [x1, y2]],  # Rectangle coordinates
                        'group_id': None,
                        'shape_type': shape_type,
                        'flags': {},
                    })
                elif shape_type == 'polygon':
                    labelme_shapes.append({
                        'label': class_label,
                        'points': [polygon_points],
                        'group_id': None,
                        'shape_type': shape_type,
                        'flags': {},
                    })

            # Create LabelMe JSON structure
            labelme_data = {
                'version': '4.5.9',
                'flags': {},
                'shapes': labelme_shapes,
                'imagePath': yolo_annotation_file.replace('.txt', '.jpg'),  # Replace with your image filename
                'imageData': None,
                'imageHeight': image_height,  # Replace with your image height
                'imageWidth': image_width,   # Replace with your image width
            }

            # Write LabelMe JSON file
            labelme_output_file = os.path.splitext(yolo_annotation_file)[0] + '.json'
            with open(os.path.join(labelme_output_dir, labelme_output_file), 'w') as labelme_file:
                json.dump(labelme_data, labelme_file, indent=2)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Convert YOLO annotations to LabelMe JSON format.")
    
    # Add arguments
    parser.add_argument("--yolo", required=True, help="Path to the YOLO annotations directory.")
    parser.add_argument("--labelme", required=False, default= 'results', help="Path to output directory.")
    parser.add_argument("--width", type=int, required=False, default= 1024, help="Width of the images.")
    parser.add_argument("--height", type=int, required=False, default= 1024, help="Height of the images.")
    parser.add_argument("--classes", required=True, help="Path to the classes file(TXT format).")
    
    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.labelme_output_dir):
        os.makedirs(args.labelme_output_dir)    
    
    # Load class mapping from file
    class_mapping = load_class_mapping(args.class_mapping_file)
    
    # Convert YOLO annotations to LabelMe format
    convert_yolo_to_labelme(args.yolo_annotation_dir, args.labelme_output_dir, args.image_width, args.image_height, class_mapping)
    
    print("---------------Conversion completed----------------")
    
    
if __name__ == '__main__':
    main()