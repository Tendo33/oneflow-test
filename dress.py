import numpy as np
import math
import matplotlib.pyplot as plt
import json
import os
import argparse

parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--path', '-n', help='path属性')

args = parser.parse_args()

total_loss_values = []
total_x = []
total_y = []


for root, dirs, files in os.walk(args.path):

    for file in files:
        
        if file.endswith('.json'):

            try:
                with open(os.path.join(root, file), 'r', encoding="utf-8", newline="\n") as f:
                    com_x = []
                    dev_y = []
                    for line in f.readlines():
                        dev_data = json.loads(line)
                        
                        dev_y.append(dev_data['total_loss'])
                        com_x.append(dev_data["iteration"])

            except Exception as e:
                print(f"Error opening file {os.path.join(root, file)}: {e}")
    
            total_y.append(dev_y)
            total_x.append(com_x)

new_total_y = []
new_total_x = []
for i in range(len(total_y)):
    if len(total_y[i]) >= 10:
        new_total_y.append(total_y[i])
        new_total_x.append(total_x[i])


for i in range(0, len(total_y), 3):

    plt.plot(new_total_x[i],new_total_y[i],label="master")
    plt.plot(new_total_x[i + 1],new_total_y[i + 1],label="naive",linestyle = "--")
    plt.plot(new_total_x[i + 2],new_total_y[i + 2],label="rank_per_process",linestyle = ":")
    plt.xlabel("iteration")
    plt.ylabel("total_loss")
    plt.title('DP2_MP2_PP2_zerofalse_stage0_mbs32_gbs512_acc8_1n8g')
    plt.legend()   #打上标签
    plt.savefig("./LibAI_bert_large_pretrain_graph_nl24_nah16_hs1024_FP16_actrue_DP2_MP2_PP2_zerofalse_stage0_mbs32_gbs512_acc8_1n8g,png")



