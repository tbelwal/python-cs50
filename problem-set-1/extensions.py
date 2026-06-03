def main():
    file_name = input("Enter File Name: ").lower().strip()

    media_type = get_media(file_name)
    print(media_type)


def get_media(name):
    # dot_index = name.rfind(".")
    file_ext = name[name.rfind(".") :]

    match file_ext:
        case ".gif":
            return "image/gif"
        case ".jpg":
            return "image/jpeg"
        case ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


main()
