from transformers import (BloomTokenizerFast,
                          BloomForTokenClassification,
                          DataCollatorForTokenClassification,
                          AutoModelForTokenClassification,
                          TrainingArguments, Trainer)
from datasets import load_dataset
import torch
import os


def run(model_name):
    tokenizer = BloomTokenizerFast.from_pretrained(f"bigscience/{model_name}", add_prefix_space=True)
    model = BloomForTokenClassification.from_pretrained(f"bigscience/{model_name}")
    print(model.config)
    print(model)

    inputs = tokenizer(
        "HuggingFace is a company based in Paris and New York", add_special_tokens=False, return_tensors="pt"
    )

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_token_class_ids = logits.argmax(-1)

    # Note that tokens are classified rather then input words which means that
    # there might be more predicted token classes than words.
    # Multiple token classes might account for the same word
    predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]
    print(predicted_tokens_classes)


if __name__ == "__main__":
    model_name = "bloom-560m"
    run(model_name)
