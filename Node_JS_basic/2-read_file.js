// Function countStudents that attempts to read a database synchronously

const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
		throw new Error('Cannot load the database');
	}

	
}