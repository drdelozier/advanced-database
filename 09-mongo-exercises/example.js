db = connect("mongodb+srv://soliton.sdfdfg.mongodb.net/myFirstDatabase", "<user>", "<password>")	
console.log(db.adminCommand('listDatabases'))
db = db.getSiblingDB('sample_airbnb')
console.log(db.getCollectionNames())
console.log(db.listingsAndReviews.find({number_of_reviews:70}).limit(5))

console.log(db.listingsAndReviews.aggregate({ $unwind: "$reviews" },{$project:{"review_scores.review_scores_rating":1,"reviews.comments":1}}));

