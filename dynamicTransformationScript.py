import csv
import uuid

# Two Inputs Files 
##################################################
raw_data_file = './dev/my-data-org-source-data.csv'
mapping_file = './dev/mapping-mydata_org-mdo.csv'
##################################################

# Output file
##################################################
conforming_triples = './output/my-data-instances'
##################################################


def main():
    try:
        my_data_map = {} # My Data dictional - keys: Data Proptery , Value: MyDataOntologyExpansion

        # Reading the mapping file 
        with open(mapping_file, newline='') as mapping:
            mapping_reader = csv.reader(mapping, delimiter=',', quotechar='|')
            for row in mapping_reader:
                data_attribute = row[0] # Get the key for my_data_map 
                my_data_map[data_attribute] = row[1:] # Assigns the MyDataOntologyExpansion to the key 
            
            
        # Reading the raw data file
        with open(raw_data_file, newline='') as raw_data:
            print(my_data_map) # Prints the dictionay  
            
            # TODO 
            # Use the my Data Map to match the raw data to the correct mapping

              
    except Exception as e:
        print("Error Reading Raw data: " + e)

if __name__ == "__main__":
    main()