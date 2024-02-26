// Task 2 Test Cases

const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function() {
  it('should return the sum of two rounded numbers when type is SUM', function() {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });

  it('should return the subtraction of two rounded numbers when type is SUBTRACT', function() {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });

  it('should return the division of two rounded numbers when type is DIVIDE', function() {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });

  it('should throw an error for invalid type', function() {
    expect(() => calculateNumber('INVALID', 1, 2)).to.throw(Error);
  });
});
