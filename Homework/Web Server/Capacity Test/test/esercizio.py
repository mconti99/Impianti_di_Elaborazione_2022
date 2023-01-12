#load csv file
import csv
import matplotlib.pyplot as plt
import numpy as np

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

def calc_median_response_time(data):
    resp_times = []
    for row in data:
        resp_times.append(float(row[1]))
    resp_times.sort()
    return resp_times[len(resp_times) // 2]

def main():
    #calculate average response time 
    base_file_name = r'C:\Users\itama\Desktop\Impianti di Elaborazione\test\test'
    experiments = [500, 1000, 1500, 2000, 2500, 3000, 3500]
    resp_times = []

    for experiment in experiments:
        med_resp_times = []
        for trial in range(1, 4):
            file_name = base_file_name + str(experiment) + '.' + str(trial) + '.csv'
            data = read_csv_file(file_name)
            med_resp_times.append(calc_median_response_time(data))
        resp_times.append(sum(med_resp_times) / len(med_resp_times))
    
    plt.figure(1)
    plt.plot(experiments, resp_times)
    plt.xlabel('Number of requests')
    plt.ylabel('Response time (ms)')
    plt.show()
    
    #calculate throughput
    throughputs = []

    for experiment in experiments:
        avg_throughput = 0
        for trial in range(1, 4):
            file_name = base_file_name + str(experiment) + '.' + str(trial) + 'report' + '.csv'
            data = read_csv_file(file_name)
            avg_throughput = data[-1][7]
        avg_throughput = float(avg_throughput)
        throughputs.append(avg_throughput)

    plt.figure(2)
    plt.plot(experiments, throughputs)
    plt.xlabel('Number of requests per second')
    plt.ylabel('Throughput (req/s)')
    plt.show()

    #calculate power
    power = np.array(throughputs) / np.array(resp_times)
    plt.figure(3)
    plt.plot(experiments, power)
    plt.xlabel('Number of requests per second')
    plt.ylabel('Power (req/s)/(ms)')
    plt.show()

if __name__ == '__main__':
    main()