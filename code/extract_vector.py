import os

def extract_individual(fileName):
    with open(fileName, "br") as f:
        data = bytearray(f.read())
        first = data[:64]
        offset = data[60]
        second = data[offset: offset+264]
    f.close()
    return first + second

def extract_folder(read_path, write_path):
    vectors = []
    for root, dirs, files in os.walk(read_path, topdown=False):
        for name in files:
            fileName = os.path.join(root + "/", name)
            data = extract_individual(fileName)
            vectors.append(data)
            print(fileName)
    index = len(read_path) - read_path[::-1].index("/")
    write_file = read_path[index:]
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


main()