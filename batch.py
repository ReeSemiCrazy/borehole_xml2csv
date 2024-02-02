import os
import litho_convert as litho
import lu_convert as lu
import rqd_convert as rqd

def main(xml_folder, csv_folder):
    if not os.path.exists(csv_folder):
        os.mkdir(csv_folder)
    for file_name in os.listdir(xml_folder):
        xml_file = os.path.join(xml_folder, file_name)
        csv_file = os.path.join(csv_folder, file_name.split(".")[0] + ".csv")
        # change the prefix(library) of the functions to change the output content 
        # among: litho, lu, rqd
        dict_data = rqd.xml2dict(xml_file) 
        rqd.save_to_csv(dict_data, csv_file)
main("zk", "zk_csv_rqd")