export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw Error('Position outside range');
  }
  const b = new ArrayBuffer(length);
  const x = new Int8Array(b, 0, length);
  x.set([value], position);
  return new DataView(b);
}
