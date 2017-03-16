import os, json, sys

input_file = sys.argv[1]
output_file = sys.argv[2]

import_file = open(input_file)
users_data = json.load(import_file)
log_file = open(output_file, 'a')


count = 0
for item in users_data['matrix']:
    if count < item['number']:
        count = item['number']
    
for item in users_data['matrix']:
    if count == item['number'] and item['result'] !=0:
        log_file.write('%s' % "id: " + str(item['id']) + ", " + "number: " + str(item['number']) + ", " +  "committer_name: " + users_data['committer_name'] + ", " + "committer_email: " + users_data['committer_email'] + "\n") 


import_file.close()
log_file.close()
