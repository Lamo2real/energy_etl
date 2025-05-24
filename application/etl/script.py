
from extract import extract_energy_data
# from transform import transform_data
# from load import load_data

def main():
    data = extract_energy_data()
    # transformed = transform_data(data)
    # load_data(transformed)
    return data

if __name__ == "__main__":
    main()