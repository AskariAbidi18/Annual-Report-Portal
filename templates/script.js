document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulate authentication (this would be done on the server in a real app)
    if (username === 'admin' && password === 'admin123') {
        // Redirect to Admin Dashboard
        window.location.href = 'admin.html';
    } else if (username === 'user' && password === 'user123') {
        // Redirect to User Dashboard
        window.location.href = 'user.html';
    } else {
        alert('Invalid username or password');
    }
});

function logout() {
    // Redirect to login page
    window.location.href = 'index.html';
}

// Handle profile form submission
document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const regNumber = document.getElementById('regNumber').value;
    const dob = document.getElementById('dob').value;
    const className = document.getElementById('class').value;

    // Simulate saving data (this would be done on the server in a real app)
    alert(`Profile Updated:
Name: ${name}
Registration Number: ${regNumber}
Date of Birth: ${dob}
Class: ${className}`);
});
document.addEventListener('DOMContentLoaded', function() {
    // Show the correct section based on the selected link
    const createReportLink = document.getElementById('createReportLink');
    const myReportsLink = document.getElementById('myReportsLink');
    const profileFormSection = document.getElementById('profileFormSection');
    const reportsSection = document.getElementById('reportsSection');

    createReportLink.addEventListener('click', function() {
        profileFormSection.style.display = 'block';
        reportsSection.style.display = 'none';
    });

    myReportsLink.addEventListener('click', function() {
        profileFormSection.style.display = 'none';
        reportsSection.style.display = 'block';
        displayReports();
    });

    function displayReports() {
        const reportsList = document.getElementById('reportsList');
        reportsList.innerHTML = ''; // Clear previous reports

        const reports = JSON.parse(localStorage.getItem('userReports')) || [];
        reports.forEach((report, index) => {
            const reportItem = document.createElement('div');
            reportItem.className = 'report-item';
            reportItem.innerHTML = `
                <strong>Report ${index + 1}:</strong><br>
                Name: ${report.name}<br>
                Registration Number: ${report.regNumber}<br>
                Date of Birth: ${report.dob}<br>
                Class: ${report.class}
            `;
            reportsList.appendChild(reportItem);
        });
    }

    document.getElementById('profileForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const userId = document.getElementById('userId').value;
        const password = document.getElementById('password').value;
        const name = document.getElementById('name').value;
        const regNumber = document.getElementById('regNumber').value;
        const dob = document.getElementById('dob').value;
        const className = document.getElementById('class').value;

        // Save profile data to local storage
        const userProfile = { userId, password, name, regNumber, dob, class: className };
        localStorage.setItem('userProfile', JSON.stringify(userProfile));

        // Save report to local storage
        const reports = JSON.parse(localStorage.getItem('userReports')) || [];
        reports.push(userProfile);
        localStorage.setItem('userReports', JSON.stringify(reports));

        alert('Profile Updated and Report Saved');
    });

    function logout() {
        // Redirect to login page
        window.location.href = 'index.html';
    }

    // Load user profile on page load
    const userProfile = JSON.parse(localStorage.getItem('userProfile'));
    if (userProfile) {
        document.getElementById('userId').value = userProfile.userId || '';
        document.getElementById('password').value = userProfile.password || '';
        document.getElementById('name').value = userProfile.name || '';
        document.getElementById('regNumber').value = userProfile.regNumber || '';
        document.getElementById('dob').value = userProfile.dob || '';
        document.getElementById('class').value = userProfile.class || '';
    }
    // Redirect to Form Creation Page
function createForm() {
    alert('Redirecting to Form Creation...'); 
    // Add actual redirection logic here, e.g., window.location.href = 'create-form.html';
}

// Redirect to View Report Page
function viewReport() {
    alert('Redirecting to View Report...'); 
    // Add actual redirection logic here, e.g., window.location.href = 'view-report.html';
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulate authentication (this would be done on the server in a real app)
    if (username === 'admin' && password === 'admin123') {
        // Redirect to Admin Dashboard
        window.location.href = 'admin.html';
    } else if (username === 'user' && password === 'user123') {
        // Redirect to User Dashboard
        window.location.href = 'user.html';
    } else {
        alert('Invalid username or password');
    }
});

function logout() {
    // Redirect to login page
    window.location.href = 'index.html';
}

});
