module.exports = function calculateNumber(type, a, b) {
  const validType = type === 'SUM' || type === 'SUBTRACT' || type === 'DIVIDE';
  if (isNaN(a) || isNaN(b) || !validType) {
    throw new TypeError();
  }
  if (type === 'SUM') {
    return Math.round(a) + Math.round(b);
  }
  if (type === 'SUBTRACT') {
    return Math.round(a) - Math.round(b);
  }
  if (type === 'DIVIDE' && b !== 0) {
    return Math.round(a) / Math.round(b);
  }
  return 'Error';
};
