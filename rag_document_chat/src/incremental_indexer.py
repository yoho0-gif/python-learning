from metadata_store import load_metadata, save_metadata
from embedding import create_embedding
from faiss_store import build_chunks


def update_index(documents):

    old_metadata = load_metadata()
    old_store = load_existing_chunks()
    old_chunks = old_store
    new_chunks = []
    current_sources = set()

    for document in documents:

        source = document["source"]
        file_hash = document["hash"]
        current_sources.add(source)
        old_hash = None
        if source in old_metadata:
            old_hash = old_metadata[source].get("hash")

        if (old_hash == file_hash and old_chunks):

            print(f" 文件未變更：{source}")
            existing_chunks = [chunk for chunk in old_chunks if chunk.get("source") == source]
            new_chunks.extend(existing_chunks)
            continue

        if old_hash is None:

            print(f" 新增文件：{source}")

        else:

            print(f" 文件已修改：{source}")

        from text_splitter import split_text_by_article

        chunks = split_text_by_article(
            document["text"],
            source=source
        )

        for chunk in chunks:

            chunk["source"] = source
            chunk["file_hash"] = file_hash
            embedding = create_embedding(chunk["text"])

            if embedding is not None:

                chunk["embedding"] = embedding
                new_chunks.append(chunk)
        print(f"建立 Embedding：{source} - {chunk['id']}")


    old_sources = set(old_metadata.keys())
    deleted_sources = (old_sources - current_sources)

    for source in deleted_sources:

        print(f" 文件已刪除：{source}")


    for index, chunk in enumerate(new_chunks, start=1):

        chunk["id"] = index

    build_chunks(new_chunks)
    new_metadata = {}

    for document in documents:

        new_metadata[document["source"]] = {"hash": document["hash"]}
    save_metadata(new_metadata)

    return new_chunks


def load_existing_chunks():

    import os
    import json

    path = ("rag_document_chat/faiss_texts.json")

    if not os.path.exists(path):
        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)