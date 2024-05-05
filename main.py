from rentfinder import RentFinder
from formfiller import FormFiller


finder = RentFinder()
filler = FormFiller()
prices = finder.get_prices()
links = finder.get_links()
addresses = finder.get_addresses()
filler.fill_out_form(prices, links, addresses)
# filler.make_sheet()  #  Selenium opening Chrome won't let me sign into google to finish this step