import pandas as pd


class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_sheets(self):
        try:
            sheet_names = pd.ExcelFile(self.filepath).sheet_names
            return sheet_names
        except FileNotFoundError:
            print(f"Error: The file at {self.filepath} was not found.")
            return None
        
    def read_data(self, sheet_name):
        try:
            data = pd.read_excel(self.filepath, sheet_name=sheet_name)
            return data
        except Exception as e:
            print(f"Error reading sheet {sheet_name}: {e}")
            return None
             
        
data = DataProcessor('data\kenya_hotels_detailed_data.xlsx')
# print(data.read_sheets())

meta_data = data.read_data('Hotel_Metadata')

# print(meta_data.columns)

# print(meta_data['original_image'].iloc[0])


