// Task 6 Test Cases

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a resolved promise with data when success is true', function(done) {
    getPaymentTokenFromAPI(true).then((result) => {
      expect(result).to.deep.equal({ data: 'Successful response from the API' });
      done();
    });
  });

  it('should return a resolved promise with no data when success is false', function(done) {
    getPaymentTokenFromAPI(false).then((result) => {
      expect(result).to.be.undefined;
      done();
    });
  });
});
