// Recreate a small HTTP server using Express

const express = require('express');
const fs = require('fs').promises; // Import the promises version of fs for asynchronous file operations

// Function to count the number of students in each field
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8'); // Read the file asynchronously
    const rows = data.split('\n').filter(Boolean); // Split the data into rows and remove any empty rows
    const headers = rows.shift().split(','); // Extract the headers from the first row
    const fieldIndex = headers.indexOf('field'); // Get the index of the 'field' column
    const firstNameIndex = headers.indexOf('firstname'); // Get the index of the 'firstname' column
    const fields = [...new Set(rows.map((row) => row.split(',')[fieldIndex]))]; // Get unique field values

    let result = `Number of students: ${rows.length}\n`; // Initialize the result string with total number of students

    // Iterate over each field
    fields.forEach((field) => {
      // Filter the students for the current field
      const students = rows.filter((row) => row.split(',')[fieldIndex] === field);
      // Append the number of students in the current field and their names to the result string
      result += `Number of students in ${field}: ${students.length}. List: ${students.map((student) => student.split(',')[firstNameIndex]).join(', ')}\n`;
    });

    return result; // Return the result string
  } catch (error) {
    throw new Error('Cannot load the database'); // Throw an error if reading the file fails
  }
}

const app = express(); // Create an express application
const port = 1245; // Define the port number

// Define a route for the root URL
app.get('/', (req, res) => {
  res.send('Hello Holberton School!'); // Send a greeting message to the client
});

// Define a route for the '/students' URL
app.get('/students', async (req, res) => {
  try {
    // Call the countStudents function to get the student count data
    const data = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${data}`); // Send the student count data as a response
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`); // Send an error message if an error occurs
  }
});

// Start the server and listen on the specified port
app.listen(port, () => {
  console.log(`Listening on port ${port}.`);
});

module.exports = app; // Export the express application
