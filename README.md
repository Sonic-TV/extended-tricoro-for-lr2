# What's this?
 A customizable tricoro skin for LR2.  

# What has been changed comparing to the original?
Proper 2P, DP support has been added.  
FAST / SLOW display implemented.
Proper LIFT COVER support has been added and customizable.  
Frames and Effector Display are customizable (in the future, programmable).  
Effector Display actually represents your choice on the "EFFECTORS" tab.  
(Supported Types: PITCH, FX0-2, MASTER VOLUME, KEY / BGM BALANCE)  
Lanes are customizable.  
"Final STAGE" has been changed to "Free MODE".  
Notes, lane beams / key lights are per-lane customizable.  
FC effect codes have been refactored, making them customizable and programmable.

# Requirements
To make everything work, the latest revision of LR2OOL and LR2HackBox is required.  
Grab them here:  
https://github.com/tenaibms/LR2OOL  
https://github.com/MatVeiQaaa/LR2HackBox  
Base program must be F / S patch applied, with latest revision.

# Future Plans
Native 5 and 9 Key Support  
~~Course Result (Done)~~  
Skin Select and Key Config  
Programmable Frames and SystemParts

# Known Bugs / Side Notes
For Doubles, the CHART FILTER needs to switch to DOUBLES for the result screen to display what option has been used properly (due to using `DST_OPTION 10` for switching display modes).  
To avoid bugs on `DST_OPTION 330`, this skin is NOT using `#FLIPXXX` commands for switching sides.  
Please change sides manually if you want to change sides.  
LR2OOL extensions are mostly unsupported in BATTLE mode due to lack of extended digit definitions for 2P side.

# If you want to submit your own customizations......
Contact me on Discord.  
Or send your images to sonic04677(at)gmail(dot)com.

# If you encounter bugs......
Send me an issue on the issues tab.  
You can make the skin better by sending me pull requests as well.


# Will this port to beatoraja / LVF when everything's done?
LVF port is being considered while beatoraja is currently unplanned due to the dev can't do LUAs.  
You can fork this repository if you want to do a beatoraja port.

# Why are you using a skin with an image illegally extracted from beatmania IIDX 20 tricoro?
Bruh.

# For making / porting FC Effects...
1. Make a folder and name it whatever you want.  
2. Use "SP.csv" for SP, "DP.csv" for DP, and "B.csv", "BR.csv" for different sides in BATTLE mode.
Notice that "SP.csv" should contain both sides.
3. All of the texture files should be concentrated to 2 texture files named "main.png“ (gr=19) and "sub.png" (gr=18).
4. Make your own effects and send them either via email or pull requests.
