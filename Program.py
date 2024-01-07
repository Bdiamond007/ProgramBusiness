# Define the business ideas
business_ideas = [
{
"idea": "Launch a new e-commerce platform",
"main_points": "Market research, platform development, marketing plan",
"priority": "High",
"potential_roi": "High",
"smart_goal": "Increase online sales by 30% within 6 months",
"timeline": "Q1: Market research, Q2: Platform development, Q3: Marketing plan, Q4: Launch"
},
{
"idea": "Expand into a new geographical market",
"main_points": "Research new market, establish distribution channels",
"priority": "Medium",
"potential_roi": "Medium",
"smart_goal": "Open two new stores in the new market by the end of the year",
"timeline": "Q1: Research new market, Q2: Establish distribution channels, Q3-Q4: Open new stores"
},
{
"idea": "Develop a new product line",
"main_points": "Product design, testing, production, marketing strategy",
"priority": "High",
"potential_roi": "High",
"smart_goal": "Launch two new products and achieve $500,000 in sales by the end of the year",
"timeline": "Q1-Q2: Product design and testing, Q3: Production, Q4: Marketing and launch"
}
]

# Generate the HTML table
html_output = """
<!DOCTYPE html>
<html>
<head>
<title>Business Ideas for 2024</title>
<style>
table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}
th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}
th {
background-color: #f2f2f2;
}
</style>
</head>
<body>
<h2>Business Ideas for 2024</h2>
<table>
<tr>
<th>Business Idea</th>
<th>Main Points</th>
<th>Priority</th>
<th>Potential ROI</th>
<th>SMART Goal</th>
<th>Timeline</th>
</tr>
"""

# Loop through each idea and add it to the table
for idea in business_ideas:
    html_output += f"""
    <tr>
    <td>{idea['idea']}</td>
    <td>{idea['main_points']}</td>
    <td>{idea['priority']}</td>
    <td>{idea['potential_roi']}</td>
    <td>{idea['smart_goal']}</td>
    <td>{idea['timeline']}</td>
    </tr>
"""

# Close the HTML tags
html_output += """
</table>
</body>
</html>
"""

# Write the HTML output to a file
with open('business_ideas.html', 'w') as file:
    file.write(html_output)