/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function (address) {
  let newString = "";
  for (let i = 0; i < address.length; i++) {
    if (address[i] === ".") {
      newString += "[.]";
    } else {
      newString += address[i];
    }
  }
  return newString;
};
