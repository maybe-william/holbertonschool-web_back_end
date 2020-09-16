export default function handleResponseFromAPI(promise) {
  promise.then((success) => {
    console.log('Got a response from the API');
    return success;
  }, () => new Error());
}
