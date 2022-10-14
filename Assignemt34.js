// Assignment: 34 Javascript Basics

// Python Web Development in Hindi

// 1. Declare firstName, lastName, country, city, age, isMarried, year variable and assign
// value to it and use the typeof operator to check different data types.

var firstname="ineuron";
let lastname="mysirg";
const country="India";
const city="Bhopal";
let age=30;

let isMarried="NO";
const year=2022;
console.log(firstname);
console.log(typeof firstname);

console.log(lastname);
console.log(typeof lastname);

console.log(country);
console.log(typeof country);

console.log(city);
console.log(typeof city);

console.log(age);
console.log(typeof age);

console.log(isMarried);
console.log(typeof isMarried);

console.log(year);
console.log(typeof year);

// template literaly
console.log(`

Name is ${firstname}
Last name is ${lastname}
Country name is ${country}
city name is  ${city}
Age is ${age}
isMarried is ${isMarried}
Year name is ${year}

`);



// 2. Boolean value is either true or false.
// a. Write three JavaScript statements which provide truthy value.

var a=10;
var b=40;
console.log(a<b);    //truthy values
var a=10;
var b=10;
console.log(a==b);     //truthy values
console.log(a===b);      //trythy values
console.log(4 > 3 && 10 < 12);
console.log(4 > 3 || 10 < 12); 

// b. Write three JavaScript statements which provide falsy value.

var a=10;
var b=40;
console.log(a==b);   //falsy value
console.log(a==b);      //falsy value

console.log(a>b);          //falsy value
console.log(4 > 3 && 10 > 12) ;




// 3. Figure out the result of the following expressions first without using console.log().
// After you decide the result confirm it by using console.log()
// a. 4 > 3 && 10 < 12
console.log(4 > 3 && 10 < 12);    //true values

// b. 4 > 3 && 10 > 12
console.log(4 > 3 && 10 > 12) ;       //falsy value

// c. 4 > 3 || 10 < 12
console.log(4 > 3 || 10 < 12);         //true valuse
// d. 4 > 3 || 10 > 12
console.log(4 > 3 || 10 > 12);            //true valuse
// e. !(4 > 3)
console.log(!(4 > 3));                  //falsy value
// f. !(4 < 3)
console.log(!(4 < 3));                    //true value
// g. !(false)
console.log(!(false));                     //true value
// h. !(4 > 3 && 10 < 12)
console.log(!(4 > 3 && 10 < 12));              //falsy values
// i. !(4 > 3 && 10 > 12)
console.log( !(4 > 3 && 10 > 12));              //true 
// j. !(4 === '4')
console.log(!(4 === '4'));                  //true

// 4. Even numbers are divisible by 2 and the remainder is zero. How do you check, if a
// number is even or not using JavaScript?

let a=2;
if(a%2==0)
{
    console.log("divisible by 2")
} 
else
{
    console.log("not divisible by 2")
}


// 5. Write a code which can give grades to students according to theirs scores:
// a. 80-100, A
// b. 70-89, B

// Untitled 2

// c. 60-69, C
// d. 50-59, D
// e. 0-49, F

if(80>=100){
    console.log("Grade A")
}elseif(70>=89)
{
    console.log("Grade B")
}elseif(60>=69)
{
    console.log("Grade C")
}
elseif(50>=59)
{
    console.log("Grade D")
}
elseif(0>=49)
{
    console.log("Fail")
}


// 6. Write a program which tells the number of days in a month.

 // dout

// 7. Create a human readable time format using the Date time object
// // a. YYYY-MM-DD HH:mm

now=new Date;
console.log(now.toString());
console.log(now.getDay());
console.log(getMouth());
console.log(now.getMinutes());
console.log(now.getFullYear());

// b. DD-MM-YYYY HH:mm
now=new Date();
console.log(now.toString());
console.log(now.getDate());
console.log(now.getFullYear());
console.log(now.getMilliseconds());
// c. DD/MM/YYYY HH:mm
now=new Date();
console.log(now.toString());
console.log(now.getSeconds());
console.log(now.getTime());
console.log(now.getUTCHours());

// 8. Suppose 1 dollar is equal to 82.23 Indian rupee, create a program which converts
// dollars to rupees.

//confusion


// 9. Write a program to print unit digit of a given number.
// Input : 6693
// Output : 3

let number="6693";
console.log(number[3]);

// 10. Write a program to find the area of the circle. Take radius of circle from user as input
// and print the result in below given format.
// Expected output format – “Area of circle is A having the radius R”. Replace A with area
// & R with radius

//dout

// Facing Issues 🥲
// If you are facing any issues, please reach out to us at anurag@ineuron.ai,
// adityachaudhary@ineuron.ai

// Created By @Anurag Tiwari