
// test/test.js
const assert = require('chai').assert;
const helloWorld = require('../src/index');

describe('HelloWorld Function', () => {
  it('should return Hello, World!', () => {
    assert.equal(helloWorld(), 'Hello, World!');
  });
});
                