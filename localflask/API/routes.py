from flask import jsonify, current_app
from flask import Blueprint
from Services.Download import proxy
import json

blueprint_api = Blueprint('api', __name__)


@blueprint_api.route("/name")
def name():
    return jsonify({"names": "s = d"})


@blueprint_api.route("/add_random")
def add_random():
    return jsonify({"added": "s = d"})


@blueprint_api.route("/create_db")
def createdb():
    from API.DataBase.database import CurrentBaseAPI
    CurrentBaseAPI.init_db()
    return jsonify({"результат": "База создана"})


# получение текущего ip-адреса из яндекса
@blueprint_api.route("/ipaddress")
def ipaddr():
    ipa = proxy.Proxy.getCurrentIPAddress(None)
    if not ipa is None:
        from API.DataBase.Models import ipaddress
        ipad = ipaddress.IPAddress(ipa)
        ipad.save()
        return jsonify({"responce":
                            {"описание": "адрес добавлен",
                             "id": f"{ipad.id}",
                             "address": f"{ipad.address}",
                             "created_date": f"{ipad.created_date}"
                             }})
    return jsonify({"responce":
                        {"описание": "адрес неопределн",
                         "id": f"",
                         "address": f"",
                         "created_date": f""
                         }})


@blueprint_api.route("/lastipaddress")
def lastipaddress():
    from API.DataBase.Models import ipaddress
    ipad = ipaddress.IPAddress.lastipaddress()
    # return jsonify({"responce":
    #                     {"описание": "последний адрес",
    #                      "id": f"{ipad.id}",
    #                      "address": f"{ipad.address}",
    #                      "created_date": f"{ipad.created_date}"
    #                      }})
    return jsonify(
        id=ipad.id,
        address=ipad.address,
        created_date=ipad.created_date
    )


@blueprint_api.route("/ipaddress/<id>")
def find(id):
    from API.DataBase.Models import ipaddress
    ipad = ipaddress.IPAddress.find(id)
    return jsonify({"responce":
                        {"описание": "получен из яндекса ip-адрес",
                         "id": f"{ipad.id}",
                         "address": f"{ipad.address}",
                         "created_date": f"{ipad.created_date}"
                         }})


@blueprint_api.route("/getlistproxies")
def listproxies():
    from API.DataBase.Models import proxies
    from Services.Download.proxy import Proxy
    proxs = Proxy.getListProxies()
    for p in proxs:
        proxy = proxies.Proxy(p.address, p.port, p.type, p.country)
        proxy.save()
    return jsonify({"responce":
                        {"описание": "получен из яндекса ip-адрес",
                         "id": f"",
                         "address": f"",
                         "created_date": f""
                         }})
