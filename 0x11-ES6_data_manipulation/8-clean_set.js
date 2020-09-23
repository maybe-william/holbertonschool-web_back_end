export default function cleanSet(set, startString) {
  if (typeof startString === 'string' && startString !== '') {
    const strs = [];
    for (const x of set) {
      if (x.indexOf(startString) === 0) {
        strs.push(x.slice(startString.length));
      }
    }
    return strs.join('-');
  }
  return '';
}
