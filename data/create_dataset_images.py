from huggingface_hub import hf_hub_download

LOCAR_DIR = "/mnt/disks/dev/data"

# Download COCO2017 dataset
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/coco2017/train2017.zip", local_dir=LOCAR_DIR, repo_type="dataset")
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/coco2017/val2017.zip", local_dir=LOCAR_DIR, repo_type="dataset")

# Download llava pretrain dataset
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/llava/images.zip", local_dir=LOCAR_DIR, repo_type="dataset")

# # Download SAM pretrain dataset
# hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/sam/images.zip", local_dir=LOCAR_DIR, repo_type="dataset")

# Download share_textvqa dataset
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/share_textvqa/images.zip", local_dir=LOCAR_DIR, repo_type="dataset")

# Download web-landmark dataset
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/web-landmark/images.zip", local_dir=LOCAR_DIR, repo_type="dataset")

# Download web-celebrity dataset
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/web-celebrity/images.zip", local_dir=LOCAR_DIR, repo_type="dataset")

# Download wikiart dataset
hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/wikiart/images.zip", local_dir=LOCAR_DIR, repo_type="dataset")