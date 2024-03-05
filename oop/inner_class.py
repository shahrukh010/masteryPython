class Customer:

    def __init__(self,id,first_name,last_name,a_id,address,landmark,pincode):
        self.id = id;
        self.name = first_name;
        self.last_name = last_name;
        self.address = self.Address(a_id,address,landmark,pincode);



    class Address:

        def __init__(self,id,address,landmark,pincode):
            self.id = id;
            self.address = address;
            self.landmark = landmark;
            self.pincode = pincode;

        def display(self):
            print('-----------Address-------------');
            print(f"A_id: {self.id}");
            print(f"Address :{self.address}");
            print(f"Landmark: {self.landmark}");
            print(f"Pincode: {self.pincode}");


customer = Customer(101,"hector","smith",222,"407 Hitex Hyderabad","Hitex Camman",500084);

customer.address.display();
        



