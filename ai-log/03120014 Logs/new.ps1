$dateSuffix = Get-Date -Format "yyyy_MM_dd_hh_mm_tt"
$dirName = "03120014_$dateSuffix"

New-Item -ItemType Directory -Path $dirName
New-Item -ItemType File -Path "$dirName\prompts.txt"
Copy-Item -Path "template.json" -Destination "$dirName\template.json"
Copy-Item -Path "zip.ps1" -Destination "$dirName\zip.ps1"
