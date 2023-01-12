#load csv file
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

#open file
def read_csv_file(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[1:]

def calc_avg_response_time(data):
    resp_times = []
    for row in data:
        resp_times.append(float(row[1]))
    return sum(resp_times) / len(resp_times)

def main():
    #calculate average response time
    page_sizes = ['big', 'medium', 'small']
    ctts = ['lowctt', 'midctt', 'highctt']

    for ctt in ctts:
        for page_size in page_sizes:
            for i in range(1,6):
                data = read_csv_file(f'report-{page_size}-{ctt}-{i}.csv')
                response_time = str(calc_avg_response_time(data))
                response_time = response_time.replace('.', ',')
                #print(f'Page size: {page_size}, ctt:{ctt}, i:{i}, response time: {response_time}')
                print(f'{response_time}')
if __name__ == '__main__':
    main()