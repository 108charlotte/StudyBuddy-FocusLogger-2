async function sendMessage(action) {
    return new Promise((resolve, reject) => {
        chrome.runtime.sendMessage({ action: action }, (response) => {
            if (chrome.runtime.lastError) {
                return reject(chrome.runtime.lastError);
            }
            resolve(response);
        });
    });
}

document.addEventListener("DOMContentLoaded", function() {
    let goalInputEl = document.getElementById("goal-el");

    async function startFocusSession() {
        if (goalInputEl.value.trim() === "") {
            alert("Please enter a goal--failing to prepare is planning to fail!"); 
        } else {
            console.log("New session started"); 

            chrome.storage.local.set({ 'startTime': new Date().toISOString() });
            chrome.storage.local.set({ 'goal': goalInputEl.value });
            chrome.storage.local.set({ 'running': true });

            // Clear session history only when starting a new session
            await sendMessage("resetTimer");
            await sendMessage("startTimer");

            setTimeout(function() {
                chrome.action.setPopup({ popup: "in_focus.html" });
                window.location.href = "in_focus.html"; 
            }, 100); 
        }
    }

    let startButton = document.getElementById("start-el"); 

    if (startButton) {
        startButton.addEventListener("click", startFocusSession);
    }

    // Check if a session is already running
    chrome.storage.local.get('running', function(result) {
        if (result.running) {
            chrome.action.setPopup({ popup: "in_focus.html" });
            window.location.href = "in_focus.html";
        } else {
            chrome.action.setPopup({ popup: "index.html" });
        }
    });

    // Save state before the popup is closed
    window.addEventListener('beforeunload', function() {
        chrome.storage.local.get(['total-hours', 'total-minutes', 'total-seconds'], function(result) {
            let state = {
                'total-hours': result['total-hours'] || 0,
                'total-minutes': result['total-minutes'] || 0,
                'total-seconds': result['total-seconds'] || 0
            };
            chrome.storage.local.set(state, function() {
                console.log('State saved:', state); // Debugging log
            });
        });
    });
});