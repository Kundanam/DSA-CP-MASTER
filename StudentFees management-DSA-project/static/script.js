function addStudent() {
    let student_id = document.getElementById('student_id').value;
    let name = document.getElementById('name').value;
    let class_no = document.getElementById('class_no').value;
    let fees = document.getElementById('fees').value;

    fetch('/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            student_id: student_id,
            name: name,
            class_no: class_no,
            fees: fees
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayStudents() {
    fetch('/display_students')
    .then(response => response.json())
    .then(data => {
        let output = "<h3>Student List</h3><ul>";
        data.forEach(student => {
            output += `<li>${student.id} - ${student.name} - Class ${student.class_no} - Fees: ${student.fees}</li>`;
        });
        output += "</ul>";
        document.getElementById('output').innerHTML = output;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
