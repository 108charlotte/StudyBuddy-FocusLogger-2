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

document.addEventListener("DOMContentLoaded", async function() {
    let runningFocusTimeEl = document.getElementById("running-focus-time-el");
    let totalFocusTimeEl = document.getElementById("total-focus-time-el");

    chrome.storage.local.get(['session-hours', 'session-minutes', 'session-seconds'], function(result) {
        let hours = result['session-hours'] || 0;
        let minutes = result['session-minutes'] || 0;
        let seconds = result['session-seconds'] || 0;

        runningFocusTimeEl.textContent = `Session Duration: ${hours}h ${minutes}m ${seconds}s`; 
    });

    try {
        // Send a message to background.js to update the total time
        await sendMessage("updateTotalTime");

        // Send a message to background.js to get the total time after updating it
        let totalResponse = await sendMessage("getTotalTime");
        let totalHours = totalResponse.hours || 0;
        let totalMinutes = totalResponse.minutes || 0;
        let totalSeconds = totalResponse.seconds || 0;

        totalFocusTimeEl.textContent = `Total Focus Time: ${totalHours}h ${totalMinutes}m ${totalSeconds}s`;

        // Send a message to background.js to update the table data
        await sendMessage("updateTable");

        // Generate the table immediately after updating the table data
        await generateTable();

        console.log("Table generated and updated"); // Debugging log
    } catch (error) {
        console.error("Error:", error);
    }
});

async function generateTable() {
    return new Promise((resolve, reject) => {
        // Retrieve stored table data from chrome.storage.local
        chrome.storage.local.get('table', function(result) {
            if (chrome.runtime.lastError) {
                return reject(chrome.runtime.lastError);
            }

            console.log("Table data retrieved:", result.table);

            let rows;
            try {
                rows = JSON.parse(result.table || '[]');
            } catch (e) {
                return reject("Failed to parse table data");
            }

            console.log("Parsed rows:", rows);

            let rowEl = document.getElementById("row-el");
            if (!rowEl) {
                return reject("Element with ID 'row-el' not found");
            }

            // Clear existing rows
            rowEl.innerHTML = '';

            // Generate table rows from stored data
            rows.forEach(function(element) {
                console.log("Adding row:", element);
                let new_row = `
                <tr>
                    <td>${element.startTime}</td>
                    <td>${element.duration}</td>
                    <td>${element.goal}</td>
                </tr>`;
                rowEl.innerHTML += new_row;
            });

            resolve();
        });
    });
}

// Redirect if the page was reloaded
if (performance.navigation.type === performance.navigation.TYPE_RELOAD) {
    window.location.href = "index.html";
}