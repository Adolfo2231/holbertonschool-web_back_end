const countStudents = require('./2-read_file');

// Test with a valid file path
countStudents('database.csv');

// Test with an invalid file path
try {
  countStudents('nope.csv');
} catch (error) {
  console.error(error.message);
} 