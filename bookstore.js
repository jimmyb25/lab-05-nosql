// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
// paste your drop and insertMany commands here
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
// paste your drop and insertMany commands here
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
// paste your find commands here
db.authors.find()
db.books.find()

// Step 6: insert two new books
// paste your insert commands here
db.books.insertOne({ title: "How to Data Science", published_year: 2026, author_ids: [ 'author_005' ] })
db.books.insertOne({ title: '1984', published_year: 1949, author_ids: [ 'author_004' ] })

// Step 7: add missing authors
// paste your insert commands here
db.authors.insertOne({ _id: 'author_004', name: 'George Orwell', nationality: 'British', bio: { short: 'British writer known for dystopian social critique.', long: 'George Orwell was a British writer whose experiences such as living in poverty led him to be a fierce opponent of totalitarianism. His sharp political instincts led him to write Animal Farm and 1984, two of the most influential dystopian pieces of the 20th century.' } })
db.authors.insertOne({ _id: 'author_005', name: 'John Pork', nationality: 'USA', bio: { short: 'American pork man who wrote about data science.', long: 'John Pork was born in Pennsylvania, and grew up to be a great American Data Scientist, who wrote a book explaining how to do data science.' } })

// Step 8: filter books by a list of authors
// paste your find command here
db.books.find({ author_ids: { $in: ["author_001", "author_004"] } })