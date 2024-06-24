#!/bin/bash

# COCO2017

export DATA_DIR=/mnt/disks/dev/data/images

unzip -j ${DATA_DIR}/coco2017/train2017.zip -d ${DATA_DIR}/coco2017/train2017
unzip -j ${DATA_DIR}/coco2017/val2017.zip -d ${DATA_DIR}/coco2017/val2017
rm ${DATA_DIR}/coco2017/train2017.zip ${DATA_DIR}/coco2017/val2017.zip
mv ${DATA_DIR}/coco2017 ${DATA_DIR}/coco

# LLAVA
mkdir ${DATA_DIR}/llava/llava_pretrain
mkdir ${DATA_DIR}/llava/llava_pretrain/images
unzip ${DATA_DIR}/llava/images.zip -d ${DATA_DIR}/llava/llava_pretrain/images
# rm ${DATA_DIR}/llava/images.zip

# SAM
# unzip -j ${DATA_DIR}/sam/images.zip -d ${DATA_DIR}/sam/images
# rm ${DATA_DIR}/sam/images.zip

# share_textvqa
unzip -j ${DATA_DIR}/share_textvqa/images.zip -d ${DATA_DIR}/share_textvqa/images
# rm ${DATA_DIR}/share_textvqa/images.zip

# web-celebrity
unzip -j ${DATA_DIR}/web-celebrity/images.zip -d ${DATA_DIR}/web-celebrity/images
# rm ${DATA_DIR}/web-celebrity/images.zip 

# web-landmark
unzip -j ${DATA_DIR}/web-landmark/images.zip -d ${DATA_DIR}/web-landmark/images
# rm ${DATA_DIR}/web-landmark/images.zip

# wikiart
unzip -j ${DATA_DIR}/wikiart/images.zip -d ${DATA_DIR}/wikiart/images
# rm ${DATA_DIR}/wikiart/images.zip
