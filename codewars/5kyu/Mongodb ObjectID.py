import re
from datetime import datetime


class Mongo:
    @staticmethod
    def is_valid(s):
        return isinstance(s, str) and re.fullmatch(r'[0-9a-f]{24}', s) is not None

    @staticmethod
    def get_timestamp(s):
        if Mongo.is_valid(s):
            timestamp = int(s[:8], 16)  # Convert the first 8 hex digits to a decimal timestamp
            return datetime.utcfromtimestamp(timestamp)
        return False


if __name__ == "__main__":
    print(Mongo.is_valid("507f1f77bcf86cd799439011"))  # True
    print(Mongo.get_timestamp("507f1f77bcf86cd799439011"))  # 2012-10-17 21:13:27
