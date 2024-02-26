// Task 4 Test Cases

const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  let calculateNumberStub;
  let consoleSpy;

  beforeEach(function() {
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    calculateNumberStub.restore();
    consoleSpy.restore();
  });

  it('should call Utils.calculateNumber with correct arguments and log the result', function() {
    const totalAmount = 100;
    const totalShipping = 20;
    sendPaymentRequestToApi(totalAmount, totalShipping);
    expect(calculateNumberStub.calledOnceWithExactly('SUM', totalAmount, totalShipping)).to.be.true;
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});
