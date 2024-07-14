import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Helper function to parse the formula
        def parse_formula(formula):
            # Stack to manage nested elements and their counts
            stack = [collections.defaultdict(int)]
            i, n = 0, len(formula)  # i is the current index, n is the length of the formula

            while i < n:
                if formula[i] == '(':  # If current character is '(', start a new scope
                    stack.append(collections.defaultdict(int))
                    i += 1
                elif formula[i] == ')':  # If current character is ')', end the current scope
                    i += 1
                    start = i
                    # Read the multiplier after ')'
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[start:i] or 1)  # Default multiplier is 1 if none provided
                    top = stack.pop()  # Pop the top dictionary from the stack
                    for elem, cnt in top.items():  # Multiply the counts and add to the previous scope
                        stack[-1][elem] += cnt * multiplier
                else:
                    start = i
                    i += 1
                    # Read the element name
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[start:i]  # Extract the element name
                    start = i
                    # Read the count of the element
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[start:i] or 1)  # Default count is 1 if none provided
                    stack[-1][elem] += count  # Add the count to the current scope
            
            return stack[0]  # Return the final counts from the stack

        # Parse the formula and get the element counts
        element_counts = parse_formula(formula)
        # Sort the elements alphabetically
        sorted_elements = sorted(element_counts.items())
        result = []

        # Construct the result string
        for elem, count in sorted_elements:
            result.append(elem)  # Add the element name
            if count > 1:
                result.append(str(count))  # Add the count if it is greater than 1

        return ''.join(result)  # Join the list into a single string and return