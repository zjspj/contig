import pandas as pd
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt

def make_list(this):
    x = open(this)
    contents = x.read()
    x.close()
    print(len(contents))
    contents.replace("N", " ")
    contents = contents.split()
    content = []
    for i in contents:
        content.append(len(i))
    print(len(content))
    content.sort()
    return content

def generate_df(content):
    df = pd.DataFrame({"first": content})
    df = pd.value_counts(df["first"]).to_frame().reset_index()
    df.columns = ['len', 'frequency']
    # df["cumulative frequency"] = df["frequency"].cumsum()
    return df


def main():
    x = make_list("my1.fasta")
    # y = make_list("my2.fasta")
    dfx = generate_df(x)
    sns.kdeplot(data = dfx, cumulative=True)
    plt.show()



    # print(df)

main()