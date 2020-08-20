import os
from config import Configuration
from datetime import datetime, timedelta


class ModelBuilder(object):

    def __init__(self):
        self.model = {"basic": [], "delux": [], "total": []}

    def get_model(self):
        self.build_models()
        return self.model

    def build_model(self, filename, model):
        index = 0
        date = None
        for line in reversed(list(open(filename))):
            if index == 0:
                date = datetime.today()
            else:
                date = (date-timedelta(days=1))

            number = str(line.strip())
            if number.isdigit():
                number = int(number)
            else:
                number = 0
            model.append({"date": date.strftime("%m-%d-%Y"),
                          "amount": int(number),
                          "week": int(date.isocalendar()[1]),
                          "year": int(date.strftime("%Y")),
                          "day": int(date.strftime("%d")),
                          "month": int(date.strftime("%m"))})

            index += 1

    def build_models(self):

        self.build_model(os.path.join(Configuration.storage_path, Configuration.data_files[0]), self.model['basic'])
        self.build_model(os.path.join(Configuration.storage_path, Configuration.data_files[1]), self.model['delux'])
        self.build_model(os.path.join(Configuration.storage_path, Configuration.data_files[2]), self.model['total'])

    @staticmethod
    def build_results_model():
        return {
            "revenue": 0,  # dollar amount formatted
            "year": None,
            "week": None,
            "month": None,
            "type": None,  # basic, delux, total
            "model": None
        }

