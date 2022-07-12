import time

while True:
    time.sleep(5)
    with open("evaluator_data.txt", "r") as file:
        file.seek(0)
        check = file.readline()
        if check.isnumeric() is False:
            file.seek(0)
            artifact = file.read()
            artifact = artifact.split()
            evaluation = 0
            for counter in range(0, 4):
                if artifact[(counter * 2) + 2] == "HP":
                    evaluation += float(artifact[(counter * 2) + 3]) / 298.75
                if artifact[(counter * 2) + 2] == "ATK":
                    evaluation += float(artifact[(counter * 2) + 3]) / 19.45
                if artifact[(counter * 2) + 2] == "DEF":
                    evaluation += float(artifact[(counter * 2) + 3]) / 23.15
                if artifact[(counter * 2) + 2] == "HP%":
                    evaluation += float(artifact[(counter * 2) + 3]) / 5.83
                if artifact[(counter * 2) + 2] == "ATK%":
                    evaluation += float(artifact[(counter * 2) + 3]) / 5.83
                if artifact[(counter * 2) + 2] == "DEF%":
                    evaluation += float(artifact[(counter * 2) + 3]) / 5.83
                if artifact[(counter * 2) + 2] == "EM":
                    evaluation += float(artifact[(counter * 2) + 3]) / 23.31
                if artifact[(counter * 2) + 2] == "ER%":
                    evaluation += float(artifact[(counter * 2) + 3]) / 6.48
                if artifact[(counter * 2) + 2] == "CR":
                    evaluation += float(artifact[(counter * 2) + 3]) / 3.89
                if artifact[(counter * 2) + 2] == "CD":
                    evaluation += float(artifact[(counter * 2) + 3]) / 7.77
            evaluation = int(100 * (evaluation / 9))
            with open("evaluator_data.txt", "w") as file:
                file.write(str(evaluation))
