import pandas as pd

def to_accumulated(xs): 
    o = [xs[0]]
    for i in xs[1:]:o.append(o[-1]+i)
    return o

def main():
    df = pd.read_csv("../rawdata/federal_register_page_count_published_per_category-2-clean-a.csv")
    df = df.set_index("Year")
    df = df.rename(columns={"Presidential Documents": "presidential", "Rules": "rules", "Proposed Rules": "proposed_rules", "Notices": "notices", "Unknowns": "unknowns", "Corrections": "corrections", "TOTAL†": "total", "ACTUAL‡": "actual"})

    indx = df.index.to_list()

    
    
    print(df)

if __name__ == "__main__":
    main()
