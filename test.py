# import optparse
# parser = optparse.OptionParser()
# parser.add_option("-i", "--input",
#                   dest = "input_file",
#                   help = "Include the input file to be changed",
#                   metavar = "FILE")
# parser.add_option("-u", "--update",
#                     action="store_true",
#                     dest = "update", default = False,
#                     help = "update the version of the library")
                    

# (options, args) = parser.parse_args()

# print(options,args)

from modules.version_check import check_version



print(check_version("18.0.3","17.0.2"))