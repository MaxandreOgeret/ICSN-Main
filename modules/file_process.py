from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET


def xmlToCsv(path='./xml/', output='output.csv'):
    xmlFiles = [f for f in listdir(path) if (isfile(join(path, f)) and f[-3:] == 'xml')]
    csv = 'filename, width, height, class, xmin, ymin, xmax, ymax\n'

    for file in xmlFiles:

        tree = ET.parse(path + file)
        root = tree.getroot()
        filename = root.find('filename').text
        width = root.find('size').find('width').text
        height = root.find('size').find('height').text

        boxes = []
        for box in root.iter('object'):
            className = box.find('name').text
            bndbox = box.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text

            line = "{},{},{},{},{},{},{},{}\n".format(filename, width, height, className, xmin, ymin, xmax, ymax)
            csv = csv + line

    csv_file = open(output, "w")
    csv_file.write(csv)
    csv_file.close()

    return(path+output)