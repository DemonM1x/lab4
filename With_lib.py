from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import json
def start(input_file, output_file):
    with open(input_file, 'r') as f1:
        with open(output_file, 'w') as f2:
            data = json.load(f1)
            f2.write(json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())

start("Tuesdayj.json","Tuesdayx3.xml")