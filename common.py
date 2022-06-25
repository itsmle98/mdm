def copy_file_into_file(src, dest):
    with open(src, 'r') as fin:
        with open(dest, 'w') as fout:
            for line in fin:
                fout.write(line)