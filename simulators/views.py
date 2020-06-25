from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'simulators/index.html'


class FundedSimulatorView(TemplateView):
    template_name = 'simulators/funded-simulator.html'


class DividendSimulatorView(TemplateView):
    template_name = 'simulators/dividend-simulator.html'


class FlatPriceSaleView(TemplateView):
    template_name = 'simulators/flat-price-sale.html'
