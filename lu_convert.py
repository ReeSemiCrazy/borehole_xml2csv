import os
import csv
import xml.etree.ElementTree as ET

def xml2dict(xml_file):
    with open(xml_file, "r") as f:
        xml_string = f.read()
        root = ET.fromstring(xml_string)
        result_row = {}

        for i in range(1,99):
            for param in root.findall('.//总体参数'):
                for borehole in param.findall('.//钻孔编号'):
                    borehole_id = borehole.text  # 获取钻孔编号 
                    result_row[i] = {"钻孔编号":borehole_id}
                    for layer in root.findall('.//吕荣值'): 
                        id_term = ".//ID"
                        id_tag = id_term + str(i)
                        for in_layer in layer.findall(id_tag):
                            start_depth = in_layer.find("起始深度").text #获取起始深度
                            result_row[i]["起始深度"] = start_depth #添加到字典
                            end_depth = float(in_layer.find('终止深度').text)  # 获取终止深度  
                            result_row[i]["终止深度"] = end_depth  # 添加到字典中
                            layer_name = in_layer.find('吕荣值').text  # 获取地层名称    
                            result_row[i]["吕荣值"] = layer_name
                            layer_depth = float(in_layer.find('层底深度').text)  # 获取底层深度  
                            result_row[i]["终止深度"] = layer_depth  # 添加到字典中     
    return result_row
       
def save_to_csv(result_dict, filename):  
    with open(filename, 'w', newline='') as csvfile:  
        writer = csv.writer(csvfile) 
    # 写入表头  
        writer.writerow(['Hole ID', 'From', 'To', 'Lithology'])  
    # 写入数据行  
        for key, value in result_dict.items():
            try:
                writer.writerow([value['钻孔编号'], value['起始深度'], value['终止深度'], value['吕荣值']])
            except KeyError:
                break

def saveall(dictdata, filename):
    dictall = {}
    dictall.append(dictdata)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)