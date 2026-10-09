   # Hash map = Python dictionary. Stores key -> value.
   # A hash function turns the key into a spot, so lookups are O(1).
bookings = ['king', 'suite', 'double', 'king', 'king', 'double', 'suite', 'king']
def count_bookings(bookings):
    times = {}
    for book in bookings:
        if book in times:
            times[book] +=1
        else:
            times[book] = 1
    return times
print(count_bookings(bookings))   # {'king': 4, 'suite': 2, 'double': 2}