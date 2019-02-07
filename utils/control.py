import sys
import json

from pathlib import Path

class Control:
    """
    This is a class to handle the user control file.
    
    Attributes:
        filename {str} -- the full filename of the control file
    """

    def __init__(self, filename: str):
        """
        The constructor for the Control class
        
        Arguments:
            filename {str} -- the full filename of the control file
        """
        
        # Validates the file
        file = Path(filename)
        if not file.is_file():
            sys.exit("Error: Could not find control file.")
        if not filename.endswith(".json"):
            sys.exit("Error: Control file type is invalid. Must be type \".json\".")
        
        # Reads the filename
        f = open(filename)
        self.__settings = json.load(f)

    def get_requests(self, field: str):
        """
        Returns the user-specified subfields based on the specified field
        
        Arguments:
            field {str} -- the field from which to pull subfields from (e.g. "stocks", "reference", "iexmarket", "iexstats", "market")
        
        Returns:
            {[str]} -- a list of subfields under the specified field
        """
        
        # Validates field input
        if field not in self.__settings["fields"]:
            sys.exit(f"Error: \"{field}\" is not a valid field.")
        
        # Determines which subfields have been selected
        subfields = []
        for key, val in self.__settings["fields"][field].items():
            if val == 1:
                subfields.append(key)
        return subfields

    def get_companies(self):
        """
        Gets the user-specified company name

        Returns:
            {[str]} -- the user-specified company name
        """

        return self.__settings["companies"]

    def get_fields(self):
        """
        Gets all fields of interest, excluding those with no selected subfields.
        
        Returns:
            {[str]} -- the list of fields of interest
        """

        fields = []

        for field in list(self.__settings["fields"]):
            if len(self.get_requests(field)) is not 0:
                fields.append(field)

        return fields

#TODO: Remove this test code
if __name__ == "__main__":
    c = Control(r"C:\Users\Syihan Muhammad\Documents\Projects\stockbot\control_file.json")
    print(c.get_companies())
    print(c.get_fields())
    print(c.get_requests())
