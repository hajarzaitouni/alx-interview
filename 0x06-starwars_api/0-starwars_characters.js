#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url + movieId, (err, response, body) => {
  if (err) throw err;
  const actor = JSON.parse(body).characters;
  printName(actor);
});

const printName = (names, i = 0) => {
  if (i === names.length) return;
  request(names[i], (err, response, body) => {
    if (err) throw err;
    const character = JSON.parse(body);
    console.log(character.name);
    printName(names, i + 1);
  });
};
