const fs = require('fs');
const filePath = './loc.json';

const city_name = process.argv[2];
const overall_weather = process.argv[3];
const aqi = process.argv[4];

fs.readFile(filePath, 'utf8', (err, data) => {

	    let jsonData = {};

	  // If file exists and has content
	     if (!err && data) {
	             try {
	                         jsonData = JSON.parse(data);
	                                 } catch (e) {
	                                             console.log("Invalid JSON format. Resetting file.");
	                                                         jsonData = {};
	                                                                 }
	                                                                     }
	
	                                                                         // If file doesn't exist → err.code === 'ENOENT'
	                                                                             if (err && err.code !== 'ENOENT') {
	                                                                                     console.log("Error reading file:", err);
	                                                                                             return;
	                                                                                                 }
	
	                                                                                                     // Append new data
	                                                                                                         jsonData[city_name] = {
	                                                                                                                 overall_weather,
	                                                                                                                         aqi
	                                                                                                                             };
	
	                                                                                                                                 fs.writeFile(filePath, JSON.stringify(jsonData, null, 2), (err) => {
	                                                                                                                                         if (err) {
	                                                                                                                                                     console.log("Error writing file:", err);
	                                                                                                                                                             } else {
	                                                                                                                                                                         console.log("Data saved successfully!");
	                                                                                                                                                                                 }
	                                                                                                                                                                                     });
	                                                                                                                                                                                     });
	
