import os
import random
from datasets import load_dataset
import json

def create_vi_llava_dataset():
    def process_conv_llava(conversation):
        llava_conversation = []
        for idx, turn in enumerate(conversation):
            role = turn["role"]
            content = turn["content"]

            if role == "user":
                if idx == 0 and "<image>" not in content:
                    content = f"<image>\n{content}" if random.random() > 0.5 else f"{content}\n<image>"
                llava_conversation.append({
                    "from": "human",
                    "value": content
                })
            elif role == "assistant":
                llava_conversation.append({
                    "from": "gpt",
                    "value": content
                })
        return llava_conversation

    def preprocess_function(examples, path_prefix):
        id = ['llava_' + id for id in examples["id"]]
        image = [os.path.join(path_prefix, file_name) for file_name in examples["file_name"]]
        conversations = [process_conv_llava(conversation) for conversation in examples["conversation"]]

        return {
            "id": id,
            "image": image,
            "conversations": conversations
        }

    dataset_list = [
        "vi_llava_conversation",
        "vi_llava_complex_reasoning",
        "vi_llava_detail_description"
    ]

    split = ["train", "validation"]

    for s in split:
        total_dataset = []
        for dataset_name in dataset_list:
            print(f"Processing {dataset_name} {s}")
            dataset = load_dataset("Vi-VLM/Vista", name=dataset_name, split=s)
            if s == "train":
                path_prefix = "coco/train2017"
            elif s == "validation":
                path_prefix = "coco/val2017"
            dataset = dataset.map(lambda batch: preprocess_function(batch, path_prefix), batched=True, remove_columns=dataset.column_names)
            dataset = dataset.to_list()
            total_dataset.extend(dataset)
        with open(f"data/vi_llava_{s}.json", "w") as f:
            json.dump(total_dataset, f, ensure_ascii=False, indent=4)

def create_vi_sharegpt4v_dataset():
    def preprocess_function(examples):
        id = ['sharegpt4v_' + id for id in examples["id"]]
        image = examples["image"]
        conversations = examples["vi_conversations"]
        return {
            "id": id,
            "image": image,
            "conversations": conversations
        }
    dataset = load_dataset("Vi-VLM/Vista", name="vi_sharegpt4v", split="train")
    dataset = dataset.map(preprocess_function, batched=True, remove_columns=dataset.column_names)
    dataset = dataset.to_list()
    with open("data/vi_sharegpt4v.json", "w") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    create_vi_llava_dataset()
    create_vi_sharegpt4v_dataset()