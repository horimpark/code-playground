class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        split_fn = dirty_file_name.split(".")
        extension = split_fn[1]
        file_name = "_".join(split_fn[0].split("_")[1:])
        return f"{file_name}.{extension}"
