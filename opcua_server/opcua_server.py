from opcua import Server

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

# Setup namespace
uri = "http://example.org"
idx = server.register_namespace(uri)
server.start()
print("OPC UA server started at opc.tcp://0.0.0.0:4840/freeopcua/server/")

# Create a new node folder in the server namespace
node = server.nodes.objects.add_object(idx, "MyObject")

# Add 30 integer variables
for i in range(0, 30):
    var_name = f"Address_{i}"
    var_node = node.add_variable(idx, var_name, 0)
    var_node.set_writable()  # Set variables to be writable by clients

