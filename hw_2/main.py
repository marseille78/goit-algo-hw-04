def get_cats_info(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            result_data = []

            for cat in file.readlines():
                id, name, age = cat.strip().split(",")
                item_data = {
                    "id": id,
                    "name": name,
                    "age": age,
                }
                result_data.append(item_data)

        return result_data
    except FileNotFoundError:
        print("File Not Found")
        return []


def main():
    file_path = "./cats_file.txt"

    print(get_cats_info(file_path))


if __name__ == "__main__":
    main()