# importing required packages
# import package to handle json files
import json
# import package help with OS processes inquires
import subprocess

# open the .json file as an input
with open('sample.json', 'r') as input:
    # creating a variable obj to store the data
    obj = json.load(input)
    # printing firstName from .json file
    print('Hello, ' + obj['firstName'])
    # output data to a file sampleOutput.txt
    with open('sampleOutput.txt', 'w') as output:
        output.write(obj['firstName'] + "'s hobbies:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")


# using the subprocess package to run ipconfig command and store it in a
# pipe and use that pipe to communicate with the results
pl = subprocess.Popen(['taskList'], stdout=subprocess.PIPE).communicate()[0]
decoded = pl.decode('utf-8')
with open('taskList.txt', 'w') as output:
    output.write(decoded)
