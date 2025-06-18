function getDeltaFolder()
{
    find . -name "*delta_*" -type d
}

pip install -r requirements.txt
folder=$(getDeltaFolder)
mv $folder/* $folder/.* .
rm -r $folder/
