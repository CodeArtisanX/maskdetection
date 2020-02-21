#!/usr/bin/env bash

 python export_inference_graph.py \
 --input_type=image_tensor \
 --pipeline_config_path=data/mask.config \
 --trained_checkpoint_prefix=training/model.ckpt-1000 \
 --output_directory=output