class DataCleaner:
    @staticmethod
    def clean_data(raw_data):
        cleaned_data = []
        for item in raw_data:
            cleaned_item = item.strip().replace("\n", "")
            if cleaned_item:
                cleaned_data.append(cleaned_item)
        return cleaned_data

