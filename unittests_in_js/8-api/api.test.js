// Task 8 Test Cases

const { expect } = require('chai');
const request = require('request');

describe('Index page', function() {
  it('should return status code 200', function(done) {
    request('http://localhost:7865', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the message "Welcome to the payment system"', function(done) {
    request('http://localhost:7865', function(error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
