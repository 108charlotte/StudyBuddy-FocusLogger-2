# Changelog

## [1.25] - 2025-1-5
Table finally updating, but delayed, along with the total focus time display on the done page. The index page isn't displaying anything next to total focus time (due to another naming discrepancy). 

Debugging notes
- updated data before storing is correct


## [1.24] - 2025-1-4
Issues: 
- total focus time doesn't include most recent session
- table not updating
Updates recorded in github history with push request thingees

## [1.24] - 2025-1-4
miscillaneous changes, nothing is actually improving its just getting worse

## [1.23] - 2025-1-4
attempts to resolve issues outlined in 1.22

## [1.22] - 2025-1-4
TODO: stopwatch no longer working, tried to fix it and removed redundant code
Notes for this version: 
- session-seconds exist but are not updating on the GUI
- session minutes is deleted when end button clicked

## [1.21] - 2025-1-4
continued trying to fix error with session variables being innapropriately deleted

## [1.20] - 2025-1-4
deleted call to reset timer in in_focus.js endFocusSession(). I don't know why I put it there in the first place. 

## [1.19] - 2025-1-4
removes code which wipes session memory when index.html is opened--since opening extension always reroutes to index.html, this could be leading to data being deleted randomly when its not supposed to be

## [1.18] - 2025-1-4
setting running to false does nothing--I didn't have a reset function, so I added that and call it in endSession. 

## [1.17] - 2025-1-4
to-fix: retrieved session time always says 0
This version: sets running to false in 3 different places--likely the reason why the timer kept going. Then i'll fix the issue with not retrieving data. 

## [1.16] - 2025-1-4
- aims to fix time not deleted after running by altering background.js file

## [1.15] - 2025-1-4
- time also not deleted after running--looks like this is a bigger issue with data storage in general

## [1.14] - 2025-1-4
- nothing saved in storage, trying to fix issue

## [1.13] - 2025-1-4
TODO: fix done page not displaying times
- timer wasn't resetting when end button clicked
- done page isn't displaying total time or run time, and nothing in memory
- total focus time also isn't updating

## [1.12] - 2025-1-3
Stopwatch does not continue updating when extension is closed, tries to fix this

## [1.11] - 2025-1-3
Version 1.10 updates have finally fixed issues with reloading restarting the timer
### New Issues
- index total focus time displaying time twice
- done screen not showing focus time, running or total


## [1.10] - 2025-1-3
### Trying to Fix
- Extension deleting all data when closed

### Fixed
- Issue with goalInputEl being declared multiple times


## [1.9] - 2025-1-3
## Trying to Fix
- Extension deleting all data when closed

### Added
- Dynamic popup adjustment based on session state.

### Fixed
- Stopwatch not recording time correctly when popup is closed and reopened.
- Various minor bug fixes and performance improvements.


## Previous Versions
Undocumented changes

## 1.0
First launch from extensions bar