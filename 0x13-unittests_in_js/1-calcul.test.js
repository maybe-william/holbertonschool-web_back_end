const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  it('should add without rounding', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });
  it('should add with rounding', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('should add with rounding on both numbers', function () {
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('should add with rounding up from .5', function () {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('should throw error if NaN passed', function () {
    assert.throws(() => calculateNumber('SUM', NaN, 3.7), { name: 'TypeError' });
  });

  it('should subtract without rounding', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('should subtract with rounding', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('should subtract with rounding on both numbers', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
  });
  it('should subtract with rounding up from .5', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
  });

  it('should divide without rounding', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3), 1 / 3);
  });
  it('should divide with rounding', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 1 / 4);
  });
  it('should divide with rounding on both numbers', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 1 / 4);
  });
  it('should divide with rounding up from .5', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 3.7), 2 / 4);
  });

  it('should not divide dividing by 0', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 0), 'Error');
  });
  it('should not divide if string is wrong value', function () {
    assert.strictEqual(calculateNumber('MULTIPLICATE', 1.2, 3.7), 'Error');
  });
});
