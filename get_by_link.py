import requests
import json
from utils import get_random_header
from proxy.generate_proxy import get_proxy
import sys


def get_variats(props, attrs, sku_model):
    """
    getting variants info
    such as price, name, sale_count and stock_amount

    :param props:
    :param attrs:
    :param sku_model:

    :return:
    """
    variant_list = []
    for i in props[0]["value"]:
        attr_list = []
        for attr in attrs:
            if i["name"] in attr:
                prod = attrs[attr]
                try:
                    price = prod["price"]
                except KeyError as error:
                    print(error)
                    # seems to be default price for all vars
                    # todo: price can be shit
                    price = sku_model["skuPriceScale"]

                if "-" in price:
                    price = price.split("-")[-1]

                name = prod["specAttrs"].split(";")[-1]
                # print('shit schema')
                res_ = {
                    "price": price,
                    "name": name,
                    "saleCount": prod["saleCount"],
                    "canBookCount": prod["canBookCount"],
                }
                attr_list.append(res_)
        variant_list.append({**i, "subvariants": attr_list})
    return variant_list


def get_details(details):
    """
    returns details at the bottom of the page
    """
    return [{"name": d["name"], "values": d["values"]} for d in details]


def get_prod_by_link(url, CERT_PATH):
    # url = sys.argv[1]
    session = requests.Session()

    # set proxy here
    response = session.get(
        url,
        verify=CERT_PATH,
        headers=get_random_header(),
        proxies=get_proxy(),
        timeout=20,
    ).text

    body = response.split("<script>")[6]
    start, end = "window.__INIT_DATA=", "</script>"
    res = json.loads(body.split(start)[-1].split(end)[0])

    product = {}

    product["prices"] = res["globalData"]["orderParamModel"]["orderParam"]["skuParam"]
    product["title"] = res["globalData"]["tempModel"]["offerTitle"]
    subvar_product_amount = res["globalData"]["orderParamModel"]["orderParam"]

    sku_model = res["globalData"]["skuModel"]
    try:
        props = sku_model["skuProps"]
        attrs = sku_model["skuInfoMap"]
        product["variants"] = get_variats(props, attrs, sku_model)

        try:
            product["variant_name"] = props[0]["prop"]
            product["subvariant_name"] = props[1]["prop"]
        except KeyError as error:
            print(error)
            product["subvariant_name"] = props[0]["prop"]
            product["variant_name"] = "default"

    except KeyError as exception:
        print(exception)
        print("no sku props")
        product["variant_name"] = "default"
        product["subvariant_name"] = "default_1"
        # shit subvar price
        sub_price = product["prices"]["skuRangePrices"]["price"]
        product["variants"] = [
            {
                "imageUrl": "",
                "name": product["title"],
                "subvariants": [
                    {
                        "price": sub_price,
                        "name": product["title"],
                        "saleCount": subvar_product_amount["saledCount"],
                        "canBookCount": subvar_product_amount["canBookedAmount"],
                    }
                ],
            }
        ]

    for _, value in res["data"].items():
        if not isinstance(value, bool) and not isinstance(value, list):
            try:
                # if value['componentType'] == '@ali/tdmod-od-pc-offer-price':
                if value["componentType"] == "@ali/tdmod-od-pc-attribute-new":
                    product["details"] = get_details(value["data"])
            except KeyError as error:
                print(error)
                continue
            except TypeError as error:
                print(error)
                continue

    image_list = []
    for image in res["globalData"]["images"]:
        try:
            image_list.append(
                {
                    "url": image["fullPathImageURI"],
                    "preview": image["size220x220ImageURI"],
                }
            )
        except KeyError as error:
            print(error)

    product["images"] = image_list
    product["title"] = res["globalData"]["tempModel"]["offerTitle"]
    product["saled_count"] = res["globalData"]["tempModel"]["saledCount"]
    # print(product)
    return json.dumps(product, indent=4, ensure_ascii=False)
    # return res


if __name__ == "__main__":
    # URL = "https://detail.1688.com/offer/706710213777.html"
    # 612579417533

    URL = sys.argv[1]
    CERT_PATH = sys.argv[2]
    # CERT_PATH = "./proxy/zyte-proxy-ca.crt"
    result = get_prod_by_link(URL, CERT_PATH)
    print(result)
    # with open("sample_1.json", "w") as outfile:
    # outfile.write(json.dumps(res, indent=4, ensure_ascii=False))
