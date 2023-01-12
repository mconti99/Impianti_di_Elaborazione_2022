import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    with open(sys.argv[1]) as f:

        f_csv = open(sys.argv[2], 'w', newline='')
        writer = csv.writer(f_csv)

        data = []
        cols = []

        first_iter = True

        for line in f:
            if(line == '-' or line == '-\n'):
                if(first_iter):
                    first_iter = False
                    writer.writerow(cols)
                writer.writerow(data)
                data = []
            else:
                line = line.replace('\t', ' ')
                line = line.replace('\n', '')
                line = line.replace(':', ' ')
                line = [x for x in line.split(' ') if x != '']
                if(line[0] != 'Iteration'):
                    if(first_iter):
                        cols.append(line[0])
                    data.append(line[1])

        f_csv.close()


if __name__ == '__main__':
    main()