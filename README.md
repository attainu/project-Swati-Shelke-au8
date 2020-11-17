Design a parking lot using Python OOP methods

1. We create n number of slots
2. Allocate each parking lot to a selected car using the respective function
3. If any slot needed to be emptied function leave i used
4. The number of cars with respective colors can be known
5. The registration numbers of cars of a particular colour can be known

Test case:-

1. create_parking_lot 6
2. park KA-01-HH-1234 White
3. park KA-01-HH-9999 White
4. park KA-01-BB-0001 Black
5. park KA-01-HH-7777 Red
6. park KA-01-HH-2701 Blue
7. park KA-01-HH-3141 Black
8. leave 4
9. status
10. park KA-01-P-333 White
11. park DL-12-AA-9999 White
12. registration_numbers_for_cars_with_colour White
13. slot_numbers_for_cars_with_colour White
14. slot_number_for_registration_number KA-01-HH-3141
15. slot_number_for_registration_number MH-04-AY-1111

Test case OutPut:-

1. Created a parking lot with 6 slots
2. Allocated slot number: 1
3. Allocated slot number: 2
4. Allocated slot number: 3
5. Allocated slot number: 4
6. Allocated slot number: 5
7. Allocated slot number: 6
8. Slot number 4 is free
9. Slot No. Registration No Colour  
   1 KA-01-HH-1234 White  
   2 KA-01-HH-9999 White  
   3 KA-01-BB-0001 Black  
   5 KA-01-HH-2701 Blue  
   6 KA-01-HH-3141 Black
10. Allocated slot number: 4
11. Sorry, parking lot is full
12. KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
13. 1, 2, 4
14. 6
15. Not found
