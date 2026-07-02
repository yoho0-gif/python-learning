from unittest import result


student = {
    "name": "Tom",
    "age": 20,
    "score": 95
}
print(student["name"], student["age"], student["score"])

book = {
    "title": "Python",
    "price": 650,
    "author": "David"
}
print("書名:", book["title"], "價格:", book["price"], "作者:", book["author"])

data = {
    "status": "success",
    "result": {
        "temperature": 30,
        "humidity": 75
    }
}
print(data["result"]["temperature"])

response = {
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello!"
            }
        }
    ]
}
print(response["choices"][0]["message"]["content"])