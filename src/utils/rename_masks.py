# Converts row in csv file
# LC08_L1TP_166067_20200816_20200816_01_RT_p00669.tif
# LC08_L1GT_016028_20200821_20200822_01_RT_voting_p00667.tif

# Algorithm: voting/intersection
algorithm = "voting"
# Model: unet_64f_2conv_762/unet_64f_2conv_10c/unet_16f_2conv_762
model = "unet_64f_2conv_762"

FILE_PATH = f"../train/{algorithm}/{model}/dataset/masks_test.csv"

with open(FILE_PATH, mode="r", encoding="utf-8") as f:
    data = f.read().split("\n")[:-1]

    for i in range(len(data)):
        if "_voting_" not in data[i]:
            data[i] = data[i].replace("_RT_", "_RT_voting_")

with open(FILE_PATH, mode="w", encoding="utf-8") as f:
    for row in data:
        f.write(row + "\n")

print("Done!")
