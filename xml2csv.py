import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import random
import time
import shutil


class Xml2Cvs:
    def __init__(self):
        self.xml_filepath = r'./xmls'
        self.save_basepath = r"./annotations"
        self.trainval_percent = 0.9
        self.train_percent = 0.85

    def xml_split_train(self):

        total_xml = os.listdir(self.xml_filepath)
        num = len(total_xml)
        list = range(num)
        tv = int(num * self.trainval_percent)
        tr = int(tv * self.train_percent)
        trainval = random.sample(list, tv)
        train = random.sample(trainval, tr)
        print("train and val size", tv)
        print("train size", tr)
        start = time.time()
        test_num = 0
        val_num = 0
        train_num = 0
        for i in list:
            name = total_xml[i]
            if i in trainval:
                if i in train:
                    directory = "train"
                    train_num += 1
                    xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
                    if (not os.path.exists(xml_path)):
                        os.mkdir(xml_path)
                    filePath = os.path.join(self.xml_filepath, name)
                    newfile = os.path.join(self.save_basepath, os.path.join(directory, name))
                    shutil.copyfile(filePath, newfile)
                else:
                    directory = "validation"
                    xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
                    if (not os.path.exists(xml_path)):
                        os.mkdir(xml_path)
                    val_num += 1
                    filePath = os.path.join(self.xml_filepath, name)
                    newfile = os.path.join(self.save_basepath, os.path.join(directory, name))
                    shutil.copyfile(filePath, newfile)
            else:
                directory = "test"
                xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
                if (not os.path.exists(xml_path)):
                    os.mkdir(xml_path)
                test_num += 1
                filePath = os.path.join(self.xml_filepath, name)
                newfile = os.path.join(self.save_basepath, os.path.join(directory, name))
                shutil.copyfile(filePath, newfile)

        end = time.time()
        seconds = end - start
        print("train total : " + str(train_num))
        print("validation total : " + str(val_num))
        print("test total : " + str(test_num))
        total_num = train_num + val_num + test_num
        print("total number : " + str(total_num))
        print("Time taken : {0} seconds".format(seconds))

    def xml_to_csv(self, path):
        xml_list = []
        for xml_file in glob.glob(path + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            print(root.find('filename').text)
            for object in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size').find('width').text),
                         int(root.find('size').find('height').text),
                         object.find('name').text,
                         int(object.find('bndbox').find('xmin').text),
                         int(object.find('bndbox').find('ymin').text),
                         int(object.find('bndbox').find('xmax').text),
                         int(object.find('bndbox').find('ymax').text)
                         )
                xml_list.append(value)
        column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = pd.DataFrame(xml_list, columns=column_name)
        return xml_df

    def main(self):
        for directory in ['train', 'test', 'validation']:
            xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
            xml_df = self.xml_to_csv(xml_path)
            xml_df.to_csv('data/mask_{}_labels.csv'.format(directory), index=None)
            print('Successfully converted xml to csv.')


if __name__ == '__main__':
    Xml2Cvs().xml_split_train()
    Xml2Cvs().main()

