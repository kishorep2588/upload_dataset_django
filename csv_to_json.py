import pandas as pd
import json

csv_file_name = 'electronics_product.csv'
json_file_name = 'electronics_product.json'

csv_file = pd.DataFrame(pd.read_csv(csv_file_name, sep = ",", header = 0, index_col = False))
csv_file.to_json(json_file_name, orient = "records", date_format = "epoch", double_precision = 10, 
                 force_ascii = True, date_unit = "ms", default_handler = None,
                 indent=4)
