
from lcp_api import *

lpid = '2d39854c-101b-43dd-a0c8-39188e700518'
base_url = 'https://staging.lcp.points.com/v1/'
lp_url = base_url + 'lps/' + lpid


########################################################################################################################
def post_mvs(json_payload, prefix='post_mvs', timestamp=True, open_file=False, del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(lp_url + '/mvs/', json_payload, filename=filename, open_file=open_file, del_file=del_file)


########################################################################################################################
def post_mv_delegates(json_payload, prefix='post_mv-delegates', timestamp=True, open_file=False, del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(lp_url + '/mv-delegates/', json_payload, filename=filename, open_file=open_file, del_file=del_file)


########################################################################################################################
def post_orders(json_payload, mv_url='', prefix='post_orders', timestamp=True, open_file=False, del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(base_url + 'orders/', json_payload, trans_type='order', mv_url=mv_url, filename=filename,
                    open_file=open_file, del_file=del_file)


########################################################################################################################
def post_credits(json_payload, mv_url='', prefix='post_credits', timestamp=True, open_file=False, del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(lp_url + '/credits/', json_payload, trans_type='credit', mv_url=mv_url, filename=filename,
                    open_file=open_file, del_file=del_file)


########################################################################################################################
def post_debits(json_payload, mv_url='', prefix='post_debits', timestamp=True, open_file=False, del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(lp_url + '/debits/', json_payload, trans_type='debit', mv_url=mv_url, filename=filename,
                    open_file=open_file, del_file=del_file)


########################################################################################################################
def post_credit_order(json_payload, mv_url='', prefix='post_credit-order', timestamp=True, open_file=False,
                      del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(lp_url + '/credit-order/', json_payload, trans_type='credit-order', mv_url=mv_url,
                    filename=filename, open_file=open_file, del_file=del_file)


########################################################################################################################
def post_debit_order(json_payload, mv_url='', prefix='post_debit-order', timestamp=True, open_file=False,
                     del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return post_lcp(lp_url + '/debit-order/', json_payload, trans_type='debit-order', mv_url=mv_url, filename=filename,
                    open_file=open_file, del_file=del_file)


########################################################################################################################
def get_self_link(json_response):
    if isinstance(json_response, dict):
        json_dict = json_response
    elif isinstance(json_response, str):
        json_dict = read_json_doc(json_response, del_file=False)
    else:
        return '{"errors": [{"code": "INVALID_ARGUMENT_TYPE"}]}'
    try:
        self_link = json_dict["links"]["self"]["href"]
    except:
        self_link = '{"errors": [{"code": "NOT_FOUND", "description": "links.self.href not found"}]}'
    return self_link


########################################################################################################################
def get_mv_link(json_response):
    if isinstance(json_response, dict):
        json_dict = json_response
    elif isinstance(json_response, str):
        json_dict = read_json_doc(json_response, del_file=False)
    else:
        return '{"errors": [{"code": "INVALID_ARGUMENT_TYPE"}]}'
    try:
        mv_link = json_dict["memberValidation"]
    except:
        mv_link = '{"errors": [{"code": "NOT_FOUND", "description": "links.self.href not found"}]}'
    return mv_link


########################################################################################################################
def patch_mv(mv_url, order_url, prefix='patch_mv', timestamp=True, open_file=False, del_file=True):
    if timestamp is True:
        filename = create_filename(prefix)
    else:
        filename = prefix
    return patch_lcp(mv_url, {"order": order_url}, filename=filename, open_file=open_file, del_file=del_file)



