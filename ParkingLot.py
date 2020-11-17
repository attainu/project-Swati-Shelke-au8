"""
Project by Swati

"""

import Vehicle
import argparse
import sys

if sys.version_info[0] == 2:
    input = input()


# Parking Lot class


class ParkingLot:
    def __init__(self):
        self.capacity = 0
        self.slotid = 0
        self.numOfOccupiedSlots = 0

    # createParkingLot method
    def createParkingLot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    # getEmptySlot method
    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    # park method
    def park(self, regno, color):
        if self.numOfOccupiedSlots < self.capacity:
            slotid = self.getEmptySlot()
            self.slots[slotid] = Vehicle.Car(regno, color)
            self.slotid = self.slotid+1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
            return slotid+1
        else:
            return -1

    # leave method
    def leave(self, slotid):

        if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
            self.slots[slotid-1] = -1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
            return True
        else:
            return False

    # status method
    def status(self):
        print("Slot No.\tRegistration No.\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i + 1) +
                      "\t\t" + str(self.slots[i].regno) +
                      "\t\t" + str(self.slots[i].color))
            else:
                continue

    # getRegNoFromColor method
    def getRegNoFromColor(self, color):

        regnos = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                regnos.append(i.regno)
        return regnos

    # getSlotNoFromRegNo method
    def getSlotNoFromRegNo(self, regno):

        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                return i+1
            else:
                continue
        return -1

    # getSlotNoFromColor method
    def getSlotNoFromColor(self, color):

        slotnos = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i+1))
        return slotnos

    # show method
    def show(self, line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingLot(n)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('park'):
            regno = line.split(' ')[1]
            color = line.split(' ')[2]
            res = self.park(regno, color)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Allocated slot number: '+str(res))

        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                print('Slot number '+str(leave_slotid)+' is free')

        elif line.startswith('status'):
            self.status()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            regnos = self.getRegNoFromColor(color)
            print(', '.join(regnos))

        elif line.startswith('slot_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getSlotNoFromColor(color)
            print(', '.join(slotnos))

        elif line.startswith('slot_number_for_registration_number'):
            regno = line.split(' ')[1]
            slotno = self.getSlotNoFromRegNo(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)


# file input method


def main():

    parkinglot = ParkingLot()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--testcase')
    args = parser.parse_args()
    if args.testcase:
        with open(args.testcase, 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)

    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)


if __name__ == '__main__':
    main()
