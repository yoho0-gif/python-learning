import json
import os


METADATA_PATH = "rag_document_chat/document_metadata.json"


def load_metadata():

    if not os.path.exists(METADATA_PATH):
        return {}

    with open(
        METADATA_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_metadata(metadata):

    with open(
        METADATA_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            ensure_ascii=False,
            indent=2
        )