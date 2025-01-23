import math

# Define fixed values
a = 2
b = 5
c = 4

# Perform calculations
# Step 1: Compute c^3
# The power-law calculations are done with **.
c_cubed = c ** 3
# Step 2: Calculate square root of c^3
sqrt_c_cubed = c_cubed ** 0.5
# Step 3: Divide square root by a
division_result = sqrt_c_cubed / a
# Step 4: Multiply by 10
multiplication_result = division_result * 10
# Step 5: Add b to get final result
final_result = b + multiplication_result

# Generate HTML output
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Calculation Results</title>
    <style>
        body {{
            font-family: sans-serif;
            margin: 20px;
        }}
        .step {{
            margin: 10px 0;
        }}
        .result {{
            color: #2c3e50;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Calculation Steps and Results</h1>
    <div class="step">Initial values: a = {a}, b = {b}, c = {c}</div>
    <div class="step">1. c³ = {c_cubed}</div>
    <div class="step">2. √(c³) = {sqrt_c_cubed}</div>
    <div class="step">3. √(c³)/a = {division_result}</div>
    <div class="step">4. (√(c³)/a) × 10 = {multiplication_result}</div>
    <div class="result">5. Final Result = {final_result}</div>
</body>
</html>
"""

# Print the HTML output
print(html_output)