def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    
    def is_safe(state, col):
        current_row = len(state)
        for r, c in enumerate(state):
            if c == col or abs(c - col) == abs(r - current_row):
                return False
        return True
    
    def backtrack(state):
        if len(state) == n:
            solutions.append(state)
            return
        
        for col in range(n):
            if is_safe(state, col):
                backtrack(state + [col])
                
    backtrack([])
    return solutions