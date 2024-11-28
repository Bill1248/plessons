from os import system
import datetime

def wait():
    input ("Hit enter to continue")

def clear():
    system( "clear")


def printData(weather):
    current_time = weather["dt"]
    if current_time == 0:
        current_time = "None"
    else:
        dt_object = datetime.datetime.fromtimestamp(current_time)
        current_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")

    print("*"*42)
    print(f"{'Place':19} : {weather["name"]}")
    print(f"{'Country':19} : {weather["country"]}")
    print(f"{'Measurement time':19} : {current_time}")
    print(f"{'Weather':19} : {weather["main"]}")
    print(f"{'Temperature':19} : {weather["temp"]}")
    print(f"{'Temperature, min':19} : {weather["temp_min"]}")
    print(f"{'Temperature, max':19} : {weather["temp_max"]}")
    print(f"{'Pressure':19} : {weather["pressure"]}")
    print(f"{'Wind':19} : {weather["wind"]}")
    print("*"*42)