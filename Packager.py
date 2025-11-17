



def Package_Network(network, network_name):
    string = ""
    try:
        file = open(network_name, "w")
    except:
        open(network_name, "x")
        file = open(network_name, "w")
    
    for weight in network.weights:
        string += f"{weight}\n"
    string += "\n\n"
    for bias in network.biases:
        string += f"{bias}\n"
    file.write(string)
    file.close()

def Unpackage_Network(target_network, network_name):
    file = open(network_name, "r")
    string = file.read()
    string.split("\n\n")
    weights = string[0].split("\n")
    biases = string[1].split("\n")
    for index, weight in enumerate(weights):
        target_network.weights[index] = eval(weight)
    for index, bias in enumerate(biases):
        target_network.biases[index] = eval(bias)
    file.close()