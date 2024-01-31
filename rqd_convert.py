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
                # 获取钻孔编号
                for borehole in param.findall('.//钻孔编号'):
                    borehole_id = borehole.text   
                    result_row[i] = {"钻孔编号":borehole_id}
                    for layer in root.findall('.//采取率RQD'): 
                        id_term = ".//ID"
                        id_tag = id_term + str(i)
                        for in_layer in layer.findall(id_tag):
                            #获取钻孔进尺、计算起止深度
                            bh_length = in_layer.find("钻孔进尺").text 
                            if i == 1:
                                start_depth = 0
                                end_depth = bh_length
                            else:
                                start_depth = float(end_depth) + float(bh_length)
                                end_depth = float(end_depth) + float(bh_length) 
                            result_row[i]["起始深度"] = start_depth 
                            result_row[i]["终止深度"] = end_depth  
                            #获取岩样长度、>10cm岩心长度
                            core_length = in_layer.find("岩样长度").text 
                            rqd_length = in_layer.find("RQD长度").text
                            result_row[i]["钻孔进尺"] = bh_length  
                            result_row[i]["岩样长度"] = core_length 
                            result_row[i]["RQD长度"] = rqd_length
                            #计算采取率、RQD
                            if bh_length != 0:
                                fetch_rate = float(core_length) / float(bh_length)
                                rqd_rate = float(rqd_length) / float(bh_length)
                            else:
                                fetch_rate = 0
                                rqd_rate = 0
                            result_row[i]["采取率"] = round(fetch_rate, 2)
                            result_row[i]["RQD"] = round(rqd_rate, 2)    
    return result_row
       
def save_to_csv(result_dict, filename):  
    with open(filename, 'w', newline='') as csvfile:  
        writer = csv.writer(csvfile) 
    # 写入表头  
        writer.writerow(['Hole ID', 'From', 'To', 'BH Length', 'Core Length', 
                         'RQD Length', 'Rate', 'RQD'])  
    # 写入数据行  
        for key, value in result_dict.items():
            try:
                writer.writerow([value['钻孔编号'], value['起始深度'], value['终止深度'], 
                                 value['钻孔进尺'], value['岩样长度'], value['RQD长度'], 
                                 value['采取率'], value['RQD']])
            except KeyError:
                break

def saveall(dictdata, filename):
    dictall = {}
    dictall.append(dictdata)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)