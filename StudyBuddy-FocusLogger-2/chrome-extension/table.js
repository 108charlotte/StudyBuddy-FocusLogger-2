let goalInputEl = document.getElementById("goal-el");

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM content loaded");

    let focusTime = document.getElementById("total-focus-time-el"); 

    chrome.storage.local.get(['total-hours', 'total-minutes', 'total-seconds'], function(result) {
        let hours = result['total-hours'] || 0;
        let minutes = result['total-minutes'] || 0;
        let seconds = result['total-seconds'] || 0;

        focusTime.textContent = `Total Focus Time: ${hours}h ${minutes}m ${seconds}s`; 
    });

    // Call generateTable to populate the table
    generateTable().then(() => {
        console.log("Table generated successfully");
    }).catch((error) => {
        console.error("Error generating table:", error);
    });
});

function generateTable() {
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