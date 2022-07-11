import json
from json2html import *
import urllib.request
from models.Catalog import Catalog


class APIData:

    def __init__(self):
        data_json = APIData.fetch_data()
        self.__data: Catalog = Catalog(**data_json)

    @staticmethod
    def fetch_data():
        try:
            data = urllib.request.urlopen("https://backend-assignment.bylith.com/index.php")
            parsed_data = data.read()
            data_encoded = data.info().get_content_charset('utf8')
            return json.loads(parsed_data.decode(data_encoded))

        except Exception as e:
            print(f"fail to retrieve data from API\n Error code: {e}")

    def get_products(self):
        return self.__data.products

    def get_attributes(self):
        return self.__data.attributes

    def get_categories(self):
        categories = set()
        categories_dict = dict()

        for prod in self.get_products():
            for cat in prod.categories:
                categories.add(cat)

        for cat in categories:
            categories_dict.update({cat: self.count_categories(cat)})

        return list(categories_dict.items())

    def count_categories(self, category):
        res = 0
        for prod in self.get_products():
            for cat in prod.categories:
                if cat.id == category.id:
                    category.counter += 1
                    res += 1
        return res

    def init_html(self):
        with open("Table.html", "w") as html_file:
            html_file.write("<h1>Dor's Catalog:</h1>")
            html_file.write("<h2>Products:</h2>")
            html_file.write(json2html.convert(
                json.dumps(self.get_products(), default=lambda o: o.__dict__, sort_keys=False, indent=2)))
            html_file.write("<h2>Attributes: </h2>")
            html_file.write(json2html.convert(
                json.dumps(self.get_attributes(), default=lambda o: o.__dict__, sort_keys=False, indent=2)))
            html_file.write("<h2>Categories: </h2>")
            html_file.write(json2html.convert(
                json.dumps(self.get_categories(), default=lambda o: o.__dict__, sort_keys=False, indent=2)))
