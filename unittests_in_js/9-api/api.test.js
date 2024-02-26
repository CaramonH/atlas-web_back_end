// Task 9 - Regex Integration Testing

const { expect } = require('chai');
const request = require('request');

describe('Cart page', function() {
  it('should return status code 200 when :id is a number', function(done) {
    request('http://localhost:7865/cart/12', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the message "Payment methods for cart :id" when :id is a number', function(done) {
    request('http://localhost:7865/cart/12', function(error, response, body) {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return status code 404 when :id is NOT a number', function(done) {
    request('http://localhost:7865/cart/hello', function(error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
