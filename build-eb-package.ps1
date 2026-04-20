# Creates a zip file ready to upload to AWS Elastic Beanstalk
# Run from the repo root: .\build-eb-package.ps1

$output = "eb-deploy.zip"

# Remove old zip if present
if (Test-Path $output) { Remove-Item $output }

# Files and folders to include
$include = @(
    "Dockerfile",
    "Dockerrun.aws.json",
    "requirements.txt",
    "app",
    "rag",
    "data\chunks"
)

Add-Type -Assembly "System.IO.Compression.FileSystem"
$zip = [System.IO.Compression.ZipFile]::Open(
    (Join-Path $PWD $output),
    [System.IO.Compression.ZipArchiveMode]::Create
)

foreach ($item in $include) {
    if (Test-Path $item -PathType Leaf) {
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
            $zip, (Resolve-Path $item), $item
        ) | Out-Null
    } elseif (Test-Path $item -PathType Container) {
        Get-ChildItem -Path $item -Recurse -File | ForEach-Object {
            $entryName = $_.FullName.Substring($PWD.Path.Length + 1)
            [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
                $zip, $_.FullName, $entryName
            ) | Out-Null
        }
    }
}

$zip.Dispose()

$size = [math]::Round((Get-Item $output).Length / 1MB, 1)
Write-Host ""
Write-Host "✅ Created $output ($size MB)"
Write-Host ""
Write-Host "Next: upload this file to AWS Elastic Beanstalk"
Write-Host "  1. Go to https://console.aws.amazon.com/elasticbeanstalk"
Write-Host "  2. Create application -> Upload your code -> choose eb-deploy.zip"
