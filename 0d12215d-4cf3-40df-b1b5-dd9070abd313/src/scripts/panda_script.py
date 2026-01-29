import pandas as pd

def create_panda():
    print("[Panda] Creating a Panda (Dataframe)...")
    df = pd.DataFrame({"Name": ["Panda"], "Type": ["Bear"], "Activity": ["Eating Bamboo"]})
    print(df)
    return df

if __name__ == "__main__":
    create_panda()
