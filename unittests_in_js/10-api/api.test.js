// Task 10 Test Cases

const { expect } = require('chai');
const request = require('request');

describe('Login endpoint', function() {
  it('should return the message "Welcome :username" when POST /login with username', function(done) {
    const username = 'Betty';
    request.post('http://localhost:7865/login', { json: { userName: username } }, function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal(`Welcome ${username}`);
      done();
    });
  });
});

describe('Available payments endpoint', function() {
  it('should return status code 200 and the expected payment methods', function(done) {
    request('http://localhost:7865/available_payments', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
      done();
    });
  });
});
