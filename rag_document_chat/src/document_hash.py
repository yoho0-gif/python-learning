import hashlib


def calculate_file_hash(path):
    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        while True:
            data = file.read(1024 * 1024)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()
