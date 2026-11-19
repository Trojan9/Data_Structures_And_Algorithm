# Design a Parking Lot (with hourly pricing and a daily cap)
#
# =====================================================================================
# QUESTION
# =====================================================================================
# Design a parking lot with a fixed number of spaces.
#
#   park(plate, t)   -> a car arrives at time t. Give it a free space and a ticket.
#                       If the lot is full, return -1.
#   leave(ticket, t) -> the car leaves at time t. Free its space and return the fee.
#   available()      -> how many spaces are free right now.
#
# Pricing:
#   - $5 for the first hour
#   - $3 for every extra hour
#   - at most $30 can be paid for any 24 hours
#
# Time t is given in MINUTES (like the `t` in design-underground-system).
#
# Assumptions (say them out loud in an interview, then ask if they're OK):
#   1. A started hour is a full hour: 61 minutes = 2 hours. Even 1 minute = 1 hour = $5.
#   2. Each full 24 hours costs the cap, $30.
#   3. Hours left over after the full days are billed like a new day:
#      $5 for the first one, $3 for each extra, capped at $30.
#   4. A space fits any car (no small/large spaces). Follow-ups at the bottom.
#
# =====================================================================================
# THE PRICE TABLE (one day)
# =====================================================================================
#
#   price(h) = 5 + 3 * (h - 1), but never more than 30
#
#   hours   1   2   3   4   5   6   7   8   9   10   11 ... 24
#   price   5   8   11  14  17  20  23  26  29  30   30 ... 30
#                                               ^
#                                   5 + 3 * 9 = 32 > 30 -> capped
#
#   So from the 10th hour onwards the rest of that day is free; the car has hit the cap.
#
#   Longer stays:  hours = days * 24 + rest
#                  fee   = days * 30 + price(rest)       (price(0) = 0)
#
#     24 h   -> 1 day + 0 h  -> 30 + 0  = 30
#     25 h   -> 1 day + 1 h  -> 30 + 5  = 35
#     27 h   -> 1 day + 3 h  -> 30 + 11 = 41
#     58 h   -> 2 days + 10 h -> 60 + 30 = 90
#
# =====================================================================================
# KEY IDEA: split the job into small classes
# =====================================================================================
#
#   FeeCalculator  -> ONLY knows the prices (minutes in, dollars out).
#                     If prices change, only this class changes.
#   Ticket         -> who parked, in which space, and when they arrived.
#   ParkingLot     -> hands out spaces and tickets, takes them back, asks the
#                     FeeCalculator for the price.
#
#   Data structures in ParkingLot:
#     free_spaces : min-heap of free space numbers -> always give the LOWEST free
#                   number (closest to the entrance) in O(log n)
#     tickets     : ticket_id -> Ticket            -> O(1) lookup when the car leaves
#     parked      : plate -> ticket_id             -> stop the same car parking twice
# =====================================================================================

import heapq
import math


class FeeCalculator:
    FIRST_HOUR = 5        # $ for the first hour
    EXTRA_HOUR = 3        # $ for every hour after the first
    DAILY_CAP = 30        # $ max per 24 hours
    HOURS_PER_DAY = 24

    def price_for_hours(self, hours: int) -> int:
        """Price for 0..24 hours inside ONE day."""
        if hours <= 0:
            return 0
        return min(self.DAILY_CAP, self.FIRST_HOUR + self.EXTRA_HOUR * (hours - 1))

    def fee(self, minutes: int) -> int:
        hours = max(1, math.ceil(minutes / 60))           # a started hour counts; at least 1 hour
        days, rest = divmod(hours, self.HOURS_PER_DAY)    # full days + leftover hours
        return days * self.DAILY_CAP + self.price_for_hours(rest)


class Ticket:
    def __init__(self, ticket_id: int, plate: str, space: int, entry_time: int):
        self.ticket_id = ticket_id
        self.plate = plate
        self.space = space
        self.entry_time = entry_time


class ParkingLot:
    def __init__(self, capacity: int, calculator: FeeCalculator = None):
        self.free_spaces = list(range(1, capacity + 1))   # spaces 1..capacity, all free
        heapq.heapify(self.free_spaces)                    # already sorted, so already a heap
        self.tickets = {}                                  # ticket_id -> Ticket
        self.parked = {}                                   # plate -> ticket_id
        self.next_ticket_id = 1
        self.calculator = calculator or FeeCalculator()

    def park(self, plate: str, t: int) -> int:
        if plate in self.parked:            # this car is already inside
            return -1
        if not self.free_spaces:            # lot is full
            return -1
        space = heapq.heappop(self.free_spaces)            # lowest free space number
        ticket = Ticket(self.next_ticket_id, plate, space, t)
        self.tickets[ticket.ticket_id] = ticket
        self.parked[plate] = ticket.ticket_id
        self.next_ticket_id += 1
        return ticket.ticket_id

    def leave(self, ticket_id: int, t: int) -> int:
        ticket = self.tickets.pop(ticket_id, None)
        if ticket is None:                  # unknown or already-used ticket
            return -1
        del self.parked[ticket.plate]
        heapq.heappush(self.free_spaces, ticket.space)     # space is free again
        return self.calculator.fee(t - ticket.entry_time)

    def available(self) -> int:
        return len(self.free_spaces)


# =====================================================================================
# DRY RUN 1: the fee function
# =====================================================================================
#
#   minutes   hours = ceil(min/60)   days, rest = divmod(hours, 24)   fee
#   -------   --------------------   ------------------------------   ---------------------
#   1         1                      0, 1                             price(1) = 5
#   60        1                      0, 1                             5
#   61        2                      0, 2                             5 + 3 = 8
#   150       3   (2.5 -> 3)         0, 3                             5 + 3*2 = 11
#   540       9                      0, 9                             5 + 3*8 = 29
#   600       10                     0, 10                            5 + 3*9 = 32 -> cap 30
#   1440      24                     1, 0                             30 + 0 = 30
#   1500      25                     1, 1                             30 + 5 = 35
#   3480      58                     2, 10                            60 + 30 = 90
#
# =====================================================================================
# DRY RUN 2: the lot, capacity 2
# =====================================================================================
#
#   call                      free_spaces   tickets                 returns
#   ------------------------  ------------  ----------------------  -------------------------
#   ParkingLot(2)             [1, 2]        {}
#   park("A1", t=0)           [2]           {1: A1 in space 1}      ticket 1
#   park("B2", t=30)          []            {1: A1, 2: B2 in 2}     ticket 2
#   park("C3", t=45)          []            same                    -1 (full)
#   leave(1, t=150)           [1]           {2: B2}                 150 min = 3 h -> $11
#   park("C3", t=160)         []            {2: B2, 3: C3 in 1}     ticket 3 (gets space 1,
#                                                                    the lowest free one)
#   leave(2, t=30 + 1500)     [2]           {3: C3}                 1500 min = 25 h -> $35
#   leave(2, t=2000)          [2]           {3: C3}                 -1 (ticket already used)
#   available()                                                     1
#
# =====================================================================================
# Complexity (n = number of spaces)
# =====================================================================================
#   park       O(log n)  heappop of the lowest free space; dict inserts are O(1)
#   leave      O(log n)  heappush of the freed space; dict lookups/deletes are O(1)
#   available  O(1)
#   fee        O(1)      just arithmetic, however long the stay
#   Space      O(n)      the heap holds up to n spaces, the dicts up to n parked cars
#
#   (If you don't care which space a car gets, a plain list/stack of free spaces makes
#    park and leave O(1).)
#
# =====================================================================================
# Follow-ups they may ask
# =====================================================================================
#   - Different vehicle sizes (motorbike / car / van): one free-space heap per size;
#     a smaller vehicle may take a bigger space if its own size is full.
#   - Several floors: store (floor, space) in the heap so the lowest floor fills first.
#   - Grace period (e.g. first 10 minutes free): in fee(), return 0 if minutes <= 10.
#   - Different prices on weekends / at night: give ParkingLot a different
#     FeeCalculator. That's why prices live in their own class (strategy pattern).
#   - Lost ticket: look the car up by plate with `parked[plate]`, charge a fixed fee.
#   - Two entrances at the same time: protect park/leave with a lock so two cars
#     can't be given the same space.


if __name__ == "__main__":
    f = FeeCalculator()
    expected = {1: 5, 60: 5, 61: 8, 150: 11, 540: 29, 600: 30, 1440: 30,
                1500: 35, 1620: 41, 3480: 90}
    for minutes, want in expected.items():
        assert f.fee(minutes) == want, (minutes, f.fee(minutes), want)

    lot = ParkingLot(2)
    assert lot.park("A1", 0) == 1
    assert lot.park("B2", 30) == 2
    assert lot.park("C3", 45) == -1          # full
    assert lot.park("A1", 50) == -1          # already inside
    assert lot.leave(1, 150) == 11
    assert lot.park("C3", 160) == 3
    assert lot.tickets[3].space == 1         # lowest free space reused
    assert lot.leave(2, 30 + 1500) == 35
    assert lot.leave(2, 2000) == -1          # ticket already used
    assert lot.available() == 1
    print("all good")
