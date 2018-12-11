import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import sys
from sklearn.model_selection import train_test_split
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('xml_path', '', 'Path to the XML folder')
flags.DEFINE_string('test_size', '', 'Size of the test dataset')
FLAGS = flags.FLAGS

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)

    xml_train, xml_test = train_test_split(xml_df, test_size=float(FLAGS.test_size), random_state=0)

    return xml_train, xml_test


def main(_):
    image_path = os.path.join(os.getcwd(), FLAGS.xml_path)
    xml_train, xml_test = xml_to_csv(image_path)
    
    xml_train.to_csv('data/train.csv', index=None)
    xml_test.to_csv('data/test.csv', index=None)
    
    print('Successfully created test and train CSV files from XML.')


if __name__ == '__main__':
    tf.app.run()
