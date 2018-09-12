
from lcp_json import *

app_creds = '' #<MAC Key Identifier>:<MAC Key>


########################################################################################################################
def create_payload_str(payload, trans_type='', mv_url=''):
    if isinstance(payload, dict):
        temp_dict = payload
    elif isinstance(payload, str):
        temp_dict= read_json_doc(payload, del_file=False)
    else:
        return '{"errors": [{"code": "PAYLOAD_OF_INVALID_TYPE"}]}'

    if mv_url != '':
        if trans_type == 'order':
            if "data" in temp_dict:
                if "user" in temp_dict["data"]:
                    temp_dict["data"]["user"]["memberValidation"] = mv_url
                else:
                    temp_dict["data"]["user"] = {"memberValidation": mv_url}
            else:
                temp_dict["data"] = {"user": {"memberValidation": mv_url}}
        elif trans_type in ('credit', 'debit', 'credit-order', 'debit-order'):
            temp_dict["memberValidation"] = mv_url

    payload_str = json_dict_to_str(temp_dict)
    return payload_str


########################################################################################################################
def get_lcp(url, credentials=app_creds, filename='get_lcp.json', open_file=False, del_file=True):
    subprocess.call('python lcp_curl.py -u ' + credentials + ' -X GET ' + url + ' > ' + filename, shell=True)
    try:
        json_object = read_json_doc(filename, open_file, del_file)
    except:
        json_object = {"errors": [{"code": "BAD_REQUEST"}]}
    return json_object


########################################################################################################################
def post_lcp(url, payload, trans_type='', mv_url='', credentials=app_creds, filename='post_lcp.json', open_file=False,
             del_file=True):
    payload_str = create_payload_str(payload, trans_type, mv_url)
    subprocess.call('python lcp_curl.py -u ' + credentials + ' -X POST -d "' + payload_str + '" "' + url + '" > ' +
                    filename, shell=True)
    try:
        json_object = read_json_doc(filename, open_file, del_file)
    except:
        json_object = {"errors": [{"code": "BAD_REQUEST"}]}
    return json_object


########################################################################################################################
def patch_lcp(url, payload, credentials=app_creds, filename='put_lcp.json', open_file=False, del_file=True):
    payload_str = create_payload_str(payload)
    subprocess.call('python lcp_curl.py -u ' + credentials + ' -X PATCH -d "' + payload_str + '" "' + url + '" > ' +
                    filename, shell=True)
    try:
        json_object = read_json_doc(filename, open_file, del_file)
    except:
        json_object = {"errors": [{"code": "BAD_REQUEST"}]}
    return json_object


########################################################################################################################
def put_lcp(url, payload, credentials=app_creds,  filename='put_lcp.json', open_file=False, del_file=True):
    payload_str = create_payload_str(payload)
    subprocess.call('python lcp_curl.py -u ' + credentials + ' -X PUT -d "' + payload_str + '" "' + url + '" > ' +
                    filename, shell=True)
    try:
        json_object = read_json_doc(filename, open_file, del_file)
    except:
        json_object = {"errors": [{"code": "BAD_REQUEST"}]}
    return json_object


########################################################################################################################
def delete_lcp(url, credentials=app_creds, filename='del_lcp.json', open_file=False, del_file=True):
    subprocess.call('python lcp_curl.py -u ' + credentials + ' -X DELETE ' + url + ' > ' + filename, shell=True)
    try:
        json_object = read_json_doc(filename, open_file, del_file)
    except:
        json_object = {"errors": [{"code": "BAD_REQUEST"}]}
    return json_object
