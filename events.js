document.addEventListener('DOMContentLoaded', async function() {
    const eventsContainer = document.getElementById('events-container');
    eventsContainer.innerHTML = '<div class="loading">Loading events...</div>';

    try {
        const response = await fetch('http://127.0.0.1:11000/events.json');
        if (response.ok) {
            const events = await response.json();
            eventsContainer.innerHTML = '';  // Clear loading message
            events.forEach(event => {
                const eventElement = document.createElement('div');
                eventElement.className = 'event';
                eventElement.innerHTML = `
                    <div class="event-header">
                        <h2>${event.title}</h2>
                        <p>${event.date}</p>
                    </div>
                    <div class="event-body">
                        <p>${event.description}</p>
                        <button class="details-button">More details</button>
                        <div class="event-details">Additional event information here...</div>
                    </div>`;
                eventElement.querySelector('.details-button').addEventListener('click', () => {
                    const details = eventElement.querySelector('.event-details');
                    details.classList.toggle('show');
                });
                eventsContainer.appendChild(eventElement);
            });
        } else {
            eventsContainer.innerHTML = 'Error loading events.';
        }
    } catch (error) {
        eventsContainer.innerHTML = 'Network error: ' + error.message;
    }
});
