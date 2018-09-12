
from lcp_app_calls import *


mv = (post_mvs('mv.json', prefix='post_mvs', timestamp=True, open_file=False, del_file=True))
mv_url = get_self_link(mv)
print json_display(mv)


#mv_delegate = (post_mv_delegates('mv-delegate.json', prefix='post_mv-delegate', timestamp=True, open_file=False,
#                                   del_file=True))
#mv_url = get_mv_link(mv_delegate)
#print json_display(mv_delegate)


order = (post_orders('order.json', mv_url=mv_url, prefix='post_orders', timestamp=True, open_file=False, del_file=True))
order_url = get_self_link(order)
print json_display(order)
print json_display(patch_mv(mv_url, order_url))


credit = (post_credits('credit.json', mv_url=mv_url, prefix='post_credits', timestamp=True, open_file=False, del_file=True))
print json_display(credit)

#debit = (post_debits('debit.json', mv_url=mv_url, prefix='post_debits', timestamp=True, open_file=False, del_file=True))
#print json_display(debit)


#credit_order = (post_credit_order('credit-order.json', mv_url=mv_url, prefix='post_credit-order', timestamp=True,
#                                  open_file=False, del_file=True))
#print json_display(credit_order)


#debit_order = (post_debit_order('debit-order.json', mv_url=mv_url, prefix='post_debit-order', timestamp=True,
#                                  open_file=False, del_file=True))
#print json_display(debit_order)


