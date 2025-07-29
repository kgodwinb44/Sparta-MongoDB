# MongoDB Comparison Operators

## $eq (Equal to)
- Matches documents where the value of a field is exactly equal to the specified value.
```
db.collection.find({ age: { $eq: 25 } })
```
## $gt (Greater than)
- Matches documents where the value of a field is greater than the specified value.
```
db.collection.find({ age: { $gt: 25 } })
```
## $gte (Greater than or equal to)
- Matches documents where the value of a field is greater than or equal to the specified value.
```
db.collection.find({ age: { $gte: 25 } })
```
## $in (Matches in the array)
- Matches documents where the value of a field is equal to any value in the specified array.
```
db.collection.find({ status: { $in: ["A", "B", "C"] } })
```
## $lt (Less than)
- Matches documents where the value of a field is less than the specified value.
```
db.collection.find({ age: { $lt: 25 } })
```
## $lte (Less Than or Equal)
- Matches documents where the value of a field is less than or equal to the specified value.
```
db.collection.find({ age: { $lte: 25 } })
```
## $ne (Not equal)
- Matches documents where the value of a field is not equal to the specified value.
```
db.collection.find({ status: { $ne: "D" } })
```
## $nin (Not in array)
- Matches documents where the value of a field is not equal to any of the values in the specified array.
```
db.collection.find({ status: { $nin: ["A", "B"] } })
```