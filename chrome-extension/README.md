# StudyBuddy
A small project intended to allow middle and high school students to track their productivity in order to see progress and what does and doesn't work for them by adding tags to track their focus levels and possible influencers

# Focus-Logger Extension
An extension to help you keep track of time spent in focus. 

index.html - home page, displays total focus time, includes goal input box to help users stay on task, and start button along with table to show previous focus sessions. 

index.js - javascript file that runs index.html, handles start button actions and uploading goal from textbox to chrome memory. 

in-focus.html - page which displays running focus time, when a session is going this is what is displayed

in_focus.js - runs in-focus.html, handles uploading session time to memory so that it can be accessed once session is ended, along with the actual stopwatch function. The stopwatch I used was adapted from mihirsukhadiya (github username)'s knovator-timer-track repository. I could not find a liscense type so I hope this was enough! 

background.js - handles the actual timer updating (what i said in_focus.js did)--in_focus.js just updates the display, while background.js runs in the background and updates the timer constantly, even if the extension is closed. 

FOR BOTH OF THESE PARTS I USED THE HELP OF AI SUCH AS GITHUB COPILOT AND CHATGPT. 