import os

def extract_individual(fileName):
    with open(fileName, "br") as f:
        data = bytearray(f.read())
        first = data[:64]
        offset = data[59]
        second = data[offset: offset+264]
    f.close()
    return first + second

def extract_folder(read_path, write_path):
    print("extracting files in " + read_path)
    vectors = []
    for root, dirs, files in os.walk(read_path, topdown=False):
        for name in files:
            fileName = os.path.join(root + "/", name)
            data = extract_individual(fileName)
            vectors.append(data)
    index = len(read_path) - read_path[::-1].index("/")
    write_file = write_path + "/" + read_path[index:] + ".csv"
    print("writing to " + write_file)
    f = open(write_file, "w")
    for v in vectors:
        for i in v:
            f.write("%d," %i)
        f.write("\n")
    f.close()

def main():
    read_path = "../data/challenge_100"
    write_path = "../processed_data"
    extract_folder(read_path, write_path)

    read_path_root = "../data/exe_900"
    write_path = "../processed_data/label"
    for root, dirs, files in os.walk(read_path_root, topdown=False):
        if root != read_path_root:
            extract_folder(root.replace("\\", "/"), write_path)

main()