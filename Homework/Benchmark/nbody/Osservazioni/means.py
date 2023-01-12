for i in range(40):
    with open(f"output{i}.txt", "r") as f:
        lines = f.readlines()
        vals = [float(line.split(' ')[1]) for line in lines]
        print(f"{str(sum(vals)/len(vals)).replace('.', ',')}")

