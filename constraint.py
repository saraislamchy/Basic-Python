class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # List of nodes
        self.domains = domains  # Available colors for each region
        self.constraints = constraints  # Adjacency constraints (edges)
        self.assigned = {}  # Stores assigned colors

    def is_valid(self, variable, color):
        """Check if assigning 'color' to 'variable' violates any constraint."""
        for neighbor in self.constraints[variable]:
            if neighbor in self.assigned and self.assigned[neighbor] == color:
                return False  # if Neighbor has the same color
        return True

    def solve(self):
        """Backtracking algorithm to find a valid color assigned."""
        if len(self.assigned) == len(self.variables):
            return self.assigned  # All regions are assigned

        # Select the first unassigned region
        unassigned = [v for v in self.variables if v not in self.assigned]
        variable = unassigned[0]

        for color in self.domains[variable]:
            if self.is_valid(variable, color):
                self.assigned[variable] = color  # Assign color
                result = self.solve()
                if result:
                    return result  # Return valid solution
                del self.assigned[variable]  # Undo assignment (backtrack)
        return None  # No valid solution found

# Define rodes and their constraints (edges)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']
domains = {region: ['Red', 'Green', 'Blue'] for region in variables}
constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW']
}

# Solve the problem
csp = MapColoringCSP(variables, domains, constraints)
solution = csp.solve()
print("Valid Map Coloring Solution:")
for region, color in solution.items():
    print(f"{region}: {color}")
