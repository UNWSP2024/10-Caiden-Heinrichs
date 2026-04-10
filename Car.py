#Week 10, Program 2 - Car Class
#Caiden Heinrichs
#04/10/26


class Car:
    #Initiate attributes
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        #Test if the car is stopped or stop the car is result would be negative
        if self.__speed - 5 >= 0:
            self.__speed -= 5
        elif self.__speed == 0:
            print('The car is already stopped')
        else:
            self.__speed = 0

        return self.__speed

    def get_speed(self):
        return self.__speed


def main():
    #Create the car object (I named this car Edina)
    edina = Car('1968 Beetle', 'Volkswagen')

    #Accelerate the car and display the new speed
    for i in range(5):
        print(f'The speed of Edina is {edina.accelerate()}mph.')
    
    #Brake the car and display the new speed
    for i in range(5):
        print(f'The speed of Edina is {edina.brake()}mph.')


if __name__ == '__main__':
    main()
