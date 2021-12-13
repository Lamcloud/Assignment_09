#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# SLam, 2021-Dec-12, Added code for TODO's
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO
import DataClasses as DC

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        print('lstOfCDObjects:', lstOfCDObjects)
        cd_idx = int(input('Select the CD / Album index: ').strip())
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        print('cd info: ', cd.cd_id, cd.cd_title, cd.cd_artist)
        # TODone add code to handle tracks on an individual CD
        IO.ScreenIO.print_CD_menu()
        strCDChoice = IO.ScreenIO.menu_CD_choice()
        if strCDChoice == 'a':
            print('Enter track ID, track title, track length: ')
            trkId, trkTitle, trkLength = IO.ScreenIO.get_track_info()
            track = DC.Track(int(trkId), trkTitle, trkLength)
            cd.add_track(track)
            IO.ScreenIO.show_tracks(cd)

        elif strCDChoice == 'd':
            try:
                IO.ScreenIO.show_tracks(cd)
            except Exception as e:
                print(e)

        elif strCDChoice == 'r':
            t = int(input('Which track to remove from this CD? '))
            cd.rmv_track(t)
        elif strCDChoice == 'x':
            continue
        else:
            print('General error.')
        
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')