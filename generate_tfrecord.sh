#!/usr/bin/env bash

python generate_tfrecord.py --csv_input=data/mask_train_labels.csv  --output_path=data/mask_train.record --image_dir=images
python generate_tfrecord.py --csv_input=data/mask_test_labels.csv  --output_path=data/mask_test.record --image_dir=images
python generate_tfrecord.py --csv_input=data/mask_validation_labels.csv  --output_path=data/mask_validation.record --image_dir=images
