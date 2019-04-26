from Filtering import *

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    ssf = SpatialFilters()
    ssf.read_image (input_file)
    ssf.process (output_file, "avg")
    

