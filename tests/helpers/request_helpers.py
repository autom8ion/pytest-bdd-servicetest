import json
import requests


def post(url, headers=None, auth=None, data=None, cookies=None):

    data = json.dumps(data)
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, headers=headers, auth=auth,
                             data=data, cookies=cookies)

    return response


def put(url, headers=None, auth=None, params=None, data=None, cookies=None):

    data = json.dumps(data)
    print(data)
    requests.packages.urllib3.disable_warnings()
    response = requests.put(url, headers=headers, auth=auth, params=params,
                            data=data, cookies=cookies)

    return response



def patch(url, headers=None, auth=None, data=None, params=None, cookies=None):

    data = json.dumps(data)
    print(data)
    requests.packages.urllib3.disable_warnings()
    response = requests.put(url, headers=headers, auth=auth, params=params,
                            data=data, cookies=cookies)

    return response



def get(url, headers=None, auth=None, params=None, cookies=None):

    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, auth=auth, params=params, cookies=cookies)

    return response


def head(url, headers=None, auth=None, cookies=None):

    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, auth=auth, cookies=cookies)

    return response



def delete(url, headers=None, auth=None, cookies=None):

    requests.packages.urllib3.disable_warnings()
    response = requests.delete(url, headers=headers, auth=auth, cookies=cookies)

    return response



