# CSV Duplicate Remover

**The easiest CSV cleaner on GitHub** 🚀

A simple Python script that removes duplicate rows from CSV files by comparing against a reference dataset. Perfect for data cleaning and deduplication tasks.

## What it does

This script compares two CSV files:
- **Reference file** (`test_og.csv`): Contains the data you want to keep
- **Target file** (`test_all.csv`): Contains all data including potential duplicates
- **Output**: Creates `csv_nodupes.csv` with only the unique rows from the target file that don't exist in the reference file

## Features

- ✅ Simple and lightweight
- ✅ Uses pandas for efficient data processing
- ✅ Handles column name whitespace automatically
- ✅ Compares based on multiple columns (`row1` and `row2`)
- ✅ No external dependencies beyond pandas

## Requirements

- Python 3.6+
- pandas

## Installation

1. Clone this repository:
```bash
git clone https://github.com/zixihong/simple-csv-dupe-remover.git
cd simple-csv-dupe-remover
```

2. Install dependencies:
```bash
pip install pandas
```

## Usage

1. Prepare your CSV files:
   - `test_og.csv` - Your reference dataset (the "good" data)
   - `test_all.csv` - Your full dataset (may contain duplicates)

2. Run the script:
```bash
python duplicate_remover.py
```

3. Check the output:
   - `csv_nodupes.csv` - Contains only unique rows not found in the reference file

## File Structure

```
├── duplicate_remover.py    # Main script
├── test_og.csv            # Reference dataset
├── test_all.csv           # Full dataset
├── csv_nodupes.csv        # Output (generated)
└── README.md              # This file
```

## How it works

The script performs the following steps:

1. **Load datasets**: Reads both CSV files using pandas
2. **Clean column names**: Strips whitespace from column headers
3. **Compare data**: Uses tuple comparison on `row1` and `row2` columns to find duplicates
4. **Filter results**: Keeps only rows from `test_all.csv` that don't exist in `test_og.csv`
5. **Export**: Saves the filtered results to `csv_nodupes.csv`

## Example

If you have:
- `test_og.csv`: Contains rows A, B, C
- `test_all.csv`: Contains rows A, B, C, D, E, F

The output `csv_nodupes.csv` will contain: D, E, F (only the unique rows not in the reference)

## Customization

To modify the script for your specific needs:

1. **Change column names**: Update `['row1', 'row2']` to your actual column names
2. **Add more columns**: Include additional columns in the comparison tuple
3. **Modify file names**: Change the input/output file names as needed

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Made with ❤️ for easy data cleaning**