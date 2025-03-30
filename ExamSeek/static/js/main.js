document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
        });
    }
    
    // Exam Save/Unsave Functionality
    const saveExamButtons = document.querySelectorAll('.save-exam-btn');
    const unsaveExamButtons = document.querySelectorAll('.unsave-exam-btn');
    
    saveExamButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const examId = this.dataset.examId;
            saveExam(examId, this);
        });
    });
    
    unsaveExamButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const examId = this.dataset.examId;
            unsaveExam(examId, this);
        });
    });
    
    function saveExam(examId, button) {
        fetch('/save_exam/' + examId, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.textContent = 'Saved';
                button.disabled = true;
                button.classList.remove('btn-primary');
                button.classList.add('btn-secondary');
                showAlert('Exam saved successfully!', 'success');
            } else {
                showAlert(data.message || 'Failed to save exam.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error saving exam:', error);
            showAlert('An error occurred while saving the exam.', 'danger');
        });
    }
    
    function unsaveExam(examId, button) {
        fetch('/unsave_exam/' + examId, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const container = button.closest('.saved-exam-item');
                if (container) {
                    container.remove();
                } else {
                    button.textContent = 'Save';
                    button.classList.remove('btn-secondary');
                    button.classList.add('btn-primary');
                    button.disabled = false;
                }
                showAlert('Exam removed from your saved list.', 'info');
            } else {
                showAlert(data.message || 'Failed to remove exam.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error removing exam:', error);
            showAlert('An error occurred while removing the exam.', 'danger');
        });
    }
    
    // Alert function
    function showAlert(message, type) {
        const alertContainer = document.getElementById('alert-container');
        if (!alertContainer) return;
        
        const alertElement = document.createElement('div');
        alertElement.className = `alert alert-${type}`;
        alertElement.textContent = message;
        
        alertContainer.appendChild(alertElement);
        
        // Auto-remove after 3 seconds
        setTimeout(() => {
            alertElement.remove();
        }, 3000);
    }
    
    // Toggle elements with data-toggle attribute
    const toggleElements = document.querySelectorAll('[data-toggle]');
    
    toggleElements.forEach(element => {
        element.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.dataset.target;
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const isVisible = targetElement.style.display !== 'none';
                targetElement.style.display = isVisible ? 'none' : 'block';
                
                // Update toggle text if data-toggle-text is present
                if (this.dataset.toggleText) {
                    const currentText = this.textContent;
                    this.textContent = this.dataset.toggleText;
                    this.dataset.toggleText = currentText;
                }
            }
        });
    });
});
