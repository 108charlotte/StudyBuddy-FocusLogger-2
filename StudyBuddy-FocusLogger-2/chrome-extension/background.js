let time = 0;
let interval;

function startTimer() {
    if (interval) {
        clearInterval(interval);
    }

    interval = setInterval(() => {
        time += 1;
        chrome.storage.local.set({
            'session-hours': Math.floor(time / 3600).toString(),
            'session-minutes': Math.floor((time % 3600) / 60).toString(),
            'session-seconds': Math.floor(time % 60).toString(),
            'running': true // Indicates that the timer is running
        });

        // Send a message to update the display
        chrome.runtime.sendMessage({ action: "updateDisplay", time: time });
    }, 1000);
}

function stopTimer() {
    clearInterval(interval);
    interval = null;
    chrome.storage.local.set({ 'running': false }); // Indicates that the timer is stopped
}

function resetTimer() {
    clearInterval(interval);
    interval = null;
    time = 0; 
    chrome.storage.local.set({
        'session-hours': '0',
        'session-minutes': '0',
        'session-seconds': '0',
        'running': false // Indicates that the timer is stopped
    }, function() {
        console.log('Session variables reset'); // Debugging log
    });
}

function getSessionTime() {
    return {
        hours: Math.floor(time / 3600),
        minutes: Math.floor((time % 3600) / 60),
        seconds: Math.floor(time % 60)
    };
}

function updateTotalTime() {
    return new Promise((resolve) => {
        let sessionTime = getSessionTime();
        let { hours, minutes, seconds } = sessionTime;

        chrome.storage.local.get(['total-hours', 'total-minutes', 'total-seconds'], function(result) {
            let totalHours = parseInt(result['total-hours']) || 0; 
            let totalMinutes = parseInt(result['total-minutes']) || 0; 
            let totalSeconds = parseInt(result['total-seconds']) || 0; 

            totalHours += hours; 
            totalMinutes += minutes; 
            totalSeconds += seconds; 

            chrome.storage.local.set({ 
                'total-hours': totalHours.toString(),
                'total-minutes': totalMinutes.toString(),
                'total-seconds': totalSeconds.toString()
            }, function() {
                console.log(`Updated total time: ${totalHours}h ${totalMinutes}m ${totalSeconds}s`); // Debugging log
                resolve();
            });
        });
    });
}

function getTotalTime(callback) {
    chrome.storage.local.get(['total-hours', 'total-minutes', 'total-seconds'], function(result) {
        let totalHours = parseInt(result['total-hours']) || 0; 
        let totalMinutes = parseInt(result['total-minutes']) || 0; 
        let totalSeconds = parseInt(result['total-seconds']) || 0; 

        callback({
            hours: totalHours,
            minutes: totalMinutes,
            seconds: totalSeconds
        });
    });
}

function updateTableData() {
    return new Promise((resolve, reject) => {
        chrome.storage.local.get(['table', 'startTime', 'goal'], function(result) {
            try {
                let rows = JSON.parse(result.table || '[]');
                let startTime = result.startTime || new Date().toISOString();
                let goal = result.goal || '';

                let sessionTime = getSessionTime();
                if (!sessionTime || typeof sessionTime !== 'object') {
                    throw new Error("Invalid session time");
                }

                let duration = `${sessionTime.hours}h ${sessionTime.minutes}m ${sessionTime.seconds}s`;

                // Push an object with named properties into the rows array
                rows.push({ startTime, duration, goal });

                console.log("Updated rows before storing:", rows); // Debugging log

                chrome.storage.local.set({ 'table': JSON.stringify(rows) }, function() {
                    console.log("Data stored successfully"); // Debugging log
                    resolve();
                });
            } catch (error) {
                console.error("Error updating table data:", error);
                reject(error);
            }
        });
    });
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "startTimer") {
        startTimer();
        sendResponse({ status: "Timer started" });
    } else if (request.action === "stopTimer") {
        stopTimer();
        sendResponse({ status: "Timer stopped" });
    } else if (request.action === "resetTimer") {
        resetTimer();
        sendResponse({ status: "Timer reset" });
    } else if (request.action === "updateTable") {
        updateTableData().then(() => {
            sendResponse({ status: "Table updated" });
        }).catch((error) => {
            sendResponse({ status: "Error updating table", error: error });
        });
    } else if (request.action === "getTotalTime") {
        getTotalTime((totalTime) => {
            sendResponse(totalTime);
        });
    } else if (request.action === "updateTotalTime") {
        updateTotalTime().then(() => {
            sendResponse({ status: "Total time updated" });
        }).catch((error) => {
            sendResponse({ status: "Error updating total time", error: error });
        });
    }
    return true; // Required to indicate that the response will be sent asynchronously
});