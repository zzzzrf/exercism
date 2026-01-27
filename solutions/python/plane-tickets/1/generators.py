"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    index = 0
    seats = ['A', 'B', 'C', 'D']
    while index < number:
        yield seats[index % 4]
        index += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    index = 0
    seats = ['A', 'B', 'C', 'D']
    while index < number:
        row_n = int(index / 4) + 1
        if row_n >= 13:
            row_n += 1
        yield str(row_n) + seats[index % 4]
        index += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    index = 0
    seats = ['A', 'B', 'C', 'D']
    return_seats = {}
    for passenger in passengers:
        row_n = int(index / 4) + 1
        if row_n >= 13:
            row_n += 1
        return_seats[passenger] = str(row_n) + seats[index % 4]
        # yield {passenger : str(row_n) + seats[index % 4]}
        index += 1
    return return_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for item in seat_numbers:
        append = 12 - len(item) - len(flight_id)
        yield item + flight_id + '0' * append
