from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """
    静的ページのサイトマップ
    """
    changefreq = "daily"

    # クローラーに対するページの重要度 デフォルトは0.5
    priority = 0.5

    def items(self):
        return ['simulators:index', 'simulators:funded-simulator', 'simulators:dividend-simulator', 'simulators:flat-price-sale', 'simulators:terms', 'simulators:privacy',]

    def location(self, item):
        return reverse(item)
