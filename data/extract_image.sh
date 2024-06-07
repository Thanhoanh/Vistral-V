#!/bin/bash

# COCO2017

unzip -j data/images/coco2017/train2017.zip -d data/images/coco2017/train2017
unzip -j data/images/coco2017/val2017.zip -d data/images/coco2017/val2017
rm data/images/coco2017/train2017.zip data/images/coco2017/val2017.zip

# LLAVA
mkdir data/images/llava/llava_pretrain
mkdir data/images/llava/llava_pretrain/images
unzip -j data/images/llava/images.zip -d data/images/llava/llava_pretrain/images
rm data/images/llava/images.zip

# SAM
unzip -j data/images/sam/images.zip -d data/images/sam/images
rm data/images/sam/images.zip

# share_textvqa
unzip -j data/images/share_textvqa/images.zip -d data/images/share_textvqa/images
rm data/images/share_textvqa/images.zip

# web-celebrity
unzip -j data/images/web-celebrity/images.zip -d data/images/web-celebrity/images
rm data/images/web-celebrity/images.zip 

# web-landmark
unzip -j data/images/web-landmark/images.zip -d data/images/web-landmark/images
rm data/images/web-landmark/images.zip

# wikiart
unzip -j data/images/wikiart/images.zip -d data/images/wikiart/images
rm data/images/wikiart/images.zip
