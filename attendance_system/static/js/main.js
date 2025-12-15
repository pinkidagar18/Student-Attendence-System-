// Common JavaScript functions for the application

// Show a custom alert/toast message
function showAlert(message, type = 'info', duration = 3000) {
    // Create alert element
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.top = '20px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '9999';
    alertDiv.style.maxWidth = '300px';
    
    // Set content
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // Add to document
    document.body.appendChild(alertDiv);
    
    // Auto-dismiss
    setTimeout(() => {
        alertDiv.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(alertDiv);
        }, 150);
    }, duration);
}

// Format date for display
function formatDate(dateString) {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Check if camera is available
function checkCameraAvailability() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        showAlert('Camera access is not supported in this browser. Please use a modern browser.', 'danger');
        return false;
    }
    return true;
}

// Validate form inputs
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    return form.checkValidity();
}

// Document ready event
document.addEventListener('DOMContentLoaded', function() {
    // Initialize any Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Add current year to footer if it exists
    const footerYearEl = document.getElementById('current-year');
    if (footerYearEl) {
        footerYearEl.textContent = new Date().getFullYear();
    }
});
