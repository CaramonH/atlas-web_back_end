// Task 3 Test Cases

const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  let calculateNumberSpy;

  beforeEach(function() {
    calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(function() {
    calculateNumberSpy.restore();
  });

  it('should call Utils.calculateNumber with correct arguments and log the result', function() {
    const totalAmount = 100;
    const totalShipping = 20;
    sendPaymentRequestToApi(totalAmount, totalShipping);
    expect(calculateNumberSpy.calledOnceWithExactly('SUM', totalAmount, totalShipping)).to.be.true;
  });
});
