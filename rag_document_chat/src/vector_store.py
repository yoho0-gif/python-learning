import json
import os


def save_vectors(chunks, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2
        )


def load_vectors(path):
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)