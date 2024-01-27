$file1Path = ".\prompts.txt"
$file2Path = ".\template.json"
$currentFolderName = (Get-Item $PSScriptRoot).Name

$zipFilePath = ".\$currentFolderName.zip"

Compress-Archive -Path $file1Path, $file2Path -DestinationPath $zipFilePath -Force