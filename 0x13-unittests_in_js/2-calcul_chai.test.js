const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  it('should add without rounding', function () {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });
  it('should add with rounding', function () {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('should add with rounding on both numbers', function () {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });
  it('should add with rounding up from .5', function () {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });
  it('should throw error if NaN passed', function () {
    expect(() => calculateNumber('SUM', NaN, 3.7)).to.throw(TypeError,'');
  });

  it('should subtract without rounding', function () {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
  });
  it('should subtract with rounding', function () {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
  });
  it('should subtract with rounding on both numbers', function () {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
  });
  it('should subtract with rounding up from .5', function () {
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
  });

  it('should divide without rounding', function () {
    expect(calculateNumber('DIVIDE', 1, 3)).to.equal(1 / 3);
  });
  it('should divide with rounding', function () {
    expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(1 / 4);
  });
  it('should divide with rounding on both numbers', function () {
    expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.equal(1 / 4);
  });
  it('should divide with rounding up from .5', function () {
    expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.equal(2 / 4);
  });

  it('should not divide dividing by 0', function () {
    expect(calculateNumber('DIVIDE', 1.2, 0)).to.equal('Error');
  });
  it('should not divide if string is wrong value', function () {
    expect(() => calculateNumber('MULTIPLICATE', 1.2, 3.7)).to.throw(TypeError,'');
  });
});
