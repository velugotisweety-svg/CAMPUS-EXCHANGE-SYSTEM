
// const items = [
//   {
//     id: 1,
//     name: "Wireless Headphones",
//     category: "electronics",
//     price: 1200,
//     condition: "Like New",
//     seller: "Rahul",
//     phone: "9876543210",
//     postedDate: "2026-01-12",
//     description: "High quality wireless headphones with excellent sound and battery life.",
//     image: "images/headphones.jpg"
//   },
//   {
//     id: 2,
//     name: "Bluetooth Speaker",
//     category: "electronics",
//     price: 900,
//     condition: "Used",
//     seller: "Anjali",
//     phone: "9123456780",
//     postedDate: "2026-01-10",
//     description: "Portable Bluetooth speaker with good bass and clear audio.",
//     image: "images/speaker.jpg"
//   },
//   {
//     id: 3,
//     name: "Laptop Stand",
//     category: "accessories",
//     price: 500,
//     condition: "Good",
//     seller: "Suresh",
//     phone: "9988776655",
//     postedDate: "2026-01-08",
//     description: "Adjustable laptop stand suitable for study and work setups.",
//     image: "images/laptop_stand.jpg"
//   },
//   {
//     id: 4,
//     name: "Operating Systems Book",
//     category: "books",
//     price: 350,
//     condition: "Good",
//     seller: "Divya",
//     phone: "9012345678",
//     postedDate: "2026-01-06",
//     description: "Operating Systems textbook useful for engineering students.",
//     image: "images/book.jpg"
//   },
//   {
//     id: 5,
//     name: "Study Chair",
//     category: "furniture",
//     price: 900,
//     condition: "Used",
//     seller: "Amit",
//     phone: "9090909090",
//     postedDate: "2026-01-05",
//     description: "Comfortable study chair in good condition.",
//     image: "images/chair.jpg"
//   },
//   {
//     id: 6,
//     name: "Lunch Box Set",
//     category: "daily",
//     price: 300,
//     condition: "Good",
//     seller: "Pooja",
//     phone: "8899776655",
//     postedDate: "2026-01-03",
//     description: "Durable lunch box set suitable for daily campus use.",
//     image: "images/lunch_box.jpg"
//   },
//   {
//     id: 7,
//     name: "Electric Kettle",
//     category: "electronics",
//     price: 800,
//     condition: "Used",
//     seller: "Kiran",
//     phone: "9345678123",
//     postedDate: "2026-01-01",
//     description: "Electric kettle for quick boiling, ideal for hostels.",
//     image: "images/kettle.jpg"
//   }
// ];
// function loadItemsFromBackend() {
//   fetch('http://127.0.0.1:5000/items')
//     .then(res => res.json())
//     .then(data => {
//       items = data;
//       displayItems(items); // tumhara existing function
//     })
//     .catch(err => console.log(err));
// }

// // page load pe call
// window.onload = loadItemsFromBackend;
let items = [];  // sirf ye rakho

function loadItemsFromBackend() {
  fetch('http://127.0.0.1:5000/items')
    .then(res => res.json())
    .then(data => {
      items = data;
      displayItems(items); // existing function
    })
    .catch(err => console.log(err));
}

// page load pe call
window.onload = loadItemsFromBackend;
