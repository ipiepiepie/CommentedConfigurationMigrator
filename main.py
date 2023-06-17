import os
import yaml


# This recursive function iterates over all YAML nodes
# and writes its java equivalent to output file.
def parse_node(name, dictionary, path):
    child_nodes = dictionary[name]

    if isinstance(child_nodes, dict):  # Child nodes are another nodes
        for line in parent_node_template:
            output.write(
                line.format(name=generate_name(path), path='"{}"'.format(path), type=to_java_type(name)) + "\n")

        for node in child_nodes:
            next_path = path + "." + node
            parse_node(node, child_nodes, next_path)
    else:  # Child nodes is some value
        for line in node_template:
            output.write(
                line.format(name=generate_name(path), value=to_java_value(child_nodes), path='"{}"'.format(path),
                            type=to_java_type(child_nodes)) + "\n"
            )


# Convert Python type to Java type
def to_java_type(node):
    t = type(node)

    if t == list:
        return 'List'
    elif t == str:
        return 'String'
    elif t == bool:
        return 'Boolean'
    elif t == int:
        return 'Integer'
    elif t == float:
        return 'Float'


# Generate name for CommentedNode (just uppercase str and replaces '.' by '_')
def generate_name(path):
    return path.upper().replace(".", "_")


# Convert node to Java value
# e.g. surround String by "", convert list to List.of(...)
def to_java_value(node):
    t = type(node)

    if t == list:
        s = ', '.join(to_java_value(line) for line in node)
        return 'List.of({})'.format(s)
    if t == str:  # Convert to Java string
        return '"{}"'.format(node)
    if t == bool:  # Convert Python boolean to Java boolean
        return str(node).lower()
    else:
        return str(node)


# Main func
if __name__ == "__main__":
    # create output file
    output = open('output.java', 'w', encoding="utf-8")

    # read settings from config
    with open('conf.yml', 'r', encoding="utf-8") as file:
        config = yaml.safe_load(file)
        # initialise templates
        parent_node_template = config['parent_node']
        node_template = config['node']

    # wait for input
    file_path = input('Enter a file path: ')

    # check if input file exists
    if not os.path.exists(file_path):
        print('The specified file does NOT exist')
        exit(1)

    # open YAML input file
    with open(file_path, 'r', encoding="utf-8") as file:
        nodes = yaml.safe_load(file)

        # Iterate over first nodes in YML
        for n in nodes:
            parse_node(n, nodes, n)
        print("Exported YAML nodes to {}!".format(output.name))
