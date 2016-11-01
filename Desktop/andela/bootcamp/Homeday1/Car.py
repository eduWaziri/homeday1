class Car(object):

    def __init__(self, name=None, model=None, type=None):
        # set name
        if name==None:
            self.name = 'General'
        else:
            self.name = name

        # set model
        if model==None:
            self.model = 'GM'
        else:
            self.model = model

        # set num_of_doors
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

         # set car type
        if type == 'trailer':
            self.saloon = False
            self.num_of_wheels = 8
        else:
            self.saloon = True
            self.num_of_wheels = 4

        # other default values
        self.speed = 0

        print self.name
        print self.model
        print self.num_of_doors

    def is_saloon(self):
        print self.saloon
        return self.saloon

    def drive(self, num):
        # trailers and saloons have different speeds
        if self.is_saloon():
            self.speed = pow(10,num)
        else:
            self.speed = num*11
        return self


name = 'honda'
model = 'Hyundai'

#honda = Car(name)
honda = Car(name=None, model=model)
honda.is_saloon()

p_name = 'Porsche'
p_model = '911 Turbo'

porsche = Car(name=p_name, model=p_model)
porsche.is_saloon()

t_name = 'MAN'
t_model = 'Truck'
t_type = 'trailer'


man = Car(name=t_name, model=t_model, type=t_type)
man.is_saloon()