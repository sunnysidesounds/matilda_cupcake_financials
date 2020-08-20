from config import Configuration


class FinancialCalculator(object):

    @staticmethod
    def calculate_revenue(model):
        if model['type'] == 'total':
            total = sum([r['amount'] for r in model['model']])
            model['revenue'] = "${:,.2f}".format(total)
        elif model['type'] == 'basic':
            total = sum([Configuration.cost_of_basic * r['amount'] for r in model['model']])
            model['revenue'] = "${:,.2f}".format(total)
        elif model['type'] == 'delux':
            total = sum([Configuration.cost_of_delux * r['amount'] for r in model['model']])
            model['revenue'] = "${:,.2f}".format(total)
        return model