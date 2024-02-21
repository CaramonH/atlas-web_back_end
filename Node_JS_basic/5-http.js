// Create a small, more complex HTTP server using the HTTP module

const http = require('http');
const fs = require('fs');

// Create an HTTP server
const server = http.createServer((req, res) => {
  // Handle requests for the root URL
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    // Handle requests for the '/students' URL
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    const path = process.argv[2];
    if (path === undefined) {
      // Send an error message if the database path is not provided
      res.write('Cannot load the database');
      res.end();
      return;
    }

    // Read the database file content
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        // Send an error message if reading the file fails
        res.write('Cannot load the database');
        res.end();
        return;
      }

      const rows = data.trim().split('\n');
      const students = rows.slice(1);

      const csStudentsList = [];
      const sweStudentsList = [];

      students.forEach((row) => {
        const [name, , , field] = row.split(',');
        if (field === 'CS') csStudentsList.push(name);
        if (field === 'SWE') sweStudentsList.push(name);
      });

      // Output the number of students, CS students, and their names
      res.write(`Number of students: ${students.length}\n`);
      res.write(`Number of students in CS: ${csStudentsList.length}. List: ${csStudentsList.join(', ')}\n`);
      // Output the number of SWE students and their names
      res.write(`Number of students in SWE: ${sweStudentsList.length}. List: ${sweStudentsList.join(', ')}`);
      res.end(); // End the response
    });
  } else {
    // Handle unknown routes
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Resource not found');
  }
});

const port = 1245;
// Start the server
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

module.exports = server;
