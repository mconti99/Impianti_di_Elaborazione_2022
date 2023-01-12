import sys
import numpy as np

def main():
    with open(sys.argv[1]) as f:

        n_clusters = int(input("Insert number of clusters: "))

        clusters = [[] for i in range(n_clusters)]


        for i, line in enumerate(f):
            if i == 0:
                continue
            else:
                vals = line.split('",')
                vals = [val.replace('"', '') for val in vals]
                vals = [val.replace('\n', '') for val in vals]
                vals = [val.replace(",", '.') for val in vals]
                vals = [float(val) for val in vals]
                elem = {
                    "id": i,
                    "data": vals[:-1]
                }
                clusters[int(vals[-1])-1].append(elem)
        
        for i,cluster in enumerate(clusters):
            print(f"Cluster {i+1}: {len(cluster)} elements")
        
        centroids = [0 for i in range(n_clusters)]

        for i,cluster in enumerate(clusters):
            centroid = np.array([elem['data'] for elem in cluster]).mean(axis=0)
            centroids[i] = centroid
        
        for i, cluster in enumerate(clusters):
            min_dist = np.linalg.norm(np.array(cluster[0]['data']) - centroids[i])
            min_elem = None
            for elem in cluster:
                dist = np.linalg.norm(np.array(elem['data']) - centroids[i])
                if dist <= min_dist:
                    min_dist = dist
                    min_elem = elem
            print(f"Cluster {i+1}: Closest element to centroid: {min_elem['id']}")


if __name__ == '__main__':
    main()