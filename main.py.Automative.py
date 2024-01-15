class Car:
    def __(self, wheels=4):
        self.wheels = wheels


class Gasoline(Car):
    def __init__(self, Model_Name='Tata Puch bs6 2020', Engine_type='Tata bs6 Gasoline Engine', Gas_tank_cap = '30Kg',
                 color_of_Car="red", Average='4.7km/ltr', Seating_capasity=2, Horse_power=' 100hp',
                 Transmission='6 Speed Manual',
                 Standard_Feature='-7- inch infotaninment touchscreen\n                   -Blutooth connectivity\n                   -LED headlights\n                   -Sport tuned suspention\n                   -Convertible soft toop',
                 PRICE ='from 10,50,000 INR**'):
        # Car.__init__(self)
        self.Model_Name = Model_Name
        self.Engine_type = Engine_type
        self.Gas_tank_cap = Gas_tank_cap
        self.color_of_Car = color_of_Car
        self.Average = Average
        self.Seating_capacity = Seating_capasity
        self.Horse_power = Horse_power
        self.Horse_power = Horse_power
        self.Transmission = Transmission
        self.Standard_Feature = Standard_Feature
        self.PRICE = PRICE


class Electric(Car):
    def __init__(self,Model_Name = 'Tata Bs5 2020', Engine_type = 'Tata bs5 Electric Engine', Battery_cap = '100km',
                 color_of_Car = 'Green', Seating_capasity = 4, Horse_power = ' 120hp',
                 Transmission = '10 Speed Manual',
                 Standard_Feature = '-7- inch infotaninment touchscreen\n                   -Blutooth connectivity\n                   -LED headlights\n                   -Sport tuned suspention\n                   -Convertible soft toop',
                 PRICE = 'from 15,50,000 INR**'):
        # Car.__init__(self)
        self.Model_Name = Model_Name
        self.Engine_type = Engine_type
        self.Battery_cap = Battery_cap
        self.color_of_Car = color_of_Car
        self.Seating_capacity = Seating_capasity
        self.Horse_power = Horse_power
        self.Transmission = Transmission
        self.Standard_Feature = Standard_Feature
        self.PRICE = PRICE

class Hybrid(Gasoline, Electric):
    def __init__(self, Model_Name = 'PQR Motors Hybrid 2021', Engine_Type = ' 1.5 Engine + Gasoline Engine + Electric Engine',
                 Battery_cap = '100km',
                 color_of_Car = 'Yellow', Seating_capasity = 4, Horse_power = ' 120hp',
                 Transmission = '10 Speed Manual',
                 Standard_Feature = '-7- inch infotaninment touchscreen\n                   -Blutooth connectivity\n                   -LED headlights\n                   -Sport tuned suspention\n                   -Convertible soft toop',
                 PRICE = 'from 19,50,000 INR**'):

        self.Model_Name = Model_Name
        self.Engine_Type = Engine_Type
        self.Battery_cap = Battery_cap
        self.color_of_Car = color_of_Car
        self.Seating_capacity = Seating_capasity
        self.Horse_power = Horse_power
        self.Transmission = Transmission
        self.Standard_Feature = Standard_Feature
        self.PRICE = PRICE


user = 0
while True:
    user = input("what is your preferred transmission type MANUAL or AUTOMATIC : ")
    user == user.upper()
    if user == "MANUAL" or user == "AUTOMATIC":
        if user == "MANUAL":
            G = Gasoline()
            print("this Manual car Available In 1 Color Variant: Red : ")
            while True:
                color = input("Please select One color available variant RED: ")
                color == color.upper()
                if color == "RED": #or color == "GREEN":
                    print("****************************************************************")
                    print(f'Model_Name : {G.Model_Name}\nEngine_type : {G.Engine_type}\nGas_tank_cap : {G.Gas_tank_cap}\ncolor_of_Car : {G.color_of_Car}\nAverage : {G.Average}')
                    print(f'Seating_capacity : {G.Seating_capacity}\nHorse_power : {G.Horse_power}\nTransmission:{G.Transmission}')
                    print(f'Standard_Feature : {G.Standard_Feature}')
                    print(f'PRICE : {G.PRICE}')
                    print("****************************************************************")
                    break
                else:
                    print("!!sorry!! Color Is Not Available Yet")
            break


        elif user == "AUTOMATIC":
            print("Automatic Car Available In Three Engine Type : GASOLINE, ELECTRIC, HYBRID... ")

            while True:
                engine = input("Please select Engine As per your conveyance : GASOLINE, ELECTRIC, HYBRID :-  ")
                engine == engine.upper()
                if engine == "GASOLINE":
                    G = Gasoline()
                    print("this automatic car available is 1 color: Red :  ")
                    while True:
                        color = input("please select one color from available variant: RED : ")
                        color == color.upper()
                        if color == "RED": #or color == "GREEN" or color == "YELLOW":
                            print("************************************************************")
                            print(f'Model_Name : {G.Model_Name}\nEngine_type : {G.Engine_type}\nGas_tank_cap : {G.Gas_tank_cap}\ncolor_of_Car : {G.color_of_Car}\nAverage : {G.Average}')
                            print(f'Seating_capacity : {G.Seating_capacity}\nHorse_power : {G.Horse_power}\nTransmission:{G.Transmission}')
                            print(f'Standard_Feature : {G.Standard_Feature}')
                            print(f'PRICE : {G.PRICE}')
                            print("****************************************************************")
                            break
                        else:
                            print("!!Sorry!! Color is nor available")
                    break


                elif engine == "ELECTRIC":
                    E = Electric()
                    print("this Automatic Electric car available in 1 color variant: Green : ")
                    while True:
                        color = input("Please select the one color from available variant GREEN : ")
                        color == color.upper()
                        if color == "GREEN":
                            print("**************************************************************")
                            print(f'Model_Name: {E.Model_Name}\nEngine_Type: {E.Engine_type}\nBattery_cap: {E.Battery_cap}')
                            print(f'color_of_Car: {E.color_of_Car}\nSeating_capacity: {E.Seating_capacity}\nHorse_power: {E.Horse_power}')
                            print(f'Transmission: {E.Transmission}\nStandard_Feature: {E.Standard_Feature}')
                            print(f'PRICE: {E.PRICE}')
                            break
                        else:
                            print("!!Sorry!! Color is not available...")
                    break


                elif engine == "HYBRID":
                    H = Hybrid()
                    print("this Automatic Electric car available in 1 color variant: Yellow : ")
                    while True:
                        color = input("Please select the one color from available variant YELLOW : ")
                        color == color.upper()
                        if color == "YELLOW":
                            print("**************************************************************")
                            print(f'model_name : {H.Model_Name}\nEngine_Type: {H.Engine_Type}\nBattery_cap: {H.Battery_cap}')
                            print(f'color_of_Car : {H.color_of_Car}\nSeating_capacity: {H.Seating_capacity}\nHorse_power: {H.Horse_power}')
                            print(f'Transmission: {H.Transmission}\nStandard_Feature: {H.Standard_Feature}\nPRICE:  {H.PRICE}')
                            break
                        else:
                            print("!!Sorry!! Color is not available...")
                    break
                else:
                    print("please enter valid details of engine!!")
            break
    else:
        print("please enter valid details of car transmission")
