
def main():
    with open('in.txt', 'r') as in_file:
        with open('out.txt', 'w+') as out_file:
            for line in in_file:
                raw = line.split("==")
                line = f'{raw[0]} = "=={raw[1].strip()}" '
                print(line)
                out_file.write(line + '\n')


if __name__ == '__main__':
    main()