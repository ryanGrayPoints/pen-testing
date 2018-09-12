
import subprocess
import json
import datetime
import re


########################################################################################################################
def open_del(filename, open_file=False, del_file=True):
    if open_file is True:
        subprocess.call(filename, shell=True)
    if del_file is True:
        subprocess.call('del ' + filename, shell=True)


########################################################################################################################
def read_json_doc(json_doc, open_file=False, del_file=True):
    try:
        with open(json_doc, 'r') as json_file:
            json_object = json.load(json_file)
        open_del(json_doc, open_file, del_file)
    except:
        json_object = {}
    return json_object


########################################################################################################################
def json_dict_to_str(json_dict):
    temp_str = str(json_dict)
    json_str = temp_str.replace('"', '\\"').replace("'", '\\"').replace(', u\\', ', \\').replace(': u\\', ': \\'). \
        replace('{u\\', '{\\').replace('[u\\', '[\\')
    return json_str


########################################################################################################################
def json_display(json_dict):
    json_str = str(json_dict)
    output_str = json_str.replace("'", '"').replace('{u"', '{"').replace('[u"', '["').replace('', '').\
        replace(', u"', ', "').replace(': u"', ': "').replace(',', ',\n').replace('{', '{\n')
    return output_str


########################################################################################################################
def create_filename(prefix):
    date_str = str(datetime.datetime.now())
    timestamp = re.sub('[^0-9]', '', date_str)
    filename = prefix + '_' + timestamp
    return filename

