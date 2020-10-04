const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('should work without rounding', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('should work with rounding', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it('should work with rounding on both numbers', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it('should work with rounding up from .5', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
