"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    print(wagons)
    *wagons_list, = wagons
    return wagons_list

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagons1, wagons2, wagonsbegin, *other_wagons = each_wagons_id
    return [wagonsbegin] + missing_wagons + other_wagons + [wagons1, wagons2]

def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *route["stops"],  = stops.values()
    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [r_1, r_2, r_3],[b_1, b_2, b_3],[o_1,o_2,o_3] = wagons_rows
    return [[r_1,b_1,o_1],[r_2,b_2,o_2],[r_3,b_3,o_3]]
