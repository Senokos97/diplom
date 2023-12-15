import configuration
import data
import requests
import string


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def creation_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


def order_track():
    response = creation_order(data.body)
    return response.json().get('track')


def get_order_on_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))
