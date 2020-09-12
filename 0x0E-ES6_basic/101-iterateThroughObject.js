export default function iterateThroughObject(reportWithIterator) {
  let first = true;
  let ret = '';
  let res = reportWithIterator[Symbol.iterator]().next();
  while (!res.done) {
    if (!first) {
      ret = ret.concat(' | ');
    }
    ret = ret.concat(res.value);
    first = false;
    res = reportWithIterator[Symbol.iterator]().next();
  }
  return ret;
}
