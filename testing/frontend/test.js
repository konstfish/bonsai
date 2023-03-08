test = {
    "metrics": {
      "CPU": {
        "core_count": 5,
        "percent": 2.1
      },
    }
  }

test = {
    "date": "2023-01-22 21:05:08.161899",
    "id": "a44090ccb7c5b7e17a57e83425da99e044f1a2adb9d33333d5ddfa049f8ea63c",
    "metrics": {
      "CPU": {
        "core_count": 5,
        "individual_cores": [
          2.9,
          1,
          1.9,
          2.9,
          1.9
        ],
        "percent": 2.1
      },
      "DISK": {
        "/": {
          "free": 11124613120,
          "used": 48329768960,
          "used_percent": 81.3
        }
      },
      "MEM": {
        "mem_free": 394838016,
        "mem_used": 865271808,
        "percent": 17.1
      },
      "NET": {}
    }
  }

function flattenDict(ob) {
    var toReturn = {};

    for (var i in ob) {
        if (!ob.hasOwnProperty(i)) continue;

        if ((typeof ob[i]) == 'object' && ob[i] !== null) {
            var flatObject = flattenDict(ob[i]);
            for (var x in flatObject) {
                if (!flatObject.hasOwnProperty(x)) continue;
                toReturn[i + '.' + x] = flatObject[x];
            }
        } else {
            toReturn[i] = ob[i];
        }
    }
    return toReturn;
}


console.log(flattenDict(test))
console.log(
    Object.keys(flattenDict(test)))

// pfuscher weg
let key = "metrics.CPU.core_count";
let value = eval("test." + key);
console.log(value); // Output: 5

// proper weg
let key2 = "metrics.CPU.core_count";
let keys2 = key.split(".");
console.log(keys2)
let value2 = keys2.reduce((obj, key2) => obj[key2], test);
console.log(value2)