module.exports = function countStudents(filename) {
  const readline = require('readline');
  const fs = require('fs');

  const stream = fs.createReadStream(filename);
  stream.on('error', () => {
      throw Error("Cannot load the database");
  });
  const reader = readline.createInterface({
      input: stream
    });

  let fields = []
  const objs = []


  setTimeout(() => {

  reader.on('line', (line) => {
    if (fields === []){
      fields = line.replace(/\n/, "").split(",");
    } else {
      const obj = {};
      values = line.replace(/\n/, "").split(",");
      for (let i; i < values.length; i++) {
        obj[fields[i]] = values[i];
      }
      objs.push(obj);
    }
  });


  if (fields.length > 0) {
    console.log(`Number of students: ${objs.length}`);
  }

  let study = new Set();
  objs.map((x) => study.add(x.field));
  for (const area of study) {
    const in_study = objs.filter((a) => a.field === area);
    const first = in_study.map((b) => b.firstname).join(", ");
    console.log(`Number of students in ${area}: ${in_study.length}. List: ${first}`);
  }
  }, 2000);
}
