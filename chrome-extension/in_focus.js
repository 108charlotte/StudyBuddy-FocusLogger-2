let interval;

function updateDisplay(display, time) {
    display.innerHTML = `<p>Running Focus Time: ${Math.floor(time / 3600).toString().padStart(2, "0")}:${Math.floor((time % 3600) / 60).toString().padStart(2, "0")}:${Math.floor(time % 60).toString().padStart(2, "0")}</p>`;
}

function stopTimer() {
    chrome.runtime.sendMessage({ action: "stopTimer" });
    clearInterval(interval);
    interval = null;
}

function endFocusSession() {
    stopTimer(); // Ensure the timer stops
    chrome.action.setPopup({ popup: "index.html" });
    window.location.href = "done.html";
}

document.addEventListener("DOMContentLoaded", function() {
    let focusTimeEl = document.getElementById("focus-time-el");
    let goalEl = document.getElementById("goal-text-el");

    // Retrieve goal from chrome.storage and display it
    chrome.storage.local.get('goal', function(result) {
        goalEl.textContent += result.goal || '';
    });

    let endButton = document.getElementById("end-el");

    if (endButton) {
        endButton.addEventListener("click", endFocusSession);
    }

    // Listen for messages from background.js to update the display
    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
        if (request.action === "updateDisplay") {
            updateDisplay(focusTimeEl, request.time);
        }
    });

    // Retrieve stored time from chrome.storage
    chrome.storage.local.get(['session-hours', 'session-minutes', 'session-seconds', 'running'], function(result) {
        let storedHours = parseInt(result['session-hours']) || 0;
        let storedMinutes = parseInt(result['session-minutes']) || 0;
        let storedSeconds = parseInt(result['session-seconds']) || 0;

        // Update the display with the stored time
        updateDisplay(focusTimeEl, storedHours * 3600 + storedMinutes * 60 + storedSeconds);

        // Start the timer if it is running
        if (result.running) {
            chrome.runtime.sendMessage({ action: "startTimer" });
        }
    });
});