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

    def filter_model_by_args(self, args):
        results_model = ModelBuilder.build_results_model()
        results_model['type'] = args.type
        results_model['model'] = self.model[args.type]
        if args.year:
            results_model['year'] = int(args.year)
            # filter to year
            results_model['model'] = [m for m in results_model['model'] if m['year'] == results_model['year']]

        if args.month:
            results_model['month'] = int(args.month)
            # filter to month
            results_model['model'] = [m for m in results_model['model'] if m['month'] == results_model['month']]

        if args.week:
            results_model['week'] = int(args.week)
            # filter to week
            results_model['model'] = [m for m in results_model['model'] if m['week'] == results_model['week']]

        results_model['count'] = sum([r['amount'] for r in self.model[args.type]])

        return results_model

    @staticmethod
    def build_results_model():
        return {
            "revenue": 0,  # dollar amount formatted
            "year": None,
            "week": None,
            "month": None,
            "type": None,  # basic, delux, total
            "model": None,
            "count": None
        }

