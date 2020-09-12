export default function createReportObject(employeesList) {
  const ret = {
    allEmployees: [...employeesList],
  };
  let deptNum = 0;
  for (const x in employeesList) {
    if (x !== 'Something weird') {
      ret[x] = employeesList[x];
      deptNum += 1;
    }
  }
  const getNum = () => deptNum;
  ret.getNumberOfDepartments = getNum;
  return ret;
}
