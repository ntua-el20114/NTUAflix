import datetime, os

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'backup_{timestamp}.sql'
backup_file_path = os.path.join('./back_end/Database', backup_file) #assuming you run this script from the root of the project
# MySQL dump command
mysqldump_cmd = f"mysqldump -h  localhost -u root ntuaflix > {backup_file_path}"
# Execute the mysqldump command
os.system(mysqldump_cmd)