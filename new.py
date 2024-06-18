from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define variables
name = 'John Doe'
age = 25

# Load the template file
template = env.get_template('template.html')

# Render the template with variables
rendered_html = template.render(name=name, age=age)

# Print or save the rendered HTML
print(rendered_html)


output_file_path = './.html'
with open(output_file_path,'w') as output_file:
    output_file.write(rendered_html)


print(f'Rendered HTML saved to {output_file_path}')