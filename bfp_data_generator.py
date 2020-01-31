import pandas as pd
import numpy as np


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":

    df = pd.DataFrame(
        [
            map(str, range(0, 100)),
            np.random.normal(10, 2, 100),
            np.random.uniform(1, 5, 100),
        ]
    ).T
    df.columns = ["id", "x", "y"]
    df.to_excel("data.xlsx", index=False)
