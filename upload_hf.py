from huggingface_hub import HfApi
api = HfApi()

# Upload all the content from the local folder to your remote Space.
# By default, files are uploaded at the root of the repo
api.upload_folder(
    folder_path="checkpoints/llava-vistral-7b-lora-2",
    repo_id="Vi-VLM/llava-vistral-7b-lora",
    repo_type="model"
)