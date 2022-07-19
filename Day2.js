
function minimumWaitingTime(queries) {
    queries = queries.sort((a, b) => a - b); // nlogn - time taken by sorting algorithm
    let total = 0

    for (let i = 0; i < queries.length; i++) { // n for the loop on queries
        total += queries[i] * (queries.length - (i + 1))
    }
  return total;
}
