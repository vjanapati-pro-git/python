import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file_name in filenames:
            file_path = os.path.join(dirpath, file_name)
            total_size += os.path.getsize(file_path)
    return total_size

def convert_bytes_to_gb(bytes_size):
    gb_size = bytes_size / (1024 * 1024 * 1024)
    return gb_size

def get_largest_items(folder_path, num_items=20):  # Default to 20
    items = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for name in dirnames + filenames:
            full_path = os.path.join(dirpath, name)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                item_type = "File"
            else:
                size = get_folder_size(full_path)
                item_type = "Folder"
            items.append((size, full_path, item_type))

    items.sort(reverse=True)

    return items[:num_items]

def main():
    path = input("Enter the path to analyze: ")

    if not os.path.exists(path):
        print("Path does not exist.")
        return

    # Change: Calculate and print total size of the input path
    total_size = get_folder_size(path)
    total_size_gb = convert_bytes_to_gb(total_size)
    print(f"Total size of {path}: {total_size_gb:.2f} GB\n")

    print(f"Top 20 largest files/folders in {path}:")
    largest_items = get_largest_items(path)
    for size, item, item_type in largest_items:
        size_in_gb = convert_bytes_to_gb(size)
        print(f"{item}: {size_in_gb:.2f} GB ({item_type})")

if __name__ == "__main__":
    main()

