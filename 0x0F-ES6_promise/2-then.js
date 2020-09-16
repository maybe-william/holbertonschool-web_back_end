export default function handleResponseFromAPI(promise) {
  return promise.then((success) => {
    console.log('Got a response from the API');
    return {
      status: 200,
      body: success,
    };
  }, () => new Error());
}
