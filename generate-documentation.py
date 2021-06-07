#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=unused-variable

# Owned
__author__ = "Audrey Carval"
__credits__ = ["Sébastien Brun", "Frédéric Spiers"]
__license__ = "----"
__date__ = "15/06/2021"
__maintainers__ = ["Audrey Carval"]
__email1__ = "carval.audrey@gmail.com"


############################################################################
################################## Import #################################
############################################################################

import os
import sys
import shutil
import json
import yaml
import re
import argparse


############################################################################
################################# Functions ################################
############################################################################

nl = '\n'

def parse():
    parser = argparse.ArgumentParser(description='Generate documentation from a tekton folder')
    parser.add_argument('--dst-dir', nargs='?', type=str, const="./documenation", help="Folder's path where the documentation will be generated. If the folder already exist, the files inside will be deleted.")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('--tekton-dir', type=str, help="Tekton's sources folder path", required=True)
    args = parser.parse_args()
    return args

# Remove a given folder and its content
def delete_folder(folder_path): 
    # checking whether folder exists or not
    if os.path.exists(folder_path):
        # removing the file using the os.rmtree() method
        shutil.rmtree(folder_path)

def create_table(documentation_file, tekton_object_index, next_title_number, kind, name, params):
    documentation_file.write(f"##{str(tekton_object_index+1)}- {kind} {name.join(nl).join(nl).join(nl)}")
    documentation_file.write(f"###{str(next_title_number)}- {kind}'s params details{nl}")
    documentation_file.write("| NAME   |      DEFAULT      |  DESCRIPTION |\n")
    documentation_file.write("|----------|-------------|----------------------|\n")
    for param_index, param in enumerate(params):
        name=param.get("name")
        default=param.get("default", "/")
        description=param.get("description", "/")
        description=" ".join(description.split())
        documentation_file.write(f"| {name} | {str(default)} | {description} |{nl}")

def create_table_trigger_binding(documentation_file, tekton_object_index, next_title_number, kind, name, params):
    documentation_file.write(f"##{str(tekton_object_index+1)}- {kind} {name}{nl}{nl}")
    documentation_file.write(f"###{str(next_title_number)}- {kind}'s params details{nl}")
    documentation_file.write("| NAME   |      VALUE      |\n")
    documentation_file.write("|----------|-------------|\n")
    for param_index, param in enumerate(params):
        name=param.get("name")
        value=param.get("value", "/")
        documentation_file.write(f"| {name}  |  {str(value)}  |{nl}")

# Generate a mermaid schema
def generate_mermaid_schema(documentation_file, tasks, kind = "tasks", next_title_number=1,access_key = "params",):
    documentation_file.write(f"### {str(next_title_number)}- {kind} 's details{nl}")
    documentation_file.write('```mermaid\nclassDiagram\n')
    for task_index, task in enumerate(tasks):
        # Replace - with _ to no cause issue with mermaid
        task_name=task.get("name").replace("-", "_")
        task_params=task.get(access_key, "")
        task_run_after_list=task.get("runAfter")
        documentation_file.write('class '+task_name+'{\n')
        
        # Indicate step or task params
        if len(task_params):
            for task_param_index, task_param in enumerate(task_params):
                task_param_name=task_param.get('name')
                task_param_value=task_param.get('value', "")
                documentation_file.write(f"        {task_param_name} : {task_param_value} {nl}")
        
        documentation_file.write('    }\n')
        
        # Indicate link between task
        if task_run_after_list: 
            for task_run_after_index, task_run_after in enumerate(task_run_after_list):
                task_run_after_formatted=task_run_after.replace("-", "_")
                documentation_file.write(f"   {task_run_after_formatted} --|> {task_name}{nl}")
        
        # Indicate link between step
        if access_key=="env" and task_index < len(tasks)-1 and len(tasks) >= 2:
            stepAfter=tasks[task_index+1].get("name")
            stepAfter=stepAfter.replace("-", "_")
            documentation_file.write(f"    {task_name} --|> {stepAfter}{nl}")
    
    documentation_file.write('```\n')
    next_title_number=next_title_number+1
    
def generate_documentation(tekton_folder, destination_folder):
    if not os.path.exists(tekton_folder):
        print(f"The folder {tekton_folder} does not exist")
        return
    #delete old documentation
    delete_folder(destination_folder)

    #create destination folder
    os.mkdir(destination_folder)

    #for each yml file create a documentation documentation
    for root, dirs, files in os.walk(tekton_folder):
        for file in files:
            documentation_file_name=re.sub('yml|yaml',  "md", file)
            documentation_file = open(destination_folder+ "/"+documentation_file_name, "a")
            documentation_file.write("#Tekton documentation\n\n")
            with open(tekton_folder+"/"+file, 'r') as stream:
                try:
                    print(f"Processing file {tekton_folder}/{file}...")
                    tekton_objects = yaml.load_all(stream, Loader=yaml.FullLoader)
                    # For each yaml object (task, pipeline...) create some documetation
                    for tekton_object_index, tekton_objet in enumerate(tekton_objects):
                        next_title_number=1
                        kind=tekton_objet.get("kind")
                        spec=tekton_objet.get("spec")
                        tasks=spec.get("tasks", "")
                        steps=spec.get("steps", "")
                        params=spec.get("params")
                        results=spec.get("results")
                        name=tekton_objet.get("metadata").get("name")

                        if kind == 'EventListener':
                            continue

                        # Params table
                        documentation_file.write("----\n")
                        if params:
                            if kind == 'TriggerBinding':
                                create_table_trigger_binding(documentation_file, tekton_object_index, next_title_number, kind, name, params)
                            else: 
                                create_table(documentation_file, tekton_object_index, next_title_number, kind, name, params)
                            next_title_number=next_title_number+1

                        # Result table
                        if results: 
                            documentation_file.write(f"### {str(next_title_number)} - {kind}'s output details{nl}{nl}")
                            documentation_file.write("| NAME   | DESCRIPTION |\n")
                            documentation_file.write("|----------|-------------|\n")

                            for result_index, result in enumerate(results):
                                result_name=result.get("name")
                                result_description=result.get("description", "/")
                                result_description=" ".join(result_description.split())
                                documentation_file.write(f"| {result_name}  |  {result_description} |{nl}")
                            
                            next_title_number=next_title_number+1

                        # Tasks mermaid schema
                        if len(tasks):
                            generate_mermaid_schema(documentation_file, tasks, "Tasks", next_title_number)
                        
                        # Steps mermaid schema
                        if len(steps):
                            generate_mermaid_schema(documentation_file, steps, "Steps", next_title_number, "env")    
                except yaml.YAMLError as exc:
                    print(exc)

############################################################################
################################### Main ###################################
############################################################################

def main(): 
    args = parse()
    tekton_folder = getattr(args, 'tekton_dir')
    destination_folder = getattr(args, 'dst_dir')
    generate_documentation(tekton_folder, destination_folder)

if __name__ == "__main__":
    main()
