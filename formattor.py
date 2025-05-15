def press_title(data):
    if not data:
        raise ValueError("Data must be provided")
    if data.get("type") != "title":
        raise ValueError("Data type must be 'title'")
    titles = data.get("title")
    title_str = ""
    index = 0
    for title in titles:
        if title.get("type") == "text":
            text = title.get("text")
            if text:
                content = text.get("content")
                if content:
                    if index == 0:
                        title_str += f"{content}"
                    else:
                        title_str += f"\n{content}"
                    index += 1
    return title_str


def press_text(data):
    if not data:
        raise ValueError("Data must be provided")
    if data.get("type") != "rich_text":
        raise ValueError("Data type must be 'rich_text'")
    texts = data.get("rich_text")
    str = ""
    index = 0
    for text in texts:
        text = text.get("text")
        if text:
            content = text.get("content")
            if content:
                if index == 0:
                    str += f"{content}"
                else:
                    str += f"\n{content}"
                index += 1
    return str


def press_number(data):
    if not data:
        raise ValueError("Data must be provided")
    if data.get("type") != "number":
        raise ValueError("Data type must be 'number'")
    number = data.get("number")
    return number


def press_url(data):
    if not data:
        raise ValueError("Data must be provided")
    if data.get("type") != "url":
        raise ValueError("Data type must be 'url'")
    url = data.get("url")
    return url


def press_files(data):
    if not data:
        raise ValueError("Data must be provided")
    if data.get("type") != "files":
        raise ValueError("Data type must be 'files'")
    files = data.get("files")
    paths = []
    for file in files:
        if file.get("type") == "external":
            path = file.get("external", {}).get("url")
        elif file.get("type") == "file":
            path = file.get("file", {}).get("url")

        if path:
            paths.append(path)

    return paths


def press_file(data):
    if not data:
        raise ValueError("Data must be provided")
    if data.get("type") != "file":
        raise ValueError("Data type must be 'files'")
    path = None
    if data.get("type") == "external":
        path = data.get("external", {}).get("url")
    elif data.get("type") == "file":
        path = data.get("file", {}).get("url")
    else:
        raise ValueError(f"File type must be 'external' or 'file'\n {data}")
    return path


def press_image(data):
    if data["type"] != "image":
        raise ValueError("Invalid data type. Now type is", data["type"])
    return press_file(data["image"])
