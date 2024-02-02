import litho_convert as litho
import lu_convert as lu
import rqd_convert as rqd

##一个用于测试的终端界面
def main():
    while True:
        print("This is the test!\n"
            "1. Output Lithology\n"
            "2. Output Water Pressure Test Value in LU\n"
            "3. Output RQD value\n"
            "q: Quit！")
        user_input = input("Your choice:\n")
        if user_input == "q":
                break
        else:
            try:
                match int(user_input):
                    case 1:
                        test1 = litho.xml2dict("sample.xml")
                        print(test1)
                        litho.save_to_csv(test1, "lithotest.csv")
                        print("Lithology Converted")
                    case 2:
                        test2 = lu.xml2dict("sample.xml")
                        print(test2)
                        lu.save_to_csv(test2, "lutest.csv")
                        print("Lu Converted")
                    case 3:
                        test3 = rqd.xml2dict("sample.xml")
                        print(test3)
                        rqd.save_to_csv(test3, "rqdtest.csv")
                        print("RQD Converted")
                    case _:
                        print("I have a bad feeling about this...")     
            except ValueError:
                print("I have a bad feeling about this...")
main()