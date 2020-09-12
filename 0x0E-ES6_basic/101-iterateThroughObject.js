export default function iterateThroughObject(reportWithIterator) {
  let first = true;
  let ret = '';
  for (const x of reportWithIterator) {
    if (!first) {
      ret += ' | ';
    }
    ret += x.toString();
    first = false;
  }
  return ret;
}
