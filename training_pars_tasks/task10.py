# 10. Like 9

import json
import re

RESPONSE = "RESPONSE@HEADER@customer_info={customer_name:John Doe;customer_email:johndoe@example.com;" \
       "customer_phone:123-456-7890}order_details={order_id:5678;order_date:2023-04-18;order_items=" \
       "{product_name:apple;quantity:5}{product_name:banana;quantity:3}{product_name:orange;quantity:2}}payment_info=" \
       "{payment_method:credit_card;payment_amount:15.99}@"

def pars_tcp_response(data):
    pattern_customer_info = r'customer_info=\{([\w:;@. -]+)\}'
    customer_info_data = re.findall(pattern_customer_info, data)
    collect_data = {"customer_info": customer_info_data[0]}
    pattern_order_details = r'order_details=\{([\w:;@. -\}\{]+)\}payment_info'
    order_details_data = re.findall(pattern_order_details, data)
    collect_data['order_details'] = order_details_data[0]
    pattern_order_items = r'\{([\w:;]+)\}'
    order_items_data = re.findall(pattern_order_items, *order_details_data)
    collect_data['order_items'] = order_items_data
    pattern_payment_info = r'payment_info=\{([\w:;\., -]+)\}'
    payment_info_data = re.findall(pattern_payment_info, data)
    collect_data['payment_info'] = payment_info_data[0]
    return collect_data


def format_to_dict(text):
    return dict(key_item.split(':') for key_item in text.split(';') if key_item)


def collect_result(collect_data):
    data_dict = {'customer_info': format_to_dict(collect_data['customer_info'])}
    order_details_info = collect_data['order_details'].split(";", 2)[:2]
    data_dict['order_details'] = dict(key_item.split(':') for key_item in order_details_info)
    data_dict['order_details']['order_items'] = [format_to_dict(item) for item in collect_data['order_items']]
    data_dict['payment_info'] = format_to_dict(collect_data['payment_info'])
    return data_dict


def dict_to_json(dict_obj):
    return json.dumps(dict_obj)

collect_data = pars_tcp_response(RESPONSE)
dict_response = collect_result(collect_data)
print(dict_response)

json_str_response = dict_to_json(dict_response)
print(json_str_response)