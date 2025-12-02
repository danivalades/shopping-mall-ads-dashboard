from pathlib import Path
import kagglehub

# Kaggle dataset identifier from the Kaggle page
DATASET = "marceaxl82/shopping-mall-paid-search-campaign-dataset"


def download_data():
    # This downloads the dataset to a local cache (~/.cache/kagglehub/...)
    path = kagglehub.dataset_download(DATASET)
    print("Downloaded dataset to:", path)

    # Copy any CSVs into your project data/raw folder
    path = Path(path)
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    for csv_path in path.glob("*.csv"):
        target = raw_dir / csv_path.name
        target.write_bytes(csv_path.read_bytes())
        print(f"Copied {csv_path.name} -> {target}")


if __name__ == "__main__":
    download_data()
