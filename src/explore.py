from loader import load_all_data

data = load_all_data()

for name, df in data.items():
    print("\n" + "=" * 80)
    print(f" FILE: {name}")
    print("=" * 80)

    print("\nShape:")
    print(df.shape)


    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 3 Rows:")
    print(df.head(3))