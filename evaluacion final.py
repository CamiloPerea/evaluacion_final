
print("Owner:Camilo Perea")
print("Company: Viajes Express")
print("Safe Travels Around the World")
class Port_Tucbo:
    def __init__(self):
        self.offices = {}
        self.number_offices = 1

    def perform_dispatch(self, vehicle_plate, vehicle_description, driver_name, route, load_description):
        self.offices[self.number_offices] = {
            'vehicle_plate,': vehicle_plate,
            'vehicle_description': vehicle_description,
            'driver_name': driver_name,
            'route': route,
            'load_description': load_description
        }
        self.number_offices += 1

    def show_shipments(self):
        for number, offices in self.offices.items():
            print(f"Number of offices: {number}")
            print(f"vehicle_plate,: {offices['vehicle_plate,']}")
            print(f"vehicle_description: {offices['vehicle_description']}")
            print(f"Name of the driver: {offices['driver_name']}")
            print(f"route: {offices['route']}")
            print(f"load_description: {offices['load_description']}")
            print("↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯↯")

#Descripcion de los vehiculos
Port_Tucbo = Port_Tucbo()


Port_Tucbo .perform_dispatch("WOU123", "FORD EXPLORER", "Cristiano ronaldo", "USA-Argentina", "Cosmetic Load")
Port_Tucbo .perform_dispatch("WLX777", "RUBICON", "Cristiano ronaldo", "Asia-Colombia", "Ball Loading")
Port_Tucbo .perform_dispatch("CRF250", "CADILACC", "Camilo Pera", " Transilvania-Dubai", "Charging of technological devices ")

Port_Tucbo .show_shipments()
print("Thank you for using this company for orders")
print("☣️☣️☣️☣️☣️☣️☣️☣️IMPORTANT☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️")
print("⮕If your order has not arrived, please inform us to verify, and we will refund 70% of the value of your order.⬅")

   