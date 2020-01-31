import time

import pandas as pd


if __name__ == "__main__":
    pd.set_option("display.max_rows", None)

    df = pd.read_excel("data.xlsx")
    print(df)
    print("-" * 36)

    start = int(input("起点ID："))
    df["distance"] = (
        (df["x"] - df.loc[start, "x"]) ** 2 + (df["y"] - df.loc[start, "y"]) ** 2
    ) ** (1 / 2)
    df = df.drop(index=start)
    result = df.sort_values(by="distance").reset_index(drop=True)
    result["accumulated"] = result["distance"].cumsum()

    method = int(input("1.按总距离; 2.按stop; 3.按距离;\n>> "))
    if method not in [1, 2, 3]:
        exit()
    elif method == 1:
        cumsum_dis = float(input("总距离:"))
        print(result[result.accumulated < cumsum_dis])
    elif method == 2:
        limit = int(input("多少stop："))
        print(result.head(limit))
    else:
        max_dis = float(input("距离上限:"))
        print(result[result.distance < max_dis])

time.sleep(1)
print("谢谢使用!")
