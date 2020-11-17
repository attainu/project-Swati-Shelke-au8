import unittest
from ParkingLot import ParkingLot


# TestParkingLot class


class TestParkingLot(unittest.TestCase):

    # testcase method for create parking lot
    def test_create_parking_lot(self):
        parkingLot = ParkingLot()
        res = parkingLot.createParkingLot(6)
        self.assertEqual(6, res)

    # testcase method for park
    def test_park(self):
        parkingLot = ParkingLot()
        res = parkingLot.createParkingLot(6)
        res = parkingLot.park("KA-01-HH-1234", "White")
        self.assertNotEqual(-1, res)

    # testcase method for leave
    def test_leave(self):
        parkingLot = ParkingLot()
        res = parkingLot.createParkingLot(6)
        res = parkingLot.park("KA-01-HH-1234", "White")
        res = parkingLot.leave(1)
        self.assertEqual(True, res)

    # testcase method for getRegNoFromColor
    def test_getRegNoFromColor(self):
        parkingLot = ParkingLot()
        res = parkingLot.createParkingLot(6)
        res = parkingLot.park("KA-01-HH-1234", "White")
        res = parkingLot.park("KA-01-HH-9999", "White")
        regnos = parkingLot.getRegNoFromColor("White")
        self.assertIn("KA-01-HH-1234", regnos, res)
        self.assertIn("KA-01-HH-9999", regnos)

    # testcase method for getSlotNoFromRegNo
    def test_getSlotNoFromRegNo(self):
        parkingLot = ParkingLot()
        res = parkingLot.createParkingLot(6)
        res = parkingLot.park("KA-01-HH-1234", "White")
        res = parkingLot.park("KA-01-HH-9999", "White")
        slotno = parkingLot.getSlotNoFromRegNo("KA-01-HH-9999")
        self.assertEqual(2, slotno, res)

    # testcase method for getSlotNoFromColor
    def test_getSlotNoFromColor(self):
        parkingLot = ParkingLot()
        res = parkingLot.createParkingLot(6)
        res = parkingLot.park("KA-01-HH-1234", "White")
        res = parkingLot.park("KA-01-HH-9999", "White")
        slotnos = parkingLot.getSlotNoFromColor("White")
        self.assertIn("1", slotnos, res)
        self.assertIn("2", slotnos)


if __name__ == '__main__':
    unittest.main()
