export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw Error('Position outside range');
  }
  const x = new Int8Array(length);
  x.set(value, position);
  return x;
}
