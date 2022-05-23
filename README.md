# Better-Raids
A Touchportal Plugin to make your Twitch Raids easier

## Documentation
Here, I am going to explain how to install and use the free Better Raids plugin for Touchportal.

### Get started
1. Download the .tpp file [here](https://github.com/Levithan7/Better-Raids/blob/main/BetterRaid%20Testpage.tpz)
2. Import it into tochportal as [usual](https://www.touch-portal.com/blog/post/tutorials/import-plugin-guide.php#:~:text=Importing%20a%20plugin%20file&text=A%20Touch%20Portal%20plug%2Din%20file%20has%20the%20.,icon%20in%20the%20system%20tray.)
3. Download the [example page](https://github.com/Levithan7/Better-Raids/blob/main/BetterRaid%20Testpage.tpz)
4. Import them into Touch Portal
5. You might need to restart TouchPortal. If you open the Page on your phone and the buttons seem "glitchy" you need to exit the page, then restart touchportal and then go back into the page. If that doesn't help you, please contact me. Restarting Touchportal should only be needed after importing the plugin.
6. To create all the needed Touchportal dynamic Values, you need to press the "Create" Button (The icon is a big pencil). You need to do this everytime you want to **add a new streamer**
7. Now you need to edit all the streamers buttons. In the tab "On Pressed" insert the Streamers name like this: Raid("/raid <name>"). Then, in the "On Event" Tab, you need to select the correct state right after "When the plug-in state" for both events.
8. To refresh the streamer buttons, press the "Refresh" Button (Two circeling arrows). You need to do this every time you want to **refresh your streamers online states** Online streamers will be marked as green and offline streamers will be marked as red. 
9. To raid a streamer, simply press the button with his name on it
10. To cancel a raid, simply press the "Cancel Raid" Button

### How to customize
#### The Create Action
This action is called "Create Streamer States". You already used it in step 5. in "Get Started".
You can add multiple streamers by splitting their names with a comma like this: Create(Name1,Name2,Name3)
Please note **that you must not use spaces between the names. Only commas*

### The Check Action
This action is called "Check for streamers". You already used it in step 6. in "Get Started".
You can add multiple streamers by splitting their names with a comma like this: Refresh(Name1,Name2,Name3)
Please note **that you must not use spaces between the names. Only commas**
  
## Contact
If you have a problem or a question, contact me on Discord.
**Levithan#3125**
