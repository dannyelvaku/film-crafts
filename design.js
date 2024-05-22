// Open modal with clicked image
function openModal(imageSrc) {
    var modal = document.getElementById('modal');
    var modalImage = document.getElementById('photos/DANN.jpg');
    modal.style.display = 'block';
    modalImage.src = imageSrc;
}

// Close modal
function closeModal() {
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
}
// Function to set ticket type and price
function setTicketInfo(ticketType, ticketPrice) {
    document.getElementById('ticket-type').value = ticketType;
    document.getElementById('ticket-price').value = ticketPrice;
}

// Function to buy regular ticket
function buyRegularTicket() {
    setTicketInfo('Regular', 200);
}

// Function to buy VIP ticket
function buyVIPTicket() {
    setTicketInfo('VIP', 500);
}
