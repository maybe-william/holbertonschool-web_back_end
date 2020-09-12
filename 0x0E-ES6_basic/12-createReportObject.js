export default function createReportObject(employeesList) {
  return {
    getNumberOfDepartments() {
      return employeesList.length;
    },
    allEmployees: [...employeesList],
  };
}
