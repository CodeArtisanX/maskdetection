## 项目目录
```c
.
├── annotations
│   ├── test
│   ├── train
│   └── validation
├── data
│   ├── model
│   ├── mask.config
│   ├── mask.pbtxt
│   ├── mask_test.record
│   ├── mask_test_labels.csv
│   ├── mask_train.record
│   ├── mask_train_labels.csv
│   ├── mask_validation.record
│   └── mask_validation_labels.csv
├── export_inference_graph.py
├── export_inference_graph.sh
├── generate_tfrecord.py
├── generate_tfrecord.sh
├── images
│   ├── mask.jpg
│   └── momask.jpg
├── model_main.py
├── test.py
├── train.sh
├── training
├── xml2csv.py
├── xmls
│   ├── mask.jpg
│   └── momask.jpg
```
## 依赖

1. LabelImg  [https://github.com/tzutalin/labelImg](https://github.com/tzutalin/labelImg);
2. TensorFlow Models [https://github.com/tensorflow/models/](https://github.com/tensorflow/models/);
3. Pre training model of coco dataset [faster_rcnn_resnet101_coco_11_06_2017.tar.gz](http://storage.googleapis.com/download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gz).

## 配置

1. 编辑 data 目录下到 mask.config 文件，将内容包含 PATH_TO_BE_CONFIGURED 替换成当前文件的路径；
2. 将下载后的 COCO 数据集预训练模型解压保存到 data/model 目录。

## 训练
```shell
sh train.sh
```

