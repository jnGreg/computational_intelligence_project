import math
import random

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from src.functions.gen_dist_matrix import generate_dist_matrix
from src.functions.task_generator import generate_task

#





# [START data_model]
def create_data_model(Task):
    """Stores the data for the problem."""
    df = generate_dist_matrix(Task.points)
    listOfDFRows = df.to_numpy().tolist()
    cargo_weights = [int(x.cargo_amount) for x in Task.points]  # lista wag paczek
    vehicle_capacities = [int(el.capacity) for el in Task.trucks]  # lista ładunków
    num_vehicles = len(Task.trucks)  # liczba pojazdów
    cargo_weights[0] = 500

    data = {}

    # Here we got the data model, our pandas data frame
    data['distance_matrix'] = listOfDFRows

    # [START demands_capacities]
    data['demands'] = cargo_weights

    # Put the gallon carrying capacities of the trucks here
    data['vehicle_capacities'] = vehicle_capacities
    # [END demands_capacities]

    # How many trucks
    data['num_vehicles'] = num_vehicles
    data['depot'] = 0
    return data
    # [END data_model]


# [START solution_printer]
def print_solution(Task, data, manager, routing, solution):
    """Prints solution on console."""

    print(f'Diplay raod nfo ||||    Point number [cargo_weight] (actual truck load)       |||')
    print('')
    # Display dropped nodes.
    _12h_break_point = random.choice(range(1, len(Task.points)))

    dropped_nodes = 'Dropped nodes:'
    for node in range(routing.Size()):
        if routing.IsStart(node) or routing.IsEnd(node):
            continue
        if solution.Value(routing.NextVar(node)) == node:
            dropped_nodes += ' {}'.format(manager.IndexToNode(node))
    print(dropped_nodes)
    total_distance = 0
    total_load = 0
    total_time = 0
    for vehicle_id in range(data['num_vehicles']):
        truck = Task.trucks[vehicle_id]
        index = routing.Start(vehicle_id)
        plan_output = 'TRUCK {}  :\n'.format(vehicle_id)
        route_time = 0
        route_distance = 0
        route_load = 0
        breaks_time = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            if data['demands'][node_index] > 0:
                route_time += math.fabs(data['demands'][node_index]) * truck.load_speed
            else:
                route_time +=math.fabs(data['demands'][node_index]) * truck.unload_speed
            route_load += data['demands'][node_index]
            plan_output += ' {0} [{2}] ({1}) -> '.format(node_index, route_load, data['demands'][node_index])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
            route_time += routing.GetArcCostForVehicle(previous_index, index, vehicle_id) * truck.speed

            if int(node_index) == _12h_break_point:  # handling extra requirements
                route_time += 43200
                print(" This driver has Extra 12h break in point: ", _12h_break_point)

        breaks_time += round(route_time/10800) * 600  # 10 minutes of break after 3h of driving
        route_time += breaks_time


        plan_output += ' {0} [{2}] ({1})\n'.format(manager.IndexToNode(index),
                                                 route_load, data['demands'][node_index])
        plan_output += 'Distance of the route: {} km\n'.format(route_distance)
        plan_output += 'Load at the end of the route: {} kg\n'.format(route_load)
        plan_output += 'Time of the route: {0} s  or {1} h\n'.format(route_time, round(route_time/3600,2))
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
        total_time += route_time
    print('')
    print('Total distance of all routes: {} km'.format(total_distance))
    print('Total load of all routes: {} kg'.format(total_load))
    print('Total time of all routes: {0} s or {1} h'.format(total_time, round(total_time/3600,2)))
    # [END solution_printer]


def get_routes(solution, routing, manager):
    """Get vehicle routes from a solution and store them in an array."""
    # Get vehicle routes and store them in a two dimensional array whose
    # i,j entry is the jth location visited by vehicle i along its route.
    routes = []
    for route_nbr in range(routing.vehicles()):
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))
        routes.append(route)
    return routes


def cvrp(Task):
    """Solve the CVRP problem."""
    # Instantiate the data problem.


    # [START data]
    data = create_data_model(Task)
    num_vehicles = data["num_vehicles"]
    # [END data]

    # Create the routing index manager.
    # [START index_manager]
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])
    # [END index_manager]

    # Create Routing Model.
    # [START routing_model]
    routing_parameters = pywrapcp.DefaultRoutingModelParameters()
    #routing_parameters.solver_parameters.trace_propagation = True
    #routing_parameters.solver_parameters.trace_search = True
    routing = pywrapcp.RoutingModel(manager,routing_parameters)

    # [END routing_model]

    # Create and register a transit callback.
    # [START transit_callback]
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    # [END transit_callback]

    # Define cost of each arc.
    # [START arc_cost]
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # [END arc_cost]

    # Add Capacity constraint.
    # [START capacity_constraint]
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # [END capacity_constraint]
    num_nodes = len(Task.points)
    count_dimension_name = 'count'
    # assume some variable num_nodes holds the total number of nodes
    routing.AddConstantDimension(
        1,  # increment by one every time
        num_nodes // num_vehicles + 1,  # max value forces equivalent # of jobs
        True,  # set count to zero
        count_dimension_name)
    count_dimension = routing.GetDimensionOrDie(count_dimension_name)

    for veh in range(0, num_vehicles):
        index_end = routing.End(veh)
        count_dimension.SetCumulVarSoftLowerBound(index_end,
                                                  2,
                                                  50)

    # Allow to drop nodes.
    penalty = 1000
    for node in range(1, len(data['distance_matrix'])):
        routing.AddDisjunction([manager.NodeToIndex(node)], penalty)


    # Setting first solution heuristic.
    # [START parameters]
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.seconds = 10
    #search_parameters.log_search = True # loging result
    #search_parameters.time_limit.FromSeconds(15)
    #search_parameters.solution_limit = 30
    # [END parameters]

    # Solve the problem.
    # [START solve]
    solution = routing.SolveWithParameters(search_parameters)
    # [END solve]

    # Print solution on console.
    # [START print_solution]
    if solution:
        print_solution(Task, data, manager, routing, solution)
        routes = get_routes(solution, routing, manager)
        return routes
    # [END print_solution]
    else:
        print("Solver status: ", routing.status())
        print("""0	ROUTING_NOT_SOLVED: Problem not solved yet.
                1	ROUTING_SUCCESS: Problem solved successfully.
                2	ROUTING_FAIL: No solution found to the problem.
                3	ROUTING_FAIL_TIMEOUT: Time limit reached before finding a solution.
                4	ROUTING_INVALID: Model, model parameters, or flags are not valid.""")





#if __name__ == '__main__':
   # cvrp(T)
