import pandas

csv_og = pandas.read_csv('test_og.csv') 
csv_all = pandas.read_csv('test_all.csv') 

csv_og.columns = csv_og.columns.str.strip()
csv_all.columns = csv_all.columns.str.strip()

csv_nodupes = csv_all[~csv_all[['row1', 'row2']].apply(tuple, axis=1).isin(csv_og[['row1', 'row2']].apply(tuple, axis=1))]
csv_nodupes.to_csv('csv_nodupes.csv', index=False) 
