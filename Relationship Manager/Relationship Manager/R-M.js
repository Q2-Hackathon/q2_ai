const drpbtn1 = document.getElementById('drpbtn1');
const drpopt1 = document.getElementById('drpopt1');

drpbtn1.addEventListener('click', () => {
    if (drpopt1.style.display === 'none') {
        drpopt1.style.display = 'block';
    } else {
        drpopt1.style.display = 'none';
    }
});
const drpbtn2 = document.getElementById('drpbtn2');
const drpopt2 = document.getElementById('drpopt2');

drpbtn2.addEventListener('click', () => {
    if (drpopt2.style.display === 'none') {
        drpopt2.style.display = 'block';
    } else {
        drpopt2.style.display = 'none';
    }
});

// let Customer = [
//     {
//         Customer_ID: 1,
//         Name: "Shivam Mishra",
//         Age: "19",
//         Location: "San Francisco,CA",
//         Credit_Score: "750",
//         Has_Credit_Card: "Yes",
//         Estimated_Salary: "$100,000",
//         Excited: "Yes",
//         Tenure: "5 years",
//         Marital: "Married",
//         Loan_Type: "Car",
//     },
//     {
//         Customer_ID: 2,
//         Name: "Aditya Pratap Singh",
//         Age: "32",
//         Location: "San Francisco,CA",
//         Credit_Score: "750",
//         Has_Credit_Card: "Yes",
//         Estimated_Salary: "$100,000",
//         Excited: "Yes",
//         Tenure: "5 years",
//         Marital: "Unmarried",
//         Loan_Type: "Car",
//     },
//     {
//         Customer_ID: 3,
//         Name: "Shivam Mishra",
//         Age: "32",
//         Location: "San Francisco,CA",
//         Credit_Score: "750",
//         Has_Credit_Card: "Yes",
//         Estimated_Salary: "$2100,000",
//         Excited: "Yes",
//         Tenure: "25 years",
//         Marital: "Unmarried",
//         Loan_Type: "Education",
//     },
//     {
//         Customer_ID: 4,
//         Name: "Ritesh Mishra",
//         Age: "42",
//         Location: "San Francisco,CA",
//         Credit_Score: "1750",
//         Has_Credit_Card: "Yes",
//         Estimated_Salary: "$200,000",
//         Excited: "Yes",
//         Tenure: "1 years",
//         Marital: "Unmarried",
//         Loan_Type: "Home",
//     }
// ]
// function displayMovie(data) {

//     document.getElementById("1stsection").innerHTML = "";

//     let i=document.getElementById('customer_id').value;
//     i=i-1;
//     let htmlString = ``;

//     htmlString = htmlString + `
//         <p><b>Customer ID:</b><input type="number">${data[i].Customer_ID}</p>
//         <p><b>Name:</b> ${data[i].Name}</p>
//         <p><b>Age:</b> ${data[i].Age}</p>
//         <p><b>Location:</b> ${data[i].Location}</p>
//         <p><b>Credit Score:</b> ${data[i].Credit_Score}</p>
//         <p><b>Has Credit Card:</b> ${data[i].Has_Credit_Card}</p>
//         <p><b>Estimated Salary:</b> ${data[i].Estimated_Salary}</p>
//         <p><b>Excited:</b> ${data[i].Excited}</p>
//         <p><b>Tenure:</b> ${Tenure}</p>
//         <p><b>Marital:</b> ${Marita}</p>
//         <p><b>Loan Type:</b> ${Loan_Type}</p>
//         `;


//     document.getElementById('1stsection').innerHTML = htmlString;

// }
// displayMovie(Customer);
