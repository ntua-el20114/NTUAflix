#!/bin/bash

dir_name=03115074_$(date +"%Y_%m_%d_%I_%M_%p") 
mkdir "$dir_name"
touch "$dir_name"/prompts.txt
cp ./se23_questionnaire_template.json "$dir_name"/template.json
