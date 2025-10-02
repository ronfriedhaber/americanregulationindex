import pandas as pd
import json

def to_accumulated(xs): 
    xs = xs.fillna(0.0).to_list()
    o = [xs[0]]
    for i in xs[1:]:o.append(o[-1]+i)
    return o

def main():
    df = pd.read_csv("../rawdata/federal_register_page_count_published_per_category-2-clean-a.csv")
    df = df.set_index("Year")
    df = df.rename(columns={"Presidential Documents": "presidential", "Rules": "rules", "Proposed Rules": "proposed_rules", "Notices": "notices", "Unknowns": "unknowns", "Corrections": "corrections", "TOTAL†": "total", "ACTUAL‡": "actual"})
    df = df.iloc[::-1]

    indx = df.index.to_list()

    for col in df.columns: 
        df[col] = [(float(i.replace(",", "")) if i != "-" else 0.0) if isinstance(i, str) else i for i in df[col]]

    not_accumulated = {
        "total": df["total"].to_list(),
        "actual": df["actual"].to_list(),
        "presidential": df["presidential"].to_list(),
    }
    accumulated = {
        "total": to_accumulated(df["total"]),
        "actual": to_accumulated(df["actual"]),
        "presidential": to_accumulated(df["presidential"])
    }
    
    print(df)

    data = {
        "x_axis": indx,
        "not_accumulated": not_accumulated,
        "accumulated": accumulated
    }

    with open("../app/src/lib/data/a.json", "w") as f: f.write(json.dumps(data).replace("NaN", "null"))

    return data

if __name__ == "__main__":
    main()
