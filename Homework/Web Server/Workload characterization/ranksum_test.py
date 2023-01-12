from scipy.stats import ranksums
import csv
import sys

def main():
    data_LL = [[] for i in range(8)]
    with open(sys.argv[1]) as f:
        for index, line in enumerate(f):
            if(index != 0):
                line = line.replace('\n', '')
                vals = line.split(',"')
                for i in range(1, 9):
                    val = vals[i].replace('"', '').replace(',', '.')
                    data_LL[i-1].append(float(val))

    data_LL1 = [[] for i in range(8)]
    with open(sys.argv[2]) as f:
        for index,line in enumerate(f):
            if(index != 0):
                line = line.replace('\n', '')
                vals = line.split(',"')
                for i in range(1, 9):
                    val = vals[i].replace('"', '').replace(',', '.')
                    data_LL1[i-1].append(float(val))
        
    for i in range(8):
        print("Il p-value per la componente principale {} è pari a: {}".format(i+1,ranksums(data_LL[i], data_LL1[i]).pvalue))


if __name__ == '__main__':
    main()
