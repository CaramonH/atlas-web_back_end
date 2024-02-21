// Function countStudents logs number of students in each field

const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    // split data into rows and remove empty lines
    const rows = data.split('\n').filter((row) => row.trim());
    // extract headers from the header row
    const [headerRow, ...studentRows] = rows;
    const headers = headerRow.split(',');
    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');
    // retrieve total number of students
    console.log(`Number of students: ${studentRows.length}`);
    //group students by field and count them
    const studentsByField = studentRows.reduce((acc, row) => {
      const fields = row.split(',');
      const field = fields[fieldIndex];
      if (!acc[field]) {
        acc[field] = [];
      }
      acc[field].push(fields[firstNameIndex]);
      return acc;
    }, {});

    const fields = Object.keys(studentsByField);
    for (let i = 0; i < fields.length; i += 1) {
      const field = fields[i];
      const students = studentsByField[field];
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
