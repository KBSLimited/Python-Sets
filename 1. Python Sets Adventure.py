def compare_flight_routes(our_routes, competitor_routes):
    # Find destinations that both airlines fly to
    common_destinations = our_routes.intersection(competitor_routes)
    
    # Find destinations unique to your airline
    unique_our_destinations = our_routes.difference(competitor_routes)
    
    # Find destinations that neither airline shares
    unique_competitor_destinations = competitor_routes.difference(our_routes)
    
    # Display results
    print(f"Destinations that both airlines fly to: {common_destinations}")
    print(f"Destinations unique to our airline: {unique_our_destinations}")
    print(f"Destinations unique to competitor's airline: {unique_competitor_destinations}")

# Example routes
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Compare routes
compare_flight_routes(our_routes, competitor_routes)