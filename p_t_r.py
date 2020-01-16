
def main():
    with open('ptr_in.txt', 'r') as in_file:
        with open('ptr_out.txt', 'w+') as out_file:
            for line in in_file:
                raw = line.split("=")
                raw[0] = raw[0].strip()
                raw[3] = raw[3].strip()
                raw[3] = raw[3].strip('"')
                line = f'{raw[0]}=={raw[3].strip()}'
                print(line)
                out_file.write(line + '\n')


if __name__ == '__main__':
    main()
