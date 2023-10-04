# Enter the years here
years = 50

# Constants
c0=450
initial_decline=0.15
softening_factor=0.965

def cumulative_storage_cost(t):
    '''Calculates the cumulative storage cost on Dash Platform for t years of storage'''
    total_cost = 0
    current_cost = c0
    current_decline = initial_decline
    
    for _ in range(t):
        total_cost += current_cost
        current_cost *= (1 - current_decline)
        current_decline *= softening_factor
        
    return total_cost

print(f"{cumulative_storage_cost(years):.0f} Credits")