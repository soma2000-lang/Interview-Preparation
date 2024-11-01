class BloomFilter {
    constructor(size, hashFunctions) {
      this.size = size;
      this.hashFunctions = hashFunctions;
      this.bitArray = Array(size).fill(false);
    }
  
    add(item) {
      this.hashFunctions.forEach(hashFn => {
        const index = hashFn(item) % this.size;
        this.bitArray[index] = true;
      });
    }
  
    contains(item) {
      return this.hashFunctions.every(hashFn => {
        const index = hashFn(item) % this.size;
        return this.bitArray[index];
      });
    }
  }
  
  // Example usage with hash functions
  const hashFn1 = (str) => [...str].reduce((acc, ch) => acc + ch.charCodeAt(0), 0);
  const hashFn2 = (str) => [...str].reduce((acc, ch) => acc * 31 + ch.charCodeAt(0), 1);
  const bloomFilter = new BloomFilter(100, [hashFn1, hashFn2]);
  
  bloomFilter.add("hello");
  console.log(bloomFilter.contains("hello"));  // true
  console.log(bloomFilter.contains("world"));  // false or true (probabilistic)
  