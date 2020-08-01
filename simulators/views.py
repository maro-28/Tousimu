from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'simulators/index.html'


class FundedSimulatorView(TemplateView):
    template_name = 'simulators/funded-simulator.html'


class DividendSimulatorView(TemplateView):
    template_name = 'simulators/dividend-simulator.html'


class FlatPriceSaleView(TemplateView):
    template_name = 'simulators/flat-price-sale.html'


class TermsView(TemplateView):
    template_name = 'simulators/terms.html'


class PrivacyView(TemplateView):
    template_name = 'simulators/privacy.html'

class InfoView(TemplateView):
    template_name = 'simulators/info.html'
