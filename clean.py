import lkml
import os
from os import path

# loop through cwd
for filename in os.listdir(os.getcwd()): 
    # get extension files (non base files)
    if not filename.endswith("__base.view.lkml") and filename.endswith(".view.lkml"):
        # if filename + filename_base exists, take action
        filename_base = filename[:-10] + '__base.view.lkml'
        if path.exists(filename_base):
            # open extension file
            with open(filename, 'r') as file:
                # parse lookml
                parsed = lkml.load(file)
                # create an empty array to store fields that are shown on extension
                shown_on_extension = []
                # loop through dimensions
                if 'dimensions' in parsed:
                    for dim in parsed['dimensions']:
                        # if dim is shown, add id to array
                        if dim['hidden'] == 'no':
                            shown_on_extension.append(dim['name'])
                if 'dimension_groups' in parsed:
                    for dim_group in parsed['dimension_groups']:
                        # if dimension group is shown, add id to array
                        if dim_group['hidden'] == 'no':
                            shown_on_extension.append(dim_group['name'])
                if 'measures' in parsed:
                    for measure in parsed['measures']:
                        # if measure is shown, add id to array
                        if measure['hidden'] == 'no':
                            shown_on_extension.append(measure['name'])
        
            # open the base file
            with open(filename_base, 'r') as file: 
                # parse lookml
                parsed = lkml.load(file)
                # create an empty array to store fields that should be commented out
                fields_to_be_removed = []
                if 'dimensions' in parsed:
                    for dim in parsed['dimensions']:
                        # if dim is not shown in the extension, add to array of fields to be commented out
                        if dim['name'] not in shown_on_extension:
                            fields_to_be_removed.append(dim['name'])
                if 'dimension_groups' in parsed:
                    for dim_group in parsed['dimension_groups']:
                        # if dimension group is not shown in the extension, add to array of fields to be commented out
                        if dim_group['name'] not in shown_on_extension:
                            fields_to_be_removed.append(dim_group['name'])
                if 'measures' in parsed:
                    for measure in parsed['measures']:
                        # if measure is not shown in the extension, add to array of fields to be commented out
                        if measure['name'] not in shown_on_extension:
                            fields_to_be_removed.append(measure['name'])
                            
        print(shown_on_extension)

        # fields never shown in UI - to be commented out
        print(fields_to_be_removed)
