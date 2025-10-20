import pandas as pd
import json

def to_accumulated(xs): 
    xs = xs.fillna(0.0).to_list()
    o = [xs[0]]
    for i in xs[1:]:o.append(o[-1]+i)
    return o

def main():
    df = pd.read_csv("../rawdata/GFDEBTN.csv")
    print(df)
    # quit()
    df = df.set_index("observation_date")
    # df = df.iloc[::-1]

    indx = df.index.to_list()

    for col in df.columns: 
        df[col] = [(float(i.replace(",", "")) if i != "-" else 0.0) if isinstance(i, str) else i for i in df[col]]

    labels = ["GFDEBTN"]

    not_accumulated = {
        label: df[label].to_list()
        for label in labels
    }
    accumulated = {
        label: to_accumulated(df[label])
        for label in labels
    }
    
    print(df)

    data = {
        "x_axis": indx,
        "not_accumulated": not_accumulated,
        "accumulated": accumulated
    }

    with open("../app/src/lib/data/c.json", "w") as f: f.write(json.dumps(data).replace("NaN", "null"))

    return data

if __name__ == "__main__":
    main()
