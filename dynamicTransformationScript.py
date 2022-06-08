import csv
from curses import raw
import uuid

# Two Inputs Files 
##################################################
raw_data_file = './dev/my-data-org-source-data.csv'
mapping_file = './dev/mapping-mydata_org-mdo.csv'
##################################################

# Output file
##################################################
conforming_triples_output = './output/my-data-instances.ttl'
##################################################



def createTriples(mapping, data_value):
    try:
        conforming_triples = ""
        triple_index = 0
        iter_count = 1
        while triple_index < len(mapping):
            if mapping[triple_index] == "":
                break

            # print(iter_count % 3, triple_index, mapping[triple_index])
            if  iter_count  % 3 == 0:
                conforming_triples += " " + mapping[triple_index] + ". \n" 
            else:
                conforming_triples += " " + mapping[triple_index]
                triple_index += 1

            iter_count += 1

        return conforming_triples + " '" + data_value + "'. \n\n"
    except Exception as e:
        print("Error Creating triples: " + e)



            




def main():
    try:
        output_file = open(conforming_triples_output, "w")
        my_data_map = {} # My Data dictional - keys: Data Proptery , Value: MyDataOntologyExpansion

        # Reading the mapping file 
        with open(mapping_file, newline='') as mapping:
            mapping_reader = csv.reader(mapping, delimiter=',', quotechar='|')
            for row in mapping_reader:
                data_attribute = row[0] # Get the key for my_data_map 
                my_data_map[data_attribute] = row[1:] # Assigns the MyDataOntologyExpansion to the key 
            
        # Reading the raw data file
        with open(raw_data_file, newline='') as raw_data:
            raw_data_reader = csv.reader(raw_data, delimiter=',', quotechar='|')
            headers = next(raw_data_reader)
            for row in raw_data_reader: # Iterates though each row of the raw data
                for index, col in enumerate(row): # Itererates though each col of the raw data 
                    attribute = headers[index]
                    data_value = col
                    if attribute not in my_data_map.keys(): # Check the map covers the terms 
                        print("There is not mapping for: " + attribute)
                    else: 
                        mapping =  my_data_map[attribute]
                        
                        output_file.write(createTriples(mapping,data_value ))
            
        output_file.close()               
    
    except Exception as e:
        print("Error Reading Raw data: " + e)

if __name__ == "__main__":
    main()