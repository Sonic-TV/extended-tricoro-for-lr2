# What's this?
 A customizable tricoro skin for LR2.  

# What has been changed compared to the original?
Proper 2P, DP support has been added.  
FAST / SLOW display implemented.
Proper LIFT COVER support has been added and is customizable.  
Frames and Effector Display are customizable (in the future, programmable).  
Effector Display actually represents your choice on the "EFFECTORS" tab.  
(Supported Types: PITCH, FX0-2, MASTER VOLUME, KEY / BGM BALANCE)  
Lanes are customizable.  
"Final STAGE" has been changed to "Free MODE".  
Notes, lane beams / key lights are per-lane customizable.  
FC effect codes have been refactored to be customizable and programmable.

# Requirements
To make everything work, the latest revision of LR2OOL and LR2HackBox is required.  
Grab them here:  
https://github.com/tenaibms/LR2OOL  
https://github.com/MatVeiQaaa/LR2HackBox  
Base program must be F / S patch applied, with the latest revision.

# Future Plans
Native ~~5 and~~ 9 Key Support  
~~Course Result (Done)~~  
~~Skin Select and Key Config~~  
Programmable Frames and SystemParts (Currently customizable)

# Known Bugs / Side Notes
To avoid bugs on `DST_OPTION 330`, this skin is NOT using `#FLIPXXX` commands for switching sides.  
Please change sides manually if you want to change sides.  
Development for BATTLE-related skins is currently paused due to a lack of extended digit definitions for the 2P side.  
For SkinSelect, only the first 5 blocks are used for parts information, due to LR2's limitations. 6th - 8th blocks are bugged.

# If you want to submit your own customizations......
Contact me on Discord or send your pull requests.  
Or send your images to sonic04677(at)gmail(dot)com.

# If you encounter bugs......
Send me an issue on the issues tab.  
You can make the skin better by sending me pull requests as well.


# Will this port to beatoraja when everything's done?
**No.** The dev can't do LUAs.  
You can fork this repository if you want to do a beatoraja port.

# Why are you using a skin with an image illegally extracted from beatmania IIDX 20 tricoro?
**BRUH. None of your business. PLEASE FUCK OFF and whine on Twitter. I dare you.**

# For making / porting FC Effects...
1. Make a folder and name it whatever you want.  
2. Use "SP.csv" for SP, "DP.csv" for DP, and "B.csv", "BR.csv" for different sides in BATTLE mode.
Notice that "SP.csv" should contain both sides.
3. All of the texture files should be concentrated to 2 texture files named "main.png“ (gr=19) and "sub.png" (gr=18).
4. Make your own effects and send them either via email or pull requests.

# For making customization parts...
Just check the files in `template-for-customize-parts` to make your own.  
PSDs of note bombs and key lights will be provided on a later date.

# About Mascot System......
The mascots should be 160x160px per frame, with 50 frames in the sheet.  
Mascots are in Beat Sync. The image cycles **every 2 counts**.  
Hu Tao's sprites included in the git were originally done by https://space.bilibili.com/2425374 on bilibili.  
Other sprites are originally done by https://space.bilibili.com/104349118?spm_id_from=333.337.0.0 on bilibili. Many Thanks.

# NO CHARGES REQUIRED, BUT...
 If you want to make some donations......  
 Bring it on. Here.  
 `paypal(dot)com(slash)paypalme(slash)sonictvbms`
